import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
import joblib

# Load data
df = pd.read_csv("Titanic.csv")
df = df[['Survived','Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']]
df = df.dropna()

X = df.drop("Survived", axis=1)
y = df["Survived"]

cat_cols = ['Sex','Embarked']
num_cols = ['Pclass','Age','SibSp','Parch','Fare']

pre = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols),
        ('num', 'passthrough', num_cols)
    ],
    remainder='drop'
)

clf = Pipeline([
    ('preprocessor', pre),
    ('model', LogisticRegression(max_iter=1000))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

clf.fit(X_train, y_train)

print("Accuracy:", clf.score(X_test, y_test))

joblib.dump(clf, "titanic.pkl")