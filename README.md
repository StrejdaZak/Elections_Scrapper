# Skript pro Analýzu a Generování CSV s Výsledky Voleb

## Tento skript je určen k analýze a generování CSV s výsledky voleb. 
Skript získává data ze zadaného územního celku, zpracovává je a ukládá výsledná data do CSV souboru. Následující návod vám ukáže, jak tento skript používat a jak správně zobrazit výsledky v programu Microsoft Excel.

### 1. Instalace potřebných knihoven
Před spuštěním skriptu se ujistěte, že máte nainstalované potřebné knihovny. Pro instalaci knihoven použijte následující příkaz:

**pip install -r requirements.txt**

### 2. Použití skriptu
Pro spuštění skriptu použijte následující příkaz ve svém terminálu:

**python projekt_3.py "Odkaz" VystupniSoubor.csv**
*Odkaz:* Odkaz na stránku s výsledky voleb pro konkrétní územní celek. Nezapomeňte ho vložit do uvozovek
*VystupniSoubor.csv:* Název výstupního CSV souboru, kam budou uložena data.

### 3. Příklad použití
Zde je příklad, jak použít skript s konkrétním odkazem na výsledky voleb v územním celku Cheb:

**python projekt_3.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=5&xnumnuts=4101" VysledkyCheb.csv**

Výsledná tabulka pak bude vypadat následovně: 

| Kody | Obce | Voliči v seznamu | Vydané obálky |
|----------|----------|----------|----------|
| 554499   | Aš   | 9766   | 4289   |

### 4. Otevření CSV souboru v Excelu: 
Po vygenerování CSV souboru postupujte následovně, abyste jej správně zobrazili v programu Microsoft Excel:

- Otevřete program Microsoft Excel.
- Klikněte na "Soubor" a vyberte "Otevřít."
- Vyberte generovaný CSV soubor.
- V části "Vyberte typ souboru" zvolte "Oddělovač"
- V "Typ souboru" ověřte, že je nastaveno "65001- Unicode (UTF-8)" jako kódování.
- Klikněte na "Další"
- Nastavte "Oddělovače" na "Čárka"
- Klikněte na "Dokončit" pro zobrazení výsledků.


### 5. Poznámky
Tento skript byl vytvořen pro analýzu a zpracování dat z volebních stránek, jako projekt v rámci Python Akademie. Při používání skriptu buďte opatrní a dodržujte zákony a ustanovení týkající se zpracování dat.
