(This is the source for the website Wrocław Municipal Police Open Data. Please scroll down for [English version](#wroclaw-municipal-police-open-data))
# Publiczny Rejestr Danych Straży Miejskiej Wrocław

Otwarte dane [LINK](https://project-open-data.cio.gov/principles/), [LINK](http://www.opendatapolicies.org/browse/), [LINK](https://sunlightfoundation.com/2015/10/01/why-should-cities-have-an-open-data-policy/), [LINK](https://www.youtube.com/watch?v=ObrlsMA7c3M) są strategicznym zasobem instytucji publicznych i obywateli. Chcemy włączyć się do dyskusji na temat potrzeby istnienia Straży Miejskiej Wrocławia. Trudno dyskutować na ten temat nie posiadając informacji o tym jak Straż Miejska Wrocławia realizuje swoje. Dane te do tej pory były niedostępne dla obywateli. Nasza praca ma za zadanie udostępnić te dane zgodnie z ideą "otwartych danych".

Podobny zbiór danych znajduje się [tutaj](https://data.cambridgema.gov/Traffic-Parking-and-Transportation/Cambridge-Parking-Tickets/vnxa-cuyr) - jest to zbiór mandatów dla amerykańskiego miasta Cambridge, MA.

1. [Jak Straż Miejska Wrocławia tworzy swoje dane](#jak-stra%C5%BCmiejska-wroc%C5%82awia-tworzy-swoje-dane)
1. [Nieprzetworzone zbiory danych](#nieprzetworzone-zbiory-danych)
1. [Plany na przyszłość](#plany-na-przysz%C5%82o%C5%9B%C4%87)
1. [Regulamin używania](#regulamin-u%C5%BCywania-udost%C4%99pnianych-tutaj-danych)

## Wiki

[Wiki](https://github.com/SigmaNgo/SMW/wiki) zawiera m.in. instrukcje jak przetwarzane są dane.

## Jak Straż Miejska Wrocławia tworzy swoje dane

Aby zrozumieć jakie dane są w udostępnionych tutaj danych, najpierw należy sięgnąć do informacji jak są one tworzone. Informacje te nie są dostępne w Biletunie Informacji Publicznej Straży Miejskiej Wrocławia więc zostały udostępnione na wniosek.

|Wniosek        |Odpowiedź Straży Miejskiej Wrocławia |
| ------------- | ------------- |
|[Wniosek z pytaniami o rejestr zgłoszeń](requestForData/wniosek_rejestr_zgloszen.txt "z dnia 19 kwietnia 2018")|[Odpowiedź](requestForData/odpowiedz_rejestr_zgloszen.gif "z dnia 27 kwietnia 2018")|
|[Wniosek z pytaniami o SUMPRO](requestForData/wniosek_sumpro.txt "z dnia 28 kwietnia 2018")|[Odpowiedź](requestForData/odpowiedz_sumpro.gif "z dnia 11 maja 2018")|
|[Wniosek z pytaniami o rejestr mandatów](requestForData/wniosek_rejestr_mandatow.txt "z dnia 15 maja 2018")|[Odpowiedź](requestForData/odpowiedz_rejestr_mandatow.gif "z dnia 25 maja 2018")|

Z informacji tych można dowiedzieć się między innymi jak numerowane są zgłoszenia w udostępnionych danych.

Należy także rozróżnić interwencje od zgłoszeń. Każde zgłoszenie do Straży Miejskiej Wrocławia, np. przez obywatela Wrocławia, skutkuje interwencją (i te właśnie zgłoszenia są udostępnione w [poniższym zbiorze "Rejestr zgłoszeń"](#rejestr-zg%C5%82osze%C5%84)), natomiast nie każda interwencja SWM pochodzi ze zgłoszenia (np. Straż Miejska Wrocławia realizuje zadania zlecone w inny sposób niż przez zgłoszenia od obywateli). Co oczywiste, nie każda interwencja skutkuje mandatem.

Należy także wziąć po uwagę rozróżnienie pomiędzy rejestrem zgłoszeń a rejestrem mandatów oraz że nie wszystkie interwencje znajdują się w udostępnionym poniżej zbiorze.

## Nieprzetworzone zbiory danych

### Rejestr zgłoszeń

[LINK](./rawData/rawData.md) do danych tak jak zostały one udostępnione przez Straż Miejską Wrocławia (czyli bez jakiejkolwiek obróbki *).

_* z niestotnego tutaj powodu pliki .doc nie są dobrze obsługiwane przez skrypt tworzący z udostępnionych danych plkiki csv; tak więc dane które zostały nam udostępnione w formacie .doc zostały zmienione na format .docx; można przyjąć że są to wciąż dane nie dotknięte obróbką_

### Rejestr mandatów

[na razie pusty]

## Przetworzone zbiory danych

### Rejestr zgłoszeń

[LINK](./transformedData/transformedData.md) do przetworzonych przez nas danych. Aby sprawdzić na czym polega przetworzenie sprawdź [Wiki](https://github.com/SigmaNgo/SMW/wiki).

### Rejestr mandatów

[na razie pusty]

## Plany na przyszłość

Chcemy aby we Wrocławiu powstał portal z otwartymi danymi na wzór [tego które ma miasto Cambridge, MA](http://www.cambridgema.gov/departments/opendata). Chcielibyśmy użyć narzędzia typu https://dev.socrata.com/. Dane na temat Straży Miejskiej Wrocławia miałyby być pierwszą cegiełką budującą ten portal. Z kolei to narzędzie http://messytables.readthedocs.io ma zostać wykorzystane do porządkowania udostępnionych nam danych.

## Regulamin używania

1. Bądź odpowiedzialny.
1. Kod w tym repozytorium jest udostępniony pod licencją [LINK](/LICENSE.md).
1. [Nieprzetworzone dane](./rawData/rawData.md) zmieszczone w tym repozytorium stanowią informację publiczną w rozumieniu ustawy z dnia 6 września 2001 r. o dostępie do informacji publicznej (Dz.U. Nr 112, poz. 1198, z późn. zm.). Dane te zostały udostępnione na wniosek.
1. [Przetworzone dane](./transformedData/transformedData.md) zmieszczone w tym repozytorium stanowią informację publiczną w rozumieniu ustawy z dnia 6 września 2001 r. o dostępie do informacji publicznej (Dz.U. Nr 112, poz. 1198, z późn. zm.). Dane te zostały udostępnione na wniosek.
1. Dla wszystkich zbiorów danych w tym repozytorium zastosowanie mają następujące zastrzeżenia:
* w przypadku wykorzystania danych zmieszczonych w tym repozytorium należy dodać przypis informujący o źródle pochodzenia;
* korzystanie z informacji udostępnionej tutaj następuje na własną odpowiedzialność;
* w żadnym z wypadków Zarządzający, Właściciel, ani żadna Organizacja udostępniająca dane nie ponosi odpowiedzialności za ewentualną szkodę wynikającą z ponownego wykorzystania informacji publicznej przez korzystającego lub innych użytkowników;
* zastrzega się, że zamieszczonye tu informacje mogą być nieaktualne lub zawierać błędy.

# Widzisz błąd?

Koniecznie zgłoś go [tutaj](https://github.com/SigmaNgo/SMW/issues).

# Wroclaw Municipal Police Open Data
This is the source for the website Wrocław Municipal Police Open Data. We are seeking volunteer who would translate it to English, feel invited to apply!
