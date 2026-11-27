import pandas as pd


RAW_FILE = "dati/processed.cleveland.data"

COLS = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
        "thalach", "exang", "oldpeak", "slope", "ca", "thal", "num"]



df = pd.read_csv(RAW_FILE, names=COLS, na_values="?")

n_start = len(df)



before = len(df)
df = df.drop_duplicates()
removed_duplicates = before - len(df)



before = len(df)
df = df.dropna(subset=["ca"])
removed_missing_ca = before - len(df)



before = len(df)
df = df.dropna(subset=["thal"])
removed_missing_thal = before - len(df)



# Datu parveršana par veseliem skaitļiem
df["ca"] = df["ca"].astype(int)
df["thal"] = df["thal"].astype(int)



df["num"] = (df["num"] > 0).astype(int)



df.to_csv("tirs.csv", index=False)



print(f"Rindu skaits sākumā:            {n_start}")
print(f"Izmesti dublikāti:              {removed_duplicates}")
print(f"Izmesti (trūkst ca):            {removed_missing_ca}")
print(f"Izmesti (trūkst thal):          {removed_missing_thal}")
print(f"Rindu skaits beigās:            {len(df)}")
print(f"Pārbaude: {n_start} - {removed_duplicates + removed_missing_ca + removed_missing_thal} = {len(df)}")
