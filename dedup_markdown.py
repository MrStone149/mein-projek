#!/usr/bin/env python3
"""
Markdown Deduplication Script

Entfernt duplizierte Inhalte am Anfang von aufeinanderfolgenden .md Dateien.
Ursprung: PDFs wurden konvertiert, wobei jede PDF die letzte Seite der vorigen als erste Seite hatte.

Verwendung:
    python dedup_markdown.py --input markdown_fail --output markdown_dedup
"""

import os
import re
import argparse
from pathlib import Path
from difflib import SequenceMatcher
from dataclasses import dataclass
from typing import Optional


@dataclass
class DeduplicationResult:
    """Ergebnis der Deduplizierung einer Datei."""
    filename: str
    original_lines: int
    removed_lines: int
    final_lines: int
    duplicate_found: bool
    match_start_line: int = 0
    match_end_line: int = 0


def normalize_line(line: str) -> str:
    """
    Normalisiert eine Zeile für den Vergleich.
    - Entfernt führende/nachfolgende Leerzeichen
    - Ersetzt mehrfache Leerzeichen durch einzelne
    - Bei "Abbildung:" wird nur der Teil davor + "Abbildung:" behalten
    """
    line = line.strip()
    line = re.sub(r'\s+', ' ', line)

    # "Abbildung:" Handling - ignoriere Beschreibung danach
    abbildung_match = re.search(r'^(.*?Abbildung:\s*).*$', line, re.IGNORECASE)
    if abbildung_match:
        line = abbildung_match.group(1).strip()

    return line


def lines_similar(line1: str, line2: str, threshold: float = 0.85) -> bool:
    """
    Prüft ob zwei Zeilen ähnlich genug sind.
    Verwendet SequenceMatcher für Fuzzy-Matching.
    """
    norm1 = normalize_line(line1)
    norm2 = normalize_line(line2)

    # Leere Zeilen sind gleich
    if not norm1 and not norm2:
        return True

    # Eine leer, andere nicht
    if not norm1 or not norm2:
        return False

    # Exakter Match nach Normalisierung
    if norm1 == norm2:
        return True

    # Fuzzy Match
    ratio = SequenceMatcher(None, norm1, norm2).ratio()
    return ratio >= threshold


def find_duplicate_block_at_start(
    current_lines: list[str],
    previous_lines: list[str],
    min_consecutive_matches: int = 5,
    similarity_threshold: float = 0.85
) -> Optional[int]:
    """
    Findet den duplizierten Block am Anfang der aktuellen Datei.

    Vergleicht den Anfang von current_lines mit dem Ende von previous_lines.

    Returns:
        Index bis zu dem gelöscht werden soll (exklusiv), oder None wenn kein Duplikat.
    """
    if not current_lines or not previous_lines:
        return None

    # Wir suchen nach einem Block am Anfang von current_lines,
    # der mit einem Block am Ende von previous_lines übereinstimmt

    best_match_end = None
    best_match_length = 0

    # Versuche verschiedene Startpositionen in previous_lines (vom Ende her)
    # Wir nehmen an, dass maximal 50% der vorigen Datei dupliziert sein könnte
    max_search_lines = min(len(previous_lines), len(current_lines))

    for prev_start in range(max(0, len(previous_lines) - max_search_lines), len(previous_lines)):
        # Versuche ab dieser Position in previous_lines zu matchen
        consecutive_matches = 0
        current_idx = 0
        prev_idx = prev_start

        while current_idx < len(current_lines) and prev_idx < len(previous_lines):
            if lines_similar(current_lines[current_idx], previous_lines[prev_idx], similarity_threshold):
                consecutive_matches += 1
                current_idx += 1
                prev_idx += 1
            else:
                # Versuche leere Zeilen zu überspringen
                if not normalize_line(current_lines[current_idx]):
                    current_idx += 1
                    continue
                if prev_idx < len(previous_lines) and not normalize_line(previous_lines[prev_idx]):
                    prev_idx += 1
                    continue
                break

        # Wenn wir bis zum Ende von previous_lines gematcht haben und genug Zeilen
        if prev_idx >= len(previous_lines) and consecutive_matches >= min_consecutive_matches:
            if consecutive_matches > best_match_length:
                best_match_length = consecutive_matches
                best_match_end = current_idx

    # Nur zurückgeben wenn wir genug aufeinanderfolgende Matches haben
    if best_match_length >= min_consecutive_matches:
        return best_match_end

    return None


