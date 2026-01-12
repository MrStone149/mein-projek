# Lernfeld 5: Fertigen von Einzelteilen mit Werkzeugmaschinen

In den Lernfeldern 1 und 2 haben Sie grundlegende Kenntnisse zur Fertigung von Bauelementen mit handgeführten Werkzeugen oder mit Maschinen erworben. Darauf aufbauend befassen Sie sich in diesem Lernfeld damit, auftragsbezogen unter Berücksichtigung des Arbeits- und Umweltschutzes Werkstücke aus verschiedenen Werkstoffen auf Werkzeugmaschinen herzustellen. Zur Feinbearbeitung der Werkstücke lernen Sie dabei als neues Fertigungsverfahren z. B. das Schleifen kennen.

Grundlage Ihres Arbeitsauftrages wird in den meisten Fällen eine Fertigungszeichnung sein. Dieser entnehmen Sie die Informationen, die Sie benötigen, um die erforderlichen Fertigungsverfahren und Fertigungsschritte festzulegen. Sie erstellen Arbeitspläne, wählen geeignete Spannmittel aus und richten die Maschine ein. Schließlich entwickeln Sie Prüfpläne und wählen die geeigneten Prüfmittel aus. Bei all diesen Tätigkeiten beachten Sie die Wirtschaftlichkeit Ihrer Entscheidungen.

[ABBILDUNG: Ein Prozessdiagramm visualisiert den Zerspanungsprozess. Oben sind die Eingangsgrößen Rohteil (Werkstoff, Abmessungen) und die Anforderungen (Fertigteil-Eigenschaften wie Formen, Toleranzen, Oberflächenqualität sowie Kostengünstige Fertigung, Arbeitssicherheit und Umweltschutz) dargestellt. In der Mitte wird der Zerspanungsprozess als Transformation von Stofffluss (Rohteil zu Fertigteil und Spänen) und Energiefluss (mechanische Energie zu Wärmeenergie) unter Berücksichtigung des Informationsflusses gezeigt. Unten sind die Einflussmöglichkeiten der Fachkraft aufgelistet.]

**Einflussmöglichkeiten der Fachkraft durch Wahl von**

| technologische Daten | Werkzeug | Werkzeugmaschine | Spannmitteln | Kühlschmiermittel |
| :--- | :--- | :--- | :--- | :--- |
| Schnittgeschwindigkeit; Vorschub; Schnitttiefe | Schneidengeometrie; Schneidstoff | Typ; Genauigkeit; Antriebsleistung | Werkstück; Werkzeug | Kühlung; Schmierung; Trockenbearbeitung; Minimalschmierung |

## 1 Einflussgrößen beim maschinellen Zerspanen mit geometrisch bestimmter Schneide

Mithilfe von Werkzeugmaschinen wird aus einem Rohteil ein funktionsfähiges Fertigteil (finished part) hergestellt. Dabei ist es die Aufgabe der Fachkraft, den Zerspanungsprozess (machining operation) entsprechend zu gestalten. Um begründete Entscheidungen treffen zu können, muss sie die Auswirkungen kennen, die durch das Verändern der Prozesskenngrößen entstehen.

### 1.1 Technologische Daten und deren Auswirkungen

#### 1.1.1 Bewegungen und Geschwindigkeiten

Meistens sind drei Bewegungen zur Zerspanung erforderlich:
- **Schnittbewegung**
- **Vorschubbewegung** und
- **Zustellbewegung** (Bilder 1 und 2)

[ABBILDUNG: Darstellung der Bewegungen beim Drehen an einem zylindrischen Werkstück. Eingezeichnet sind die Schnittbewegung $v_c$, die Vorschubbewegung $v_f$ und die Zustellbewegung $a_p$.]
**Bild 1: Bewegungen beim Drehen**

[ABBILDUNG: Darstellung der Bewegungen beim Fräsen. Gezeigt wird ein rotierender Fräser mit Schnittbewegung $v_c$, Vorschubbewegung $v_f$ und Zustellbewegung.]
**Bild 2: Bewegungen beim Fräsen**

**Schnittgeschwindigkeit**
Die Wahl der **Schnittgeschwindigkeit** (cutting speed) $v_c$ richtet sich vorrangig nach
- dem **Werkstoff des Werkzeugs** (Schneidstoff): je härter, desto höher $v_c$
- dem **Werkstoff des Werkstücks**: je härter, desto niedriger $v_c$
- der **Art der Zerspanung**: bei Grobbearbeitung ist $v_c$ niedriger als bei Feinbearbeitung
- der **Kühlschmierung**: mit Kühlschmierung kann $v_c$ höher als ohne gewählt werden

