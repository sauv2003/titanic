import streamlit as st
import pandas as pd
import joblib 

model = joblib.load("titanic.pkl")

st.title("Titanic Survival Predictor")

Pclass = st.selectbox("Pclass", [1,2,3])
Sex = st.selectbox("Sex", ["male", "female"])
Age = st.number_input("Age", 1, 100, 30)
SibSp = st.number_input("Siblings/Spouse Aboard", 0, 10, 0)
Parch = st.number_input("Parents/Children Aboard", 0, 10, 0)
Fare = st.number_input("Fare", 0.0, 600.0, 30.0)
Embarked = st.selectbox("Embarked", ["S","C","Q"])

if st.button("Predict"):
    sample = pd.DataFrame([{
        "Pclass": Pclass,
        "Sex": Sex,
        "Age": Age,
        "SibSp": SibSp,
        "Parch": Parch,
        "Fare": Fare,
        "Embarked": Embarked
    }],
        columns=['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']
    )

    sample = sample.astype({
        "Pclass": int,
        "Sex": str,
        "Age": float,
        "SibSp": int,
        "Parch": int,
        "Fare": float,
        "Embarked": str
    })

    pred = model.predict(sample)[0]
    st.write("Survived 🎉" if pred == 1 else "Did Not Survive ❌")