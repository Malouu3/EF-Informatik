# APIS

[Kapitel 1-4 und 7](https://zapier.com/learn/apis/)

APIs sind Application Programming Interface, zu deutsch Programmschnittstellen. Es ist ein Protokol des Servers, das Anfragen annehmen und absenden kann. Verglichen mit einer Rezeptionistin.

Eine API (Application Programming Interface) ist ein Satz von Befehlen, Funktionen, Protokollen und Objekten, die Programmierer verwenden können, um eine Software zu erstellen oder mit einem externen System zu interagieren. Sie stellt Entwicklern Standardbefehle für die Ausführung allgemeiner Operationen zur Verfügung, so dass Codes nicht von Grund auf neu geschrieben werden müssen.

Die API – auch Programmierstelle genannt- ermöglicht es demnach Anwendungen miteinander zu kommunizieren. Die API ist nicht die Datenbank oder gar der Server, sondern der Code, der die Zugangspunkte für den Server regelt und die Kommunikation ermöglicht.

Somit wird der Datenaustausch zwischen verschiedenen Systemen um ein Vielfaches beschleunigt und vereinfacht.

## HTTP
- "Hyer-Text Transfer Protocol"
- Protokoll für die Kommunikation zwischen Server und den Browsern.

Request-Response-Circle:  Der Client sendet dem Server eine Anfrage, etwas zu tun. Der Server wiederum sendet dem Client eine Antwort, die besagt, ob der Server die Anfrage des Clients ausführen konnte oder nicht.

**Um eine gültige Anfrage zu stellen, muss der Client vier Dinge angeben:**

1. **URL**
Uniform Resource Locator

URLs in HTTP sind eindeutige Adressen für Dinge (Webseiten, Bilder oder Videos). APIs erweitern diese Adressenidee weiter auf Dinge wie z.B. Produkte, Kunden oder Tweets. Auf diese Weise werden URLs zu einer einfachen Möglichkeit für den Client, dem Server mitzuteilen, mit welcher Sache er interagieren möchte. APIs nennen sie natürlich auch nicht „Dinge“, sondern geben ihnen den technischen Namen „Ressourcen“.

2. **Methoden**
Die Request-methode übermittelt dem Server, welche Aktion der Client vom Server ausgeführt haben will. Die Verfahren werden allgemein als Request-Verben bezeichnet.

Die vier häufigsten APIs:

- **GET**:    Fordert den Server auf, eine Ressource abzurufen
- **POST**:   Fordert den Server auf, eine neue Ressource zu erstellen
- **PUT**:    Fordert den Server auf, eine vorhandene Ressource zu bearbeiten/aktualisieren
- **DELETE**: Fordert den Server auf, eine Ressource zu löschen


3. **Headers**

Headers stellen zu einer Request die Metainformation (Überschrift) dazu.

4. **Body**

Der Requesttext enthält die Daten, die der Client an den Server senden möchte.

Ein einzigartiges Merkmal des Körpers ist, dass der Client die vollständige Kontrolle über diesen Teil der Anfrage hat. Im Gegensatz zu Methoden, URLs oder Headern, bei denen das HTTP-Protokoll eine starre Struktur erfordert, ermöglicht der Text dem Client, alles zu senden, was er möchte.

### Statuscode
Statuscodes sind dreistellige Zahlen, die jeweils eine eindeutige Bedeutung haben. Bei korrekter Verwendung in einer API kann diese kleine Zahl viele Informationen an den Client übermitteln. Zum Beispiel haben Sie vielleicht diese Seite während Ihrer Internet-Streifzüge gesehen:

**NOT Foumd** ERROR 404

## JSON Format
Ein Computer muss die Daten in ein Format bringen, das der andere versteht. Im Allgemeinen bedeutet dies eine Art Textformat. Die gängigsten Formate in modernen APIs sind JSON (JavaScript Object Notation) und XML (Extensible Markup Language).


## XML Format


## Headers / Autorisierungs-HTTP-Header


## Endpunkt
