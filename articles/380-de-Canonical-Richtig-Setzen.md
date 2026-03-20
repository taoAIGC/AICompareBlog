# Wie setze ich das Canonical-Tag? Hören Sie auf, dass mehrere Seiten auf die Startseite verweisen, diese 5 Situationen werden effektiver gehandhabt

> Sprache: Chinesisch | Region: China/Global | Schlüsselwörter: Einrichten kanonischer Tags, kanonische Tags, Verwendung kanonischer Tags, kanonische Tags, SEO für doppelte Seiten, Optimierung der Seiteneinbindung, Website-Index, technisches SEO

**Schlüsselwörter**: So richten Sie kanonische Tags ein, kanonische Tags, wie Sie kanonische Tags verwenden, kanonische Tags, SEO für doppelte Seiten, Optimierung der Seiteneinbindung, Website-Indexierung, technisches SEO, Verarbeitung doppelter Inhalte, URL-Normalisierung, Einschlussprobleme, Search Console

---

## Warum verweisen viele Websites kanonisch zuerst auf die Startseite, wenn es ein Einbindungsproblem gibt?

Ich habe diese Falle zu oft gesehen.

Der Webmaster war etwas besorgt, weil die Seite nicht enthalten war, also öffnete er das Backend und nahm einige Änderungen vor, und schließlich wurde daraus:

- Die Artikelseite verweist auf die Homepage
- Die Kategorieseite verweist auf die Startseite
- Die Parameterseite verweist auf die Startseite
- Auch Produktseiten verweisen auf die Homepage

Oberflächlich betrachtet scheint es, als würde es „die Gewichte vereinheitlichen“.

Der tatsächliche Effekt ist jedoch oft: **Suchmaschinen werden immer verwirrter darüber, welche Seite Sie als Hauptseite betrachten möchten. **

Der Tag „canonical“ wurde ursprünglich verwendet, um Suchmaschinen Folgendes mitzuteilen:

**„Der Inhalt dieser Seiten ist sehr ähnlich. Bitte betrachten Sie diese Seite zunächst als offizielle Version.“**

Es handelt sich weder um eine universelle Reparaturschaltfläche noch um ein Tool, das der Homepage die Schuld gibt, wenn es ein Problem mit der Seite gibt.

Wenn Sie sich also kürzlich mit der Einrichtung kanonischer Tags beschäftigen, möchte ich Ihnen zunächst die Schlussfolgerung geben:

**kanonisch Was ich am meisten fürchte, ist nicht, nicht schreiben zu können, sondern wahllos zu schreiben. **

---

## Was genau macht Canonical? Verwechseln Sie es nicht mit 301 oder noindex.

Wenn viele Menschen zum ersten Mal mit Canonical in Kontakt kommen, werden sie höchstwahrscheinlich mit diesen beiden Dingen verwechselt:

- **301-Weiterleitung**
- **kein Index**

Sie sind nicht dasselbe.

### 1.kanonisch
bedeutet:
**Diese Seite ist barrierefrei, aber ich möchte lieber, dass Sie die andere Seite als Masterversion betrachten. **

### 2. 301 Weiterleitung
bedeutet:
**Diese Seite ist umgezogen, Sie können direkt zur neuen Adresse gehen. **

### 3. noindex
bedeutet:
**Sie können diese Seite crawlen, aber nicht in den Index aufnehmen. **

Kanonisch bedeutet also weder „Löschen der Seite“ noch „Zwang, zur Seite zu springen“.

Es handelt sich eher um eine „Archivnotiz“.

Sie sagen Suchmaschinen:

> Der Inhalt dieser Seiten ist nahezu identisch. Die Hauptversion, die gesammelt werden sollte, ist diese Seite.

Wenn Sie diese Prämisse nicht einmal verstehen, wird sie später leicht verwirrender.

---

## Wie lege ich das kanonische Label fest? Ich empfehle, sich zunächst diese 5 häufigen Szenarien anzusehen

### 1. Die gleiche Seite hat nur unterschiedliche Parameter. Dies ist am besten zum kanonischen Hinzufügen geeignet.

Dies ist die häufigste und üblichste Verwendung.

Beispielsweise können diese Adressen aufgrund statistischer Parameter, Werbeparameter und Freigabeparameter auf derselben Seite erscheinen:

