### 2.6 Spezielle Drehverfahren

### Beispielrechnungen

[ABBILDUNG: Skizze eines Kegelstumpfes mit den Maßen $D$ (großer Durchmesser), $d$ (kleiner Durchmesser), $l$ (Kegellänge) und dem Einstellwinkel $\alpha/2$.]

$\tan \frac{\alpha}{2} = \frac{D - d}{2 \cdot l}$

$\alpha$: Einstellwinkel
$D$: großer Durchmesser
$d$: kleiner Durchmesser
$L$: Kegellänge

$\tan \frac{\alpha}{2} = \frac{\text{Gegenkathete } G}{\text{Ankathete } A}$
$G = \frac{D - d}{2}$
$A = l$

$\tan \frac{\alpha}{2} = \frac{60 \, \text{mm} - 40 \, \text{mm}}{2 \cdot 80 \, \text{mm}}$
$\tan \frac{\alpha}{2} = 0,125$
$\frac{\alpha}{2} = 7,125^\circ = 7^\circ 7' 30''$

**Bild 1: Berechnung des Einstellwinkels**

Beim Schruppen der Kegelradwelle wird der Oberschlitten um den halben Kegelwinkel, den **Einstellwinkel** $\alpha/2$ (tool cutting edge angle) geschwenkt. Die Genauigkeit der Gradeinteilung ist dabei ausreichend. Beim Schlichten ist eine genauere Einstellung mithilfe eines Lehrdorns (Seite 33 Bild 3) möglich.
Wenn der Zeichnung weder der Kegelwinkel $\alpha$ (taper angle) noch der Einstellwinkel $\alpha/2$ zu entnehmen sind, muss er berechnet werden (Bild 1).
Bei Passkegeln ist oft die **Kegelverjüngung** $C$ (taper ratio) angegeben. Kegelverjüngung $1:4$ bedeutet, dass der Durchmesser des Kegels auf $4 \, \text{mm}$ Länge um $1 \, \text{mm}$ abnimmt. Der Zusammenhang von Einstellwinkel und Kegelverjüngung ist im Bild 2 dargestellt.

#### 2.6.2 Gewindedrehen

An vielen Drehteilen wie z. B. an der Kegelradwelle auf Seite 15 sind Gewinde vorhanden, die meist in mehreren Schnitten hergestellt werden (Bild 3). Obwohl die meisten heute an CNC-Drehmaschinen erstellt werden (siehe Lernfeld 8), sind im Fol-

[ABBILDUNG: Nahaufnahme eines Drehmeißels beim Schneiden eines Gewindes an einem Werkstück.]

**Bild 3: Gewindedrehen (thread turning)**

### Beispielrechnungen

[ABBILDUNG: Skizze eines Kegels mit der Angabe der Kegelverjüngung $C = 1:4$.]

$C = \frac{D - d}{l}$

weiter gilt:
$\frac{C}{2} = \frac{D - d}{2 \cdot l}$
$\tan \frac{\alpha}{2} = \frac{C}{2}$

$C$: Kegelverjüngung
$\frac{C}{2}$: Neigungsverhältnis

$C = \frac{60 \, \text{mm} - 40 \, \text{mm}}{80 \, \text{mm}} = \frac{20 \, \text{mm}}{80 \, \text{mm}}$

Im Zähler muss eine 1 stehen:
$C = \frac{20 \, \text{mm} : 20}{80 \, \text{mm} : 20} = 1:4$
$C = \frac{1}{4} = 1:4$

$\tan \frac{\alpha}{2} = \frac{1}{8}$
$\frac{\alpha}{2} = 7,125^\circ = 7^\circ 7' 30''$

**Bild 2: Einstellwinkel und Kegelverjüngung**

genden auch die Besonderheiten beim Gewindedrehen auf konventionellen Drehmaschinen dargestellt.
- Zum Gewindedrehen werden fast ausschließlich Wendeschneidplatten eingesetzt, wobei drei Typen zur Auswahl stehen (Seite 35 Bild 1).
- Der Gewindedrehmeißel muss genau auf Mitte und rechtwinklig zur Drehachse stehen, ansonsten kommt es zu Profilverzerrungen.
- Die Schnitttiefe je Schnitt beträgt ca. $0,1$ bis $0,15 \, \text{mm}$. Sie nimmt mit tieferem Eindringen ab, damit die Schneidenbelastung nicht zu groß wird. Im Wesentlichen gibt es zwei Zustellungsverfahren (Bild 4).

[ABBILDUNG: Schematische Darstellung der Radialzustellung und Flankenzustellung. Bei der Radialzustellung dringt das Werkzeug mittig ein, bei der Flankenzustellung schräg entlang einer Flanke.]

