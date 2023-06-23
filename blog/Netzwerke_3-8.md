# Kapitel 3:  Vom LAN zum Internet



# Kapitel 4:  IP-Adressen

## Adresseaufbau:

Beispiel:
````131.23.10.168````

- 4 Zahlen, je ein Byte => 32 Bit
- dizimaler Schreibweise
- durch Punkte getrennt
- Wert zwischen 0 und 255

## Netzwerkteil und Hostteil
**Netzwerkteil:**
  **Vorderer** Teil der Adresse. Ist für alle Geräte im selben Netzwerk gleich => Grundadresse aller Geräte im Netzwerk

**Hostteil:
  Hinterer** Teil der Adresse. Für jeden Host (eng. Gerät) unterschiedlich. Keine zwei Geräte eines Netz dürfen den gleichen Hostteil haben.
  
## Netzmaske

Wo der Netzwerkteil endet und Hostteil beginnt, erkennt man nicht auf den ersten Blick. Man braucht ihre binäre Form, sowie die Netzmaske, auch Subnetzmaske genannt.

__Dezimale__ Schreibweise:
`255.255.255.0`
__binäre__ Form:
`1111'1111.1111'1111.1111'1111.0000'0000`

Auf der linken Seite sind nur Einsen, auf der rechten nur Nullen. Die Wechselstelle kann mitten in einem Byte liegen, muss also nicht in der Mitte liegen.


Netzmaske wird auf die IP-Adresse angewendet in der binären Form. Die __1en__ der Netzmasek markiert die Bits der IP-Adresse als __Netzwerkteil__. Die __0en__ markieren den __Hostteil__.

```
Netzmaske:  255.255.254.0
IP-Adresse: 13.162.25.4

Binär:
Netzmaske:    1111 1111.1111 1111.1111 1110.0000 0000
IP-Adresse:   0000 1101.1010 0010.0001 1001.0000 0100
#             vvvv vvvv vvvv vvvv vvvv vvv
Netzwerkteil: 0000 1101.1010 0010.0001 100
#                                         v vvvv vvvv
Hostteil:                                 1.0000 0100
```

__Netzwerkadesse__: Netzwerkteil mit 0en auf 32 Bit langen IP-Adresse auffüllen. Wird gebraucht, wenn mehrere Netzwerke miteinander über __Router__ verbunden werden. Der Router verteilt seinen Host die Netzmaske. => Netzwerkteil aller Geräte im Netz sind gleich.

### Suffixnotation für Netzmaske

IP-Adresse interpretieren:

  - muss nicht die ganze Netzmaske aufschreiben.
  - Muss nur die Anzahl an 1sen wissen
  - Anzahl kann als __Suffix__ an einer IP-Adresse angehängt

Beispiel IP-Adresse mit Suffix:
`13.162.25.4/23`


## Broadcastadresse



## Spezielle IP-Adressen

- __127.0.0.1__:
 __"Loopback-Adresse"__. Wenn ein Gerät ein Paket an _sich selber_ senden will.


## ***Fragen***

- [ ] 