def find_duplicate_by_content_search(
    current_lines: list[str],
    previous_lines: list[str],
    min_consecutive_matches: int = 5,
    similarity_threshold: float = 0.85
) -> Optional[int]:
    """
    Alternative Methode: Sucht nach dem längsten zusammenhängenden Block
    am Anfang von current_lines, der irgendwo in previous_lines vorkommt.
    """
    if not current_lines or not previous_lines:
        return None

    # Normalisiere previous_lines für schnelleren Vergleich
    prev_normalized = [normalize_line(l) for l in previous_lines]

    # Finde die erste nicht-leere Zeile in current_lines
    first_content_idx = 0
    for i, line in enumerate(current_lines):
        if normalize_line(line):
            first_content_idx = i
            break

    first_line_norm = normalize_line(current_lines[first_content_idx])
    if not first_line_norm:
        return None

    # Suche diese Zeile in previous_lines
    potential_starts = []
    for i, prev_norm in enumerate(prev_normalized):
        if lines_similar(current_lines[first_content_idx], previous_lines[i], similarity_threshold):
            potential_starts.append(i)

    best_match_end = None
    best_match_length = 0

    for prev_start in potential_starts:
        # Zähle aufeinanderfolgende Matches
        consecutive = 0
        curr_idx = first_content_idx
        prev_idx = prev_start

        while curr_idx < len(current_lines) and prev_idx < len(previous_lines):
            curr_norm = normalize_line(current_lines[curr_idx])
            prev_norm = normalize_line(previous_lines[prev_idx])

            # Überspringe leere Zeilen
            if not curr_norm:
                curr_idx += 1
                continue
            if not prev_norm:
                prev_idx += 1
                continue

            if lines_similar(current_lines[curr_idx], previous_lines[prev_idx], similarity_threshold):
                consecutive += 1
                curr_idx += 1
                prev_idx += 1
            else:
                break

        if consecutive > best_match_length:
            best_match_length = consecutive
            best_match_end = curr_idx

    if best_match_length >= min_consecutive_matches:
        return best_match_end

    return None


def process_files(
    input_dir: Path,
    output_dir: Path,
    min_consecutive_matches: int = 5,
    similarity_threshold: float = 0.85
) -> list[DeduplicationResult]:
    """
    Verarbeitet alle part_*.md Dateien im Input-Ordner.
    """
    results = []

    # Finde alle part_*.md Dateien und sortiere sie
    md_files = sorted(input_dir.glob("part_*.md"))

    if not md_files:
        print(f"Keine part_*.md Dateien in {input_dir} gefunden.")
        return results

    print(f"Gefunden: {len(md_files)} Dateien")

    # Erstelle Output-Ordner
    output_dir.mkdir(parents=True, exist_ok=True)

    previous_lines: list[str] = []

    for i, md_file in enumerate(md_files):
        print(f"\nVerarbeite: {md_file.name} ({i+1}/{len(md_files)})")

        # Lese aktuelle Datei
        with open(md_file, 'r', encoding='utf-8') as f:
            current_lines = f.readlines()

        original_line_count = len(current_lines)
        result = DeduplicationResult(
            filename=md_file.name,
            original_lines=original_line_count,
            removed_lines=0,
            final_lines=original_line_count,
            duplicate_found=False
        )

        # Erste Datei: Keine Deduplizierung nötig
        if i == 0:
            output_lines = current_lines
            print(f"  -> Erste Datei, keine Deduplizierung")
        else:
            # Suche nach Duplikat am Anfang
            duplicate_end = find_duplicate_block_at_start(
                current_lines,
                previous_lines,
                min_consecutive_matches,
                similarity_threshold
            )

            # Fallback: Alternative Suchmethode
            if duplicate_end is None:
                duplicate_end = find_duplicate_by_content_search(
                    current_lines,
                    previous_lines,
                    min_consecutive_matches,
                    similarity_threshold
                )

            if duplicate_end is not None and duplicate_end > 0:
                result.duplicate_found = True
                result.match_start_line = 1
                result.match_end_line = duplicate_end
                result.removed_lines = duplicate_end
                result.final_lines = original_line_count - duplicate_end

                output_lines = current_lines[duplicate_end:]
                print(f"  -> Duplikat gefunden: Zeilen 1-{duplicate_end} entfernt ({duplicate_end} Zeilen)")
            else:
                output_lines = current_lines
                print(f"  -> Kein Duplikat gefunden")

        # Speichere Output
        output_file = output_dir / md_file.name
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(output_lines)

        # Speichere aktuelle Zeilen für nächste Iteration
        previous_lines = current_lines
        results.append(result)

    return results