**Radialzustellung**
- Span entsteht an beiden Flanken der Spitze: ungünstige Schnittbedingung.
- Gleichmäßiger Verschleiß

**Flankenzustellung**
- Span entsteht außer beim letzten Schnitt nur an einer Flanke der Spitze: günstige Schnittbedingung.
- Ungleichmäßiger Verschleiß

**Bild 4: Zustellmöglichkeiten beim Gewindedrehen**

Übungsaufgaben zu Berechnungen beim Kegeldrehen finden Sie auf den Seiten 37 und 38.

---

### 2.6 Spezielle Drehverfahren

[ABBILDUNG: Drei verschiedene Wendeschneidplatten-Profile für das Gewindedrehen: Vollprofil (schneidet das komplette Profil inklusive Spitze), Teilprofil (schneidet nur die Flanken, nicht die Spitze) und Mehrfachzahnprofil (besitzt mehrere Zähne für schnelleren Abtrag).]

**Vollprofil**
- Vom Gewindegrund bis zur Gewindespitze wird ein vollständiges, genaues Profil geschnitten.
- Für jede Gewindesteigung ist eine besondere Schneidplatte erforderlich.

**Teilprofil**
- Die Gewindespitze wird nicht mitgeschnitten.
- In Grenzen können unterschiedliche Steigungen mit der gleichen Schneidplatte erstellt werden.

**Mehrfachzahnprofil**
- Es werden vollständige Gewinde geschnitten.
- Weniger Schnitte bei größeren An- und Überläufen möglich.

**Bild 1: Wendeschneidplatten zum Gewindedrehen**

Bei konventionellen Drehmaschinen kommt die **Leitspindel** (lead screw) als Vorschubantrieb zum Einsatz und es ist die geforderte Gewindesteigung am Vorschubgetriebe einzustellen. Bei CNC-Drehmaschinen ist die Gewindesteigung zu programmieren.
Bei konventionellen Drehmaschinen muss der Bediener am Ende des Gewindes das Werkzeug bei gleichzeitiger Änderung der Spindeldrehrichtung zurückziehen. Das ist nur bei geringen Umdrehungsfrequenzen möglich, d. h., es sind nur kleine Schnittgeschwindigkeiten möglich. Bei CNC-Drehmaschinen ist eine Umkehr der Drehrichtung nicht erforderlich. Die Bewegungen werden automatisiert bei konstanter Umdrehungsfrequenz mit höheren Schnittgeschwindigkeiten durchgeführt.

**Überlegen Sie!**
1. In welchen Punkten unterscheidet sich Gewindedrehen an konventionellen von dem an CNC-Drehmaschinen?
2. Begründen Sie, warum der Drehmeißel auf Mitte und rechtwinklig zur Drehachse stehen muss.

### ÜBUNGEN

### Zeichnungsanalyse

1. Der folgende Ausschnitt ist auf einer Teilzeichnung zu finden:

[ABBILDUNG: Technische Zeichnung eines Wellenendes mit einem Gewinde M20, einer Gesamtlänge von 40 mm und einem Gewindefreistich nach DIN 76-B.]

a) Erklären Sie die Zeichnungsangabe DIN 76-B.
b) Unterscheiden Sie die Formen A und B.
c) Welche Größe bestimmt maßgeblich die einzelnen Maße für den Gewindefreistich?

2. Die Zeichnung eines Drehteils enthält folgende Angabe:

[ABBILDUNG: Technische Zeichnung einer Zentrierbohrung an der Stirnseite einer Welle mit der Beschriftung ISO 6411-B2,5/5,3.]

a) Erklären Sie die Zeichnungsangabe und skizzieren Sie die Einzelheit im Maßstab 5 : 1.
b) Wie tief ist zu bohren?

---

3. Auf das Wellenende soll ein Zahnrad von $55 \, \text{mm}$ Breite, ein Sicherungsring DIN 471 - 30 x 1,5 und eine Passfeder DIN 6885 - A8 x 7 x 40 montiert werden.
a) Skizzieren Sie das Wellenende und tragen Sie die fehlenden Maße ein.

[ABBILDUNG: Technische Zeichnung eines Wellenendes mit Passfedernut. Maße: $56,6^{+0,1}$, Freistich DIN 509-E0,8x0,3, Durchmesser 30m6, Fase 2x45°, Gesamtlänge 60.]

b) Skizzieren Sie den Freistich im Maßstab 10:1 als Detail.
c) Skizzieren Sie den Zusammenbau der Einzelteile im Schnitt.

4. Die Bohrbuchse DIN - A - 12 x 3 20 enthält zwei Lagetoleranzen.

[ABBILDUNG: Schnittzeichnung einer Bohrbuchse mit einem Innendurchmesser von 12F7. Es sind Toleranzen für Rundlauf (0,02 zu A) und Planlauf (0,03 zu A) angegeben.]