- `/seo-tools`
- `/seo-tools?utm_source=x`
- `/seo-tools?from=twitter`
- `/seo-tools?session=123`

Der Inhalt, den Benutzer sehen, ist fast derselbe, nur die URL ist unterschiedlich.

Der derzeit stabilste Ansatz ist normalerweise:

**Alle Parameterseiten kehren kanonisch zur Haupt-URL zurück. **

Das heißt, einheitliches Zeigen:

`/seo-tools`

In diesem Fall ist es für Suchmaschinen einfacher zu verstehen und verursacht am wenigsten Probleme.

---

### 2. Die Sortierseite, die Filterseite und die ursprüngliche Listenseite wiederholen sich stark. Sie können eine kanonische Rückkehr zur Hauptlistenseite in Betracht ziehen.

E-Commerce-Sites, Tool-Katalog-Sites und Content-Sites verfügen häufig über Seiten wie diese:

- Nach Preis sortieren
- Nach Neuestem sortieren
- Nach Farbe filtern
- Nach Region filtern

Das Problem ist:
Einige Filterseiten bringen tatsächlich keinen neuen Suchwert, sondern ändern lediglich die Anzeigereihenfolge desselben Inhalts.

Zum Beispiel:

- `/plugins`
- `/plugins?sort=latest`
- `/plugins?sort=popular`

Wenn der Kerninhalt der Seiten ähnlich ist und es keinen offensichtlichen Unterschied im Suchwert gibt, können Sie erwägen, die Sortierseite zur Hauptlistenseite zu kanonisieren.

Aber hier ist etwas zu beachten:

**Nicht alle Filterseiten sollten wieder kanonisiert werden. **

Wenn eine Filterseite selbst klare Suchanforderungen hat, wie zum Beispiel „SEO-Plug-ins für unabhängige Websites geeignet“ oder „kostenlose KI-Plug-ins“, kann es sich lohnen, separat zu existieren, anstatt sie zusammenzuführen.

Machen Sie es also nicht mechanisch. Überprüfen Sie zunächst, ob diese Seite einen unabhängigen Wert hat.

---

### 3. Wenn es mehrere URLs für denselben Inhalt gibt, muss nur eine Hauptversion explizit beibehalten werden.

Dieses Problem tritt besonders häufig bei Blogs, CMS und Revisionsseiten auf.

Beispielsweise kann derselbe Artikel gleichzeitig erscheinen in:

- neuer Link
- Alter Link
- Links mit Kategoriepfaden
- Links ohne Kategoriepfad
- Zwei Versionen mit und ohne Schrägstriche

Der Inhalt besteht eindeutig aus einem Artikel, es gibt jedoch mehrere URLs.

Geschieht dies nicht, muss die Suchmaschine raten:
Welche ist die offizielle Seite?

Das Wichtigste, was Sie tun sollten, ist, zunächst eine URL auszuwählen, die Sie wirklich lange behalten möchten, und dann:

- Geben Sie Ihr Bestes, um 301 zu erreichen, wenn Sie 301 können
- Es kann vorerst nicht gesprungen werden, zumindest ist Canonical mit der Hauptversion vereinheitlicht.

Verwenden Sie A nicht heute, B morgen und C ein paar Wochen später.

**Kanonisch Diese Art von Dingen hat am meisten Angst vor der eigenen Instabilität. **

---

### 4. Ähnliche Produktseiten und ähnliche Landingpages sollten nicht zu einer zusammengefasst werden, nur weil sie „ähnlich“ sind.

Es gibt viele Fallstricke.

Sie haben zum Beispiel diese Seiten:

- schwarze Laufschuhe
- weiße Laufschuhe
- Laufschuhe für Damen
- Breite Laufschuhe

Da sie sich alle sehr ähnlich sahen, ging jemand direkt auf die „Laufschuh-Homepage“ von Canonical.

Das Ergebnis ist:
Die Seite, die die unterteilten Suchbegriffe separat hätte abdecken können, wurde von Ihnen selbst unterdrückt.

Meine eigenen Beurteilungskriterien sind einfach:

**Wenn Benutzer beim Durchsuchen dieser Seite erwarten, unterschiedliche Inhalte, unterschiedliche Informationen und unterschiedliche Kaufentscheidungen zu sehen, verwechseln Sie das nicht. **