Optimale Schnittgeschwindigkeiten können Tabellen der Schneidstoffhersteller oder dem Tabellenbuch entnommen werden. Aufgrund der Formel für die Schnittgeschwindigkeit $v_c$ kann die erforderliche **Umdrehungsfrequenz** $n$ bestimmt werden.

$v_c = d \cdot \pi \cdot n$
$n = \frac{v_c}{d \cdot \pi}$

$v_c$: Schnittgeschwindigkeit; $d$: Durchmesser; $n$: Umdrehungsfrequenz

**Vorschub und Vorschubgeschwindigkeit**
Der **Vorschub** (feed) je Umdrehung $f$ bzw. je Zahn $f_z$ ist in erster Linie abhängig von
- der **gewünschten Oberflächenqualität** (surface quality): je kleiner der Vorschub, desto besser die Oberflächenqualität (Bilder 3 und 4)
- der **Art der Zerspanung**: bei Grobbearbeitung (rough working) wird der Vorschub größer gewählt. Dadurch nimmt die Vorschubgeschwindigkeit zu und die Fertigungszeit ab
- dem **Werkstoff des Werkstücks** (material of workpiece): je härter, desto niedriger $f$ bzw. $f_z$
- dem **Werkstoff des Schneidstoffs** (cutting material): je härter, desto höher $f$ bzw. $f_z$

[ABBILDUNG: Schematische Darstellung beim Fräsen mit Kennzeichnung des Vorschubs $f_z$ je Zahn und des Arbeitseingriffs $a_e$.]
**Bild 3: Vorschub $f_z$ je Zahn und Arbeitseingriff $a_e$ beim Fräsen**

[ABBILDUNG: Vergleich der Oberflächenqualität bei unterschiedlichen Vorschüben. Ein großer Vorschub erzeugt ein grobes Profil, ein kleiner Vorschub ein feineres Profil.]
**Bild 4: Vorschub und Oberflächenqualität**

Schneidstoffhersteller empfehlen erprobte Vorschübe in Tabellen. Die **Vorschubgeschwindigkeit** (feed speed) $v_f$ ist der pro Minute zurückgelegte Weg. Sie ist mit folgenden Formeln zu berechnen.

- Beim **Drehen**: $v_f = f \cdot n$
- Beim **Fräsen**: $v_f = f_z \cdot z \cdot n$

$v_f$: Vorschubgeschwindigkeit; $f$: Vorschub je Umdrehung; $f_z$: Vorschub je Zahn; $n$: Umdrehungsfrequenz

Die **Wirkgeschwindigkeit** $v_e$ (Bilder 1 und 2 auf Seite 2) ist die resultierende Geschwindigkeit aus **Schnittgeschwindigkeit** $v_c$ und **Vorschubgeschwindigkeit** $v_f$. Meist ist das Verhältnis von Schnittgeschwindigkeit zu Vorschubgeschwindigkeit sehr groß, dann gilt $v_e \approx v_c$.

**Zustellbewegungen**
Zustellbewegungen (infeed motions) legen beim Drehen die **Schnitttiefe** $a_p$ und beim Fräsen den **Arbeitseingriff** $a_e$ fest (Bilder 1 und 2 und Seite 2 Bild 3). Beide bestimmen die Dicke der zu zerspanenden Schicht.

[ABBILDUNG: Darstellung des Plandrehens mit Kennzeichnung von Vorschub $f$ je Umdrehung und Schnitttiefe $a_p$.]
**Bild 1: Vorschub $f$ je Umdrehung und Schnitttiefe $a_p$ beim Plandrehen**

[ABBILDUNG: Darstellung des Fräsvorgangs mit Kennzeichnung von Schnitttiefe $a_p$ und Arbeitseingriff $a_e$.]
**Bild 2: Schnitttiefe $a_p$ und Arbeitseingriff $a_e$ beim Fräsen**

**Überlegen Sie**
1. Welche Auswirkungen entstehen, wenn nur Schnitt- und Zustellbewegung beim Spanen vorhanden sind?
## 2. Von welchen Faktoren hängt die Wahl der Schnittgeschwindigkeit ab?
3. Wie groß ist die Vorschubgeschwindigkeit beim Fräsen, wenn der Fräser mit 6 Zähnen eine Umdrehungsfrequenz von $2500 \, \text{min}^{-1}$ besitzt und ein Vorschub je Zahn von $0,08 \, \text{mm}$ gewählt wird?