a) Welches ist das Bezugselement?
b) Erklären Sie die geforderten Eigenschaften.
c) Entscheiden Sie, in welcher Reihenfolge die Bohrbuchse gedreht wird und geben Sie die dazu erforderlichen Spannmittel an.

## Drehen

1. Welche Auswirkungen haben die Führungen einer Werkzeugmaschine auf das Werkstück und was können Sie dazu beitragen, dass die Führungsqualität hoch bleibt?
2. Nennen Sie zwei Funktionen, die die Arbeitsspindel einer Drehmaschine erfüllt.
3. Unterscheiden Sie Zug- und Leitspindel.
## 4. Welche Aufgaben kann der Reitstock erfüllen?
5. Beschreiben Sie je einen Vor- und Nachteil, den große Eckenwinkel gegenüber kleinen besitzen.
6. Wie verändern sich die Spanungsdicke $h$ und die Spanungsbreite $b$ bei gleichbleibendem Vorschub $f$, wenn der Einstellwinkel von 90° auf 60° abnimmt? Formulieren Sie eine Beziehung „Je ... desto“.
7. Legen Sie für das Drehen der Getriebewelle aus 34CrMo4 (siehe unten) die Arbeitsschritte und die Werkzeuge fest.
## 8. Unter welchen Bedingungen sind im Dreibackenfutter weiche Backen harten vorzuziehen?
9. Legen Sie die Spannmittel für das Drehen der Getriebewelle von Übung 7 fest.
10. Unterscheiden Sie Spanndorn und Spannzange.
11. Welche Probleme können beim Drehen von langen Wellen auftreten und wie können sie gelöst werden?
12. Ein Drehteil aus Vergütungsstahl (25CrMo4) wird mit einer Hartmetallschneide von $\varnothing 60$ auf $\varnothing 52$ bei einem Vorschub von $0,6 \, \text{mm}$ abgedreht.
a) Welche Schnittgeschwindigkeit ist zu wählen?
b) Wie groß wird die Umdrehungsfrequenz?

**zu Übung 7**

[ABBILDUNG: Detaillierte technische Zeichnung einer Getriebewelle mit verschiedenen Absätzen, Passfedernuten, Freistichen und Zentrierbohrungen. Maße beinhalten Durchmesser wie 45m6, 52, 45k6, 44,9-0,1, 33h12, 35k6, 43m6. Längenmaße: 80, 130, 155, 270. Oberflächenangaben Ra 0,8 und Ra 3,2.]

---

13. Ein Bolzen aus C60 wird mit einer beschichteten Hartmetallschneidplatte von $\varnothing 62$ auf $\varnothing 60$ abgedreht. Dabei ist der Vorschub $0,25 \, \text{mm}$ und die Umdrehungsfrequenz $3000/\text{min}$. Ist die Umdrehungsfrequenz richtig eingestellt?
14. Wie verändert sich die Schnittgeschwindigkeit, wenn mit konstanter Umdrehungsfrequenz von $1000/\text{min}$ eine Welle von $50 \, \text{mm}$ auf $10 \, \text{mm}$ Durchmesser querplangedreht wird?
15. Wie müsste sich die Umdrehungsfrequenz an einer CNC-Drehmaschine ändern, wenn bei den gleichen Bedingungen wie in Übung 14 mit einer konstanten Schnittgeschwindigkeit von $150 \, \text{m/min}$ gespant werden soll?
16. Wie groß würde theoretisch die Umdrehungsfrequenz an einer CNC-Drehmaschine bei $0 \, \text{mm}$ Durchmesser (Abstechen), wenn mit konstanter Schnittgeschwindigkeit gearbeitet wird?
17. Das dargestellte Wellenende soll mit einer Schnittgeschwindigkeit von $240 \, \text{m/min}$ durch Längsrunddrehen geschlichtet werden. Welche Umdrehungsfrequenzen sind bei den beiden Durchmessern zu wählen?

[ABBILDUNG: Skizze eines Wellenendes mit zwei Durchmessern ($\varnothing 36$ und $\varnothing 12$), Radien R3 und einer Fase 2x45°.]

