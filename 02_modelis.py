import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score



KOLONNU_NOSAUKUMI = {
    "age": "vecums",
    "sex": "dzimums",
    "cp": "sāpju_tips",
    "trestbps": "asinsspiediens",
    "chol": "holesterīns",
    "fbs": "cukurs_tukšā_dūšā",
    "restecg": "ekg_rezultāts",
    "thalach": "maks_pulss",
    "exang": "sāpes_slodzē",
    "oldpeak": "st_depresija",
    "slope": "st_slīpums",
    "ca": "asinsvadu_skaits",
    "thal": "thallija_tests",
}



df = pd.read_csv("tirs.csv")


# y , ko modelis mācās prognozēt (0 = nav slimības, 1 = ir slimība)
# X rādītāji, pēc kuriem modelis prognozē
y = df["num"]
X = df.drop(columns=["num"])


# datus sadališana: 80% apmācībai un 20% testam
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)



model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
model_acc = accuracy_score(y_test, y_pred)


# Bāzes līnija: vienkāršs "modelis", kas vienmēr saka biežāko klasi
# Ja mūsu modelis nav labāks par to, tad tas neko noderīgu nemāca
dummy = DummyClassifier(strategy="most_frequent")
dummy.fit(X_train, y_train)
base_acc = accuracy_score(y_test, dummy.predict(X_test))

print(f"Modeļa precizitāte:  {model_acc:.3f}")
print(f"Bāzes līnija:        {base_acc:.3f}")
print(f"Starpība:            {model_acc - base_acc:+.3f}")



importance = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)

importance = importance.rename(index=KOLONNU_NOSAUKUMI)
print("\nVisu kolonnu svarīgums:")
print(importance.round(3))
print("\nDivas svarīgākās kolonnas:")
print(importance.head(2))


# rindas, kur modelis kļūdījās 
wrong_mask = (y_pred != y_test.values)
wrong = X_test[wrong_mask].copy()
# patieso atbildi un modeļa atbildi, priekš tiešu kļudas noveršanas
wrong["patiesā_slimība"] = y_test[wrong_mask]
wrong["modeļa_prognoze"] = y_pred[wrong_mask]

wrong = wrong.rename(columns=KOLONNU_NOSAUKUMI)
print(f"\nKļūdu skaits testā: {len(wrong)} no {len(y_test)}")
print(wrong.to_string())