Canonical ist nur dann geeigneter, wenn sich diese Seiten wirklich nur geringfügig wiederholen, der Hauptinhalt nahezu gleich ist und der unabhängige Wert schwach ist.

Ansonsten standardisieren Sie nicht, sondern sperren aktiv Einfahrten in den Longtail-Verkehr ab.

---

### 5. Die Seite wurde aktualisiert und die alte Seite wird nicht mehr beibehalten. Verwenden Sie 301; Verwenden Sie kein kanonisches Hardtop.

Es gibt eine Situation, in der es am wahrscheinlichsten ist, dass es falsch verwendet wird:

Die alte Seite ist veraltet und wurde durch die neue Seite vollständig ersetzt.

Zu diesem Zeitpunkt sind viele Leute zu faul, um einen Sprung zu machen, also fügen sie der alten Seite einen Canonical hinzu, um auf die neue Seite zu verweisen, und denken, es sei „fast“.

Nicht genau das Gleiche.

Wenn keine Notwendigkeit besteht, die alte Seite beizubehalten, und Sie möchten, dass Benutzer beim Besuch der alten Seite direkt auf die neue Seite gelangen, ist es in der Regel sinnvoller:

**301-Weiterleitung statt nur kanonisches Schreiben. **

Da Canonical davon ausgeht, dass die alte Seite noch existiert, teilt es der Suchmaschine einfach mit: „Bitte konzentrieren Sie sich auf diese Seite.“

Und 301 bringt deutlich zum Ausdruck:

**Diese Seite wurde offiziell verschoben. **

Viele Menschen achten im Normalfall nicht auf diesen Unterschied, aber es wird ihnen sehr peinlich sein, wenn sie später den Index und das Gewicht überprüfen.

---

## Ich denke, diese vier kanonischen Fehler sind schädlicher als nicht zu schreiben.

### Fehler 1: Alle Seiten verweisen auf die Homepage

Dies ist die häufigste Form grober Behandlung.

Das Problem besteht darin, dass die Startseite, die Artikelseiten, die Produktseiten und die Kategorieseiten ursprünglich nicht der Suchabsicht dienen.

Wenn Sie eine Reihe von Seiten auf die Startseite verweisen, teilen Sie den Suchmaschinen Folgendes mit:

„Keine dieser Seiten ist wichtig, wichtig ist die Homepage.“

Seien Sie nicht allzu überrascht, wenn viele Long-Tail-Wörter nicht verwendet werden können.

---

### Fehler 2: Der Inhalt der Seite ist sehr unterschiedlich, aber es wird immer noch derselbe Kanon geschrieben

Canonical ist nicht dazu gedacht, „völlig unterschiedliche Themen“ zusammenzuführen.

Wenn die Themen, Benutzerabsichten und Keyword-Richtungen der beiden Seiten alle unterschiedlich sind, aber nur geringfügig miteinander verbunden sind, sollten Sie sie nicht willkürlich verweisen.

Die Suchmaschine erkennt nicht nur, dass Sie kanonisch geschrieben haben und folgt ihm einfach, sondern beurteilt auch selbst die Ähnlichkeit des Inhalts.

Wenn Sie wahllos schreiben, wird es oft nicht das tun, was Sie meinen.

---

### Fehler 3: Canonical verweist auf 404, Sprungseiten oder sogar nicht indizierte Seiten

Dies ist eine kleine Gefahr, die in der Technologie am leichtesten übersehen wird.

Die Zielseite, auf die Canonical verweist, sollte vorzugsweise diese Bedingungen erfüllen:

- Kann normal geöffnet werden
- Statuscode ist normal
- Nicht 404
- Nicht die Adresse nach mehrstufigen Sprüngen
- nicht noindexed

Andernfalls geben Sie der Suchmaschine eine sehr vage oder sogar falsche Anweisung.

---

### Fehler 4: Kanonisch auf der einen Seite und entgegengesetzte Signale auf der anderen Seite geben.

Zum Beispiel:

- Die Seite schreibt ihre eigene kanonische Selbstreferenz
- In der Sitemap wurde eine andere URL übermittelt
- Die meisten internen Links verweisen auf die dritte URL
- Hreflang, Redirect, Canonical bekämpfen sich gegenseitig

Diese Situation ist die problematischste.

Denn was die Suchmaschine am Ende erhält, ist kein klares Fazit, sondern ein Haufen widersprüchlicher Tipps.

