import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score


df = pd.read_csv("tirs.csv")


y = df["num"]
X = df.drop(columns=["num"])


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
model_acc = accuracy_score(y_test, y_pred)


dummy = DummyClassifier(strategy="most_frequent")
dummy.fit(X_train, y_train)
base_acc = accuracy_score(y_test, dummy.predict(X_test))

print(f"Modeļa precizitāte:  {model_acc:.3f}")
print(f"Bāzes līnija:        {base_acc:.3f}")
print(f"Starpība:            {model_acc - base_acc:+.3f}")


importance = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\nVisu kolonnu svarīgums:")
print(importance.round(3))
print("\nDivas svarīgākās kolonnas:")
print(importance.head(2))


wrong_mask = (y_pred != y_test.values)
wrong = X_test[wrong_mask].copy()
wrong["patiesā_num"] = y_test[wrong_mask]
wrong["modeļa_atbilde"] = y_pred[wrong_mask]
print(f"\nKļūdu skaits testā: {len(wrong)} no {len(y_test)}")
print(wrong.to_string())