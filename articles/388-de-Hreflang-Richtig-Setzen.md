# Hreflang Richtig Setzen? Verlass dich bei mehrsprachigen Websites nicht nur auf automatische Erkennung

> Sprache: Deutsch | Region: DACH/Global | Keywords: hreflang setzen, hreflang tag, mehrsprachiges SEO, internationales SEO, x-default, canonical, technisches SEO

**Keywords**: hreflang setzen, hreflang tag, mehrsprachiges SEO, internationales SEO, multi-region SEO, x-default, canonical, technisches SEO, Sprachversionen, Länderversionen, Alternate Pages, Google International SEO, lokalisierte Seiten

---

## Warum ranken viele mehrsprachige Websites trotzdem mit der falschen Sprach- oder Länderversion?

Das sieht man ständig.

Die Website hat Englisch, Japanisch, Deutsch und Französisch. Alles ist online. Trotzdem passiert in der Suche oft Folgendes:

- Nutzer aus Japan landen auf der englischen Seite
- Nutzer aus Großbritannien landen auf der US-Version
- Nutzer aus Brasilien landen auf einer generischen portugiesischen Seite
- Statt der lokalen Version erscheint die globale Startseite

Dann beginnt die Fehlersuche:

- Liegt es an der Übersetzung?
- Hat die lokale Seite zu wenig Autorität?
- Fehlt noch mehr Inhalt?
- Sollten wir härter per IP weiterleiten?

Manchmal spielen diese Dinge eine Rolle. Sehr oft liegt das eigentliche Problem aber viel tiefer:

**hreflang wurde nicht sauber umgesetzt.**

Google versteht nicht automatisch, dass Seiten in verschiedenen Verzeichnissen dieselbe inhaltliche Version für unterschiedliche Sprachen oder Regionen sind.

Wenn du diese Beziehung nicht klar markierst, muss Google raten.

Und im SEO ist Raten fast nie die beste Strategie.

---

## Was macht hreflang eigentlich?

Hreflang ist kein Ranking-Booster. Es ist eher ein Hinweis für Sprache und Region.

Du sagst der Suchmaschine damit:

> Diese Seiten gehören zusammen, sind aber für unterschiedliche Sprachen oder Märkte gedacht.

Richtig eingesetzt hilft hreflang vor allem bei drei Dingen:

1. Es erklärt die Beziehung zwischen Versionen
2. Es erhöht die Chance, dass Nutzer auf der passenden lokalen Seite landen
3. Es reduziert das Problem „falsche Seite im falschen Markt“

Wenn du dich fragst **wie man hreflang richtig setzt**, dann ist der Kernpunkt dieser:

**Nicht das Tag selbst ist schwer, sondern die saubere Zuordnung der richtigen Seiten, der richtigen Codes und der restlichen SEO-Signale.**

---

## Hreflang richtig setzen: Diese 5 Fälle solltest du getrennt betrachten

### 1. Gleicher Inhalt in mehreren Sprachen: Immer Seite zu Seite zuordnen

Nur die Startseite zu markieren reicht nicht.

Wenn dieselbe Produktseite auf Englisch, Deutsch, Japanisch und Französisch existiert, sollte jede Version die anderen als Alternativen referenzieren.

Typische Fehler:

- hreflang nur auf der Homepage
- eine Seite verweist auf eine andere, bekommt aber keinen Rückverweis
- man glaubt, „mehrsprachig“ sei schon genug

Ist es nicht.

### 2. Gleiche Sprache, aber unterschiedliche Länder: Region sauber trennen

Hier wird es bei vielen internationalen Websites unsauber.

Beispiele:

- `en-us`
- `en-gb`
- `en-au`
- `pt-br`
- `pt-pt`

Die Sprache ist ähnlich, aber Preise, Währung, Schreibweise, Versand oder Angebote unterscheiden sich.

Wenn alles nur als `en` oder `pt` markiert wird, ist das Signal oft zu grob.

Nutzer brauchen nicht nur die richtige Sprache, sondern oft auch die richtige Marktversion.

### 3. Globale Einstiegsseite oder Länderauswahl? Dann `x-default` nutzen

Viele internationale Seiten haben:

- eine Sprachwahl
- eine Länderauswahl
- eine globale Startseite
- eine neutrale Landingpage ohne klares Zielgebiet

Für solche Fälle ist `x-default` gedacht.

Damit sagst du Google, welche Seite als Standard dienen soll, wenn keine bessere Sprach- oder Regionszuordnung greift.

### 4. Nur echte Entsprechungen miteinander verknüpfen

Ein klassischer hreflang-Fehler ist zu viel Verlinkung.

Dann passiert so etwas:

- jede englische Seite zeigt auf jede japanische Seite
- Kategorien zeigen auf Produktseiten in anderen Ländern
- gelöschte Seiten bleiben im hreflang-Set
- Hilfeseiten zeigen auf die Homepage, nur weil die Sprache gleich ist

Das schafft keine Klarheit, sondern Rauschen.

Die sichere Regel lautet:

**Nur Seiten mit demselben Thema, derselben Funktion und derselben Ebene sollten als Alternativen verbunden werden.**

### 5. Canonical, noindex und Redirects immer zusammen mit hreflang prüfen

Hier scheitern viele Setups still im Hintergrund.

Typische Konflikte:

- hreflang ist gesetzt, aber canonical zeigt auf die globale Version
- die URL ist im hreflang-Set, leitet aber weiter
- eine Regionalseite ist noindex, taucht aber weiter im Set auf
- automatische Weiterleitungen machen die Seite für Crawler instabil

Wenn eine Seite wirklich als eigenständige Sprach- oder Länderversion existieren soll, muss sie erreichbar, indexierbar und stabil sein.

---

## Die 4 häufigsten hreflang-Fehler

### 1. Nur einseitige Verweise
A zeigt auf B, aber B nicht zurück.

### 2. Falsche Codes
Sprach- und Ländercodes werden verwechselt oder falsch formatiert.

### 3. Zu aggressive IP-Weiterleitungen
Nutzer und Crawler sehen die Originalseite kaum noch.

### 4. Schlechte Ziel-URLs
hreflang verweist auf 404-Seiten, Redirect-Ketten, Testseiten oder Parameter-URLs.

---

## Kurze Prüfliste für hreflang

### Schritt 1: Nur echte Entsprechungen sammeln
Starte mit Startseite, wichtigen Produktseiten, zentralen Kategorien und starkem Content.

### Schritt 2: Rückverweise prüfen
Wenn Seite A auf B verweist, muss B auch auf A verweisen.

### Schritt 3: Codes und finale URLs validieren
Sprache, Region und endgültige Ziel-URL prüfen.

### Schritt 4: Canonical, noindex und Redirects mitprüfen
hreflang niemals isoliert betrachten.

### Schritt 5: Suchergebnisse nach dem Rollout beobachten
Wenn weiterhin die falsche Marktversion erscheint, stimmt das Mapping noch nicht.

---

## Fazit

Hreflang ist nicht schwierig, weil das Markup kompliziert wäre. Schwierig ist die saubere inhaltliche Zuordnung.

Wenn diese Beziehungen klar sind, ist hreflang sehr nützlich.
Wenn sie unklar sind, verwirrst du die Suchmaschine nur noch mehr.

**Lass Google deine Sprach- und Länderversionen nicht erraten. Wenn du sie klar kennzeichnen kannst, dann kennzeichne sie klar.**

---

**Verwandte Suchanfragen**: hreflang setzen, hreflang tag, mehrsprachiges SEO, internationales SEO, multi-region SEO, x-default, canonical, technisches SEO
