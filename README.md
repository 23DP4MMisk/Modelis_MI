# Pirmais modelis no nulles

Projekts apmāca Random Forest modeli, kas prognozē sirds slimības esamību (0/1)
pēc pacientu medicīniskajiem rādītājiem. Datu kopa: Heart Disease (Cleveland), UCI.

## Nepieciešamās bibliotēkas
- Python 3.10+
- pandas
- scikit-learn

Instalēšana: `pip install pandas scikit-learn`

## Kā palaist
1. `python 01_tirisana.py`  (nolasa dati/processed.cleveland.data, izveido tirs.csv)
2. `python 02_modelis.py`   (apmāca modeli, izvada precizitāti, bāzes līniju un svarīgākās kolonnas)

Rezultātu skaidrojums ir failā `rezultati.md`.