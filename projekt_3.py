"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Michal Krhut
email: michal.k.ppc@gmail.com
discord: Michal K.#3398
"""

import requests
import sys
from bs4 import BeautifulSoup as bs
import pandas as pd


def zanalyzuj_data_z_webu(url):
    data = requests.get(url)
    soup = bs(data.content, "html.parser")
    return soup


def vsechny_obce(soup):
    vsechny_obce = soup.find_all("td", {"class": "overflow_name"})
    obce = [obce.text for obce in vsechny_obce]
    return obce


def kody_obci(soup):
    kody_obci = soup.find_all("td", {"class": "cislo"})
    kody = [kody.text for kody in kody_obci]
    return kody


def nazvy_stran(url_sub, kody):
    for kod in kody:
        url = f"{url_sub}{kod}"
        soup = zanalyzuj_data_z_webu(url)
        strany_soup = soup.find_all("td", {"class": "overflow_name", "headers": ["t1sa1 t1sb2", "t2sa1 t2sb2"]})
        strany = [strany.text for strany in strany_soup]
    return strany


def kompilator_dat(url_sub, kody, obce, strany):
    volici_v_seznamu = []
    vydane_obalky = []
    platne_hlasy = []
    data_hlasy = []
    for kod in kody:
        url = f"{url_sub}{kod}"
        soup = zanalyzuj_data_z_webu(url)
        volici_v_seznamu.append(soup.find("td", {"class": "cislo", "headers": "sa2"}).text.replace(" ", "").replace('\xa0', ''))
        vydane_obalky.append(soup.find("td", {"class": "cislo", "headers": "sa3"}).text.replace(" ", "").replace('\xa0', ''))
        platne_hlasy.append(soup.find("td", {"class": "cislo", "headers": "sa6"}).text.replace(" ", "").replace('\xa0', ''))
        hlasy = soup.find_all("td", {"class": "cislo", "headers": ["t1sa2 t1sb3", "t2sa2 t2sb3"]})
        hlasy_ocistene = [hlas.text.replace(" ", "").replace('\xa0', '') for hlas in hlasy]
        data_hlasy.append(hlasy_ocistene)
        data_1 = {'Kódy': kody, 'Obce': obce, 'Voliči v seznamu': volici_v_seznamu, 'Vydané obálky': vydane_obalky, 'Platné hlasy': platne_hlasy}
        data_2 = {a: [data_hlasy[b][c] for b in range(len(data_hlasy)) for c, d in enumerate(strany) if d == a] for a in strany}
        data_vse = {**data_1, **data_2}
    return data_vse


def vytvoreni_csv(data_vse, csv_soubor):
    datovy_ramec = pd.DataFrame.from_dict(data_vse)
    print ("Vytvářím CSV soubor... ")
    datovy_ramec.to_csv(csv_soubor, index=False, encoding='utf-8-sig', sep=",")
    return datovy_ramec


def kontrola_vstupu():
    if len(sys.argv) != 3:
        print(f"Program potřebuje 2 argumenty, aby jsi ho mohl spustit - URL adresu a název CSV souboru. Zkus to znovu. ")
        sys.exit()
    spravne_hodnoty_url = (
        "https://www.volby.cz/pls/ps2017nss/",
        "https://volby.cz/pls/ps2017nss/"
    )
    if not sys.argv[1].startswith(spravne_hodnoty_url):
        print(f"První argument (URL adresa) není správně. Zkus to znovu. ")
        sys.exit()
    if not sys.argv[2].endswith(".csv"):
        print(f"Druhý argument (název souboru) není správně. Zkus ho vložit například ve tvaru 'soubor.csv'")
        sys.exit()
    else:
        print(f"Stahuji data z URL adresy: {sys.argv[1]} \nChvíli strpení...")


def main():
    kontrola_vstupu()
    csv_soubor = sys.argv[2]
    url = sys.argv[1]
    url_sub = f"https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec="
    soup=zanalyzuj_data_z_webu(url)
    kody=kody_obci(soup)
    obce=vsechny_obce(soup)
    strany=nazvy_stran(url_sub, kody)
    data_vse=kompilator_dat(url_sub, kody, obce, strany)
    vytvoreni_csv(data_vse,csv_soubor)
    print(f"Data z webu byly úspěšně uložena do souboru: {csv_soubor}. \nUkončuji program ")


if __name__ == '__main__':
    main()