def generate_report(results: list[DeduplicationResult], output_dir: Path) -> str:
    """Generiert einen Bericht über die Deduplizierung."""

    report_lines = [
        "# Deduplizierung Report",
        "",
        "## Zusammenfassung",
        "",
        f"- **Dateien verarbeitet:** {len(results)}",
        f"- **Duplikate gefunden:** {sum(1 for r in results if r.duplicate_found)}",
        f"- **Zeilen entfernt (gesamt):** {sum(r.removed_lines for r in results)}",
        "",
        "## Details pro Datei",
        "",
        "| Datei | Original | Entfernt | Final | Duplikat? |",
        "|-------|----------|----------|-------|-----------|",
    ]

    for r in results:
        status = "Ja" if r.duplicate_found else "Nein"
        report_lines.append(
            f"| {r.filename} | {r.original_lines} | {r.removed_lines} | {r.final_lines} | {status} |"
        )

    report_lines.extend([
        "",
        "## Duplikat-Details",
        "",
    ])

    for r in results:
        if r.duplicate_found:
            report_lines.append(f"### {r.filename}")
            report_lines.append(f"- Entfernte Zeilen: 1-{r.match_end_line}")
            report_lines.append(f"- Anzahl entfernt: {r.removed_lines}")
            report_lines.append("")

    report_content = "\n".join(report_lines)

    # Speichere Report
    report_file = output_dir / "DEDUP_REPORT.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report_content)

    return report_content


def main():
    parser = argparse.ArgumentParser(
        description="Entfernt duplizierte Inhalte aus aufeinanderfolgenden Markdown-Dateien."
    )
    parser.add_argument(
        "--input", "-i",
        type=Path,
        default=Path("markdown_fail"),
        help="Input-Ordner mit den Original .md Dateien (default: markdown_fail)"
    )
    parser.add_argument(
        "--output", "-o",
        type=Path,
        default=Path("markdown_dedup"),
        help="Output-Ordner für deduplizierte Dateien (default: markdown_dedup)"
    )
    parser.add_argument(
        "--min-matches", "-m",
        type=int,
        default=5,
        help="Mindestanzahl aufeinanderfolgender ähnlicher Zeilen für Duplikat-Erkennung (default: 5)"
    )
    parser.add_argument(
        "--threshold", "-t",
        type=float,
        default=0.85,
        help="Ähnlichkeits-Schwellenwert 0.0-1.0 (default: 0.85)"
    )

    args = parser.parse_args()

    if not args.input.exists():
        print(f"Fehler: Input-Ordner '{args.input}' existiert nicht.")
        return 1

    print(f"=== Markdown Deduplizierung ===")
    print(f"Input:  {args.input.absolute()}")
    print(f"Output: {args.output.absolute()}")
    print(f"Min. aufeinanderfolgende Matches: {args.min_matches}")
    print(f"Ähnlichkeits-Schwellenwert: {args.threshold}")

    results = process_files(
        args.input,
        args.output,
        args.min_matches,
        args.threshold
    )

    if results:
        report = generate_report(results, args.output)
        print("\n" + "=" * 50)
        print(report)
        print("=" * 50)
        print(f"\nReport gespeichert: {args.output / 'DEDUP_REPORT.md'}")

    return 0


if __name__ == "__main__":
    exit(main())