18. Erstellen Sie mit einer Tabellenkalkulation ein Programm, mit dem Sie Schnittgeschwindigkeit und Umdrehungsfrequenz bestimmen können.
19. Mit einem Bohrer von $12 \, \text{mm}$ Durchmesser soll auf einer CNC-Drehmaschine bei einem Vorschub von $0,2 \, \text{mm}$ eine Schnittgeschwindigkeit von $20 \, \text{m/min}$ erzielt werden. Welche Vorschubgeschwindigkeit in mm/min ist zu programmieren?
20. Beim Drehen wird mit einer Vorschubgeschwindigkeit von $200 \, \text{mm/min}$ gearbeitet. Wie groß ist der Vorschub je Umdrehung, wenn mit einer Umdrehungsfrequenz von $800/\text{min}$ gedreht wird?
21. Eine Welle von $40 \, \text{mm}$ Durchmesser wird auf $30 \, \text{mm}$ Durchmesser längsrundgedreht. Welche Vorschubgeschwindigkeit ist nötig, damit bei einer Schnittgeschwindigkeit von $150 \, \text{m/min}$ ein Vorschub von $0,5 \, \text{mm}$ erzielt wird?
22. Wie groß muss die Antriebsleistung einer Drehmaschine sein, wenn ihr Wirkungsgrad $0,75$ ist, die Schnittgeschwindigkeit $200 \, \text{m/min}$ beträgt und die spezifische Schnittkraft $2500 \, \text{N/mm}^2$ bei einem Spanungsquerschnitt von $5 \, \text{mm}^2$ groß ist?
23. Eine Welle aus C60 wird von $\varnothing 60$ auf $\varnothing 52$ geschruppt. Der Vorschub beträgt $0,4 \, \text{mm}$, die Schnittgeschwindigkeit $240 \, \text{m/min}$ und der Einstellwinkel 90°.
a) Welche Umdrehungsfrequenz ist zu wählen?
b) Wie groß sind die Schnitttiefe und die Spanungsdicke?
c) Welcher Spanungsquerschnitt ergibt sich?
d) Welche Schnittleistung ist erforderlich?
e) Wie groß muss die Antriebsleistung des Motors bei einem Wirkungsgrad von $0,75$ sein?
24. An einer Drehmaschine steht eine Antriebsleistung von $40 \, \text{kW}$ zur Verfügung. Es soll eine Schnittgeschwindigkeit von $200 \, \text{m/min}$ bei $f = 1 \, \text{mm}$ und $a_p = 10 \, \text{mm}$ eingehalten werden. Die spezifische Schnittkraft beträgt $2000 \, \text{N/mm}^2$ und der Wirkungsgrad der Maschine ist $0,7$. Sind diese Schnittbedingungen zu realisieren?
25. Eine Trommel aus 34CrMo4 mit $550 \, \text{mm}$ Durchmesser wird mit einer Umdrehungsfrequenz von $50/\text{min}$ längsrundgedreht. Bei einer Spanungsdicke von $0,8 \, \text{mm}$ und einer Spanungsbreite von $10 \, \text{mm}$ beträgt die spezifische Schnittkraft $1733 \, \text{N/mm}^2$.
a) Wie groß ist der Spanungsquerschnitt?
b) Welche Schnittleistung wird gebraucht?
c) Welche Leistung muss der Antriebsmotor abgeben, wenn die Werkzeugmaschine einen Wirkungsgrad von $76\%$ hat?
26. Welche Antriebsleistung muss ein Bohrwerk bei einem Wirkungsgrad von $0,72$ haben, wenn maximal mit einem Bohrer von $40 \, \text{mm}$ Durchmesser bei einer Umdrehungsfrequenz von $800/\text{min}$ mit einer spezifischen Schnittkraft von $2000 \, \text{N/mm}^2$ und einem Vorschub von $0,3 \, \text{mm}$ gearbeitet wird?
27. Erstellen Sie mit einer Tabellenkalkulation ein Programm zur Berechnung der Schnittleistung beim Drehen und Bohren.
## 28. Ein Kegel hat eine Kegelverjüngung von $1:40$. Wie groß ist seine Neigung?
29. Ein genormter Kegelstift hat ein Kegelverhältnis von $1:50$.
a) Wie groß ist der große Durchmesser für einen Kegelstift mit den Maßen $8 \times 60$?
b) Wie groß ist der Einstellwinkel?
## 30. Wie groß sind die fehlenden Werte?

| | a) | b) | c) | d) | e) | f) | g) | h) | i) | j) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $C$ | $1:10$ | ? | ? | ? | $1:50$ | ? | ? | ? | ? | $1:0,7$ |
| $C/2$ | ? | ? | $1:80$ | ? | ? | ? | ? | ? | $1:100$ | ? |
| $D$ in mm | ? | ? | $100$ | $60$ | $85$ | $80$ | $150$ | ? | $55$ | $115$ |
| $d$ in mm | $30$ | $0$ | ? | ? | $62,5$ | $60$ | $120$ | $22,5$ | ? | $0$ |
| $L$ in mm | $200$ | $50$ | $200$ | $80$ | ? | $120$ | ? | $65$ | $220$ | ? |
| $\alpha/2$ in ° | ? | $45$ | ? | $5,71$ | ? | ? | $2,86$ | $30$ | ? | ? |