**Wirklich effektiv ist kanonisch, nicht einen einzigen Punkt richtig zu schreiben, sondern sich nicht gegenseitig im gesamten Satz von URL-Signalen zu untergraben. **

---

## Wenn Sie jetzt Canonical überprüfen möchten, reicht diese Liste aus

Wenn ich meine eigene Fehlerbehebung durchführe, schaue ich normalerweise in dieser Reihenfolge:

### Schritt eins: Hat diese Seite einen unabhängigen Suchwert?
Wenn ja, übertragen Sie es nicht einfach auf eine andere Seite.

### Schritt 2: Ist diese Seite der Zielseite sehr ähnlich?
Wenn sie einigermaßen ähnlich sind, aber tatsächlich unterschiedliche Probleme lösen, sollten Sie sie nicht zusammenführen.

### Schritt 3: Ist die Zielseite stabil, zugänglich und einbindungsfähig?
Verweisen Sie nicht auf 404-Fehler, Weiterleitungslinks oder Noindex-Seiten.

### Schritt 4: Sind andere Signale auf der Website konsistent?
Überprüfen Sie die Sitemap, interne Links, Navigation und Weiterleitungen, um festzustellen, ob Konflikte vorliegen.

### Schritt 5: Kanonische Szenarien, schreiben Sie nicht nur kanonische
Die alte Seite wurde eingestellt, also lassen Sie sie nicht halb tot.

Wenn man diese 5 Schritte betrachtet, können die meisten kanonischen Probleme tatsächlich lokalisiert werden.

---

## Mein jetzt üblicherer Ansatz: Zuerst die URL-Beziehung klären und dann über kanonisch sprechen

Ehrlich gesagt haben viele Websites kanonische Probleme, nicht weil die Tags selbst schwierig sind, sondern weil die URL-Struktur nicht von Anfang an klar durchdacht wurde.

Zum Beispiel:

- Derselbe Inhalt kann drei oder vier Arten von Links generieren
- Kategoriepfade ändern sich häufig
- Koexistenz alter und neuer URLs
- Parameterregeln sind verwirrend
- Vorlagen und Plug-Ins generieren automatisch eine Reihe doppelter Seiten

Selbst wenn Sie Canonical auf jeder Seite dieser Art von Website patchen, werden Sie es später einfach weiter patchen.

Jetzt mache ich das lieber zuerst:

**Überlegen Sie zunächst klar, welche Seiten vorhanden sein sollten, welche nicht vorhanden sein sollten und welche Seiten zusammengeführt werden sollten. **

Nach einer klaren Überlegung wird sich Canonical zu einem sehr praktischen Organisationstool entwickeln.

Ansonsten kann es problemlos als Feuerlöschgerät verwendet werden.

---

## Schreiben Sie am Ende

Wie man die kanonische Bezeichnung festlegt, ist tatsächlich nicht so mysteriös wie gedacht.

Die Schwierigkeit besteht nicht darin, wie man den Code schreibt, sondern ob man ihn zuerst klar beurteilen kann:

- Welche Seiten sind wirklich Duplikate?
- Welche Seiten sind einfach ähnlich, sollten aber beibehalten werden?
- Welche Seiten sollten kanonisch sein?
- Welche Seiten sollten eigentlich 301 sein

Ich habe jetzt immer mehr das Gefühl, dass der Kernwert von Canonical nicht die „Gewichtsübertragung“ ist, sondern:

**Lassen Sie Suchmaschinen klarer erkennen, welche Seite Ihrer Website die offizielle Version ist. **

Solange diese Idee klar ist, werden viele Probleme wie langsame Sammlung, doppelte Seiten und chaotische Indizierung viel einfacher zu bewältigen sein als zuvor.

Wenn Sie kürzlich nach einer Aufnahme suchen, prüfen Sie nicht nur, ob Canonical sie geschrieben hat.

Was mehr ist:

**Ist es auf der richtigen Seite geschrieben? **

---

**Verwandte Suchanfragen**: So richten Sie kanonische Tags ein, kanonische Tags, wie Sie kanonische Tags verwenden, kanonische Tags, SEO für doppelte Seiten, Optimierung der Seiteneinbindung, Website-Indexierung, technische SEO, Verarbeitung doppelter Inhalte, URL-Normalisierung, Einschlussprobleme, Suchkonsole