#### 1.1.2 Winkel an der Werkzeugschneide

Die **Zerspankraft** (Bild 3) bewirkt gemeinsam mit der Schnittbewegung, dass die Werkzeugschneide in das Werkstück eindringt und einen Span abtrennt. Die Schneidengeometrie der Werkzeugschneide beeinflusst den Zerspanungsprozess maßgeblich:

**MERKE**
- Mit steigendem **Keilwinkel** (wedge angle) $\beta$ nimmt die Stabilität der Werkzeugschneide zu: Je härter der Werkstoff des Werkstücks, desto größer ist $\beta$ zu wählen.
- Der **Freiwinkel** (clearance angle) $\alpha$ vermindert die Reibung zwischen der Freifläche des Werkzeugs und dem Werkstück. Mit steigendem Freiwinkel $\alpha$ verbessert sich die Qualität der Werkstückoberfläche und vermindert sich die Wärmeaufnahme des Werkzeugs. Dabei nimmt jedoch gleichzeitig der Keilwinkel $\beta$ ab.
- Der **Spanwinkel** (rake angle) $\gamma$ wirkt sich auf die Spanbildung aus. Mit zunehmendem Spanwinkel $\gamma$ wird die erforderliche Zerspankraft kleiner.
- $\alpha + \beta + \gamma = 90^\circ$

[ABBILDUNG: Schematische Darstellung des Zerspanungsvorgangs. Gezeigt werden Spanfläche, Freifläche, Zerspankraft sowie die Winkel $\alpha$ (Freiwinkel), $\beta$ (Keilwinkel) und $\gamma$ (Spanwinkel).]
**Bild 3: Zerspanungsvorgang**

#### 1.1.3 Spanarten und Spanformen

Selbst bei gleichem zu zerspanendem Werkstoff können durch Verändern der Prozesskenngrößen unterschiedliche Spanarten entstehen (Seite 4 Bild 1).

**MERKE**
Aufgrund der Spanentstehung werden drei typische **Spanarten** (kinds of chips) unterschieden: **Reißspan**, **Scherspan** und **Fließspan**.

| Spanart | Kennzeichen | Gründe | Auswirkungen |
| :--- | :--- | :--- | :--- |
| **Reißspan** | vorauseilender Riss; Herausreißen einzelner Spanteile aus dem Werkstück; kurze, nicht zusammenhängende Späne; raue Werkstückoberfläche; problemlose Spanabfuhr | | |
| **Scherspan** | In der Scherzone getrennte Spanteile verschweißen teilweise wieder; schuppiger Span | - zunehmende Verformbarkeit des Werkstoffs; - steigende Schnittgeschwindigkeit; - zunehmender Spanwinkel; - abnehmender Vorschub; - abnehmende Schnitttiefe | - bessere Oberflächenqualität; - kleinere Maßtoleranzen; - kleinere Schnittkraftschwankungen; - bessere Form- und Lagetoleranzen |
| **Fließspan** | Umformen des Werkstoffs in der Scherebene; kein Trennen des Spans; langer, fortlaufender Span; schwierige Spanabfuhr | | |

[ABBILDUNG: Illustration der drei Spanarten: Reißspan (bröckelig), Scherspan (lamellenartig) und Fließspan (kontinuierlich).]
**Bild 1: Spanarten**

[ABBILDUNG: Übersicht verschiedener Spanformen: Bröckelspäne, Spiralspäne, kurze Wendelspäne und Spiralwendelspäne.]
**Bild 2: Erwünschte Spanformen**

Die Einstellwerte und die Schneidengeometrie beeinflussen die Spanform.

**MERKE**
Erwünscht sind **kurze Spanformen** (shapes of chips) (Bild 2), die gut von der Werkzeugschneide abgeführt werden können und nicht sperrig sind.

Optimal ist ein Span, der die Vorteile der Fließspanbildung besitzt und gleichzeitig in kurzen Stücken vorliegt. Da durch die Fließspanbildung normalerweise eine lange, unerwünschte Spanform entsteht, muss der Span noch gebrochen werden. Den **Spanbruch** übernehmen **Spanformer** bzw. **Spanleitstufen**.

[ABBILDUNG: Detailansicht von Wendeschneidplatten mit integrierten Spanformern bzw. Spanleitstufen zur Kontrolle des Spanbruchs.]
**Bild 3: Spanformer bzw. Spanleitstufen bei Wendeschneidplatten**