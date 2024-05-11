from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import matplotlib
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
# Splitting the dataset into Training and Testing Data
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Plotting The Correlations between all the features

# model = pickle.load(open("./Customer_Churn_Prediction.pkl", "rb"))
if __name__ == "__main__":
    with open("./Customer_Churn_Prediction_Logistic.pkl", "rb") as f:
        model = pickle.load(f)


@app.route("/", methods=["GET"])
def Home():
    return render_template("index.html")


standard_to = StandardScaler()


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        CreditScore = int(request.form["CreditScore"])
        Age = int(request.form["Age"])
        Tenure = int(request.form["Tenure"])
        Balance = float(request.form["Balance"])
        Balance = f"{Balance:.2f}"
        NumOfProducts = int(request.form["NumOfProducts"])
        HasCrCard = int(request.form["HasCrCard"])
        IsActiveMember = int(request.form["IsActiveMember"])
        EstimatedSalary = float(request.form["EstimatedSalary"])
        Geography_Germany = request.form["Geography_Germany"]

        # if Geography_Germany == "Germany":
        #     Geography_Germany = True
        #     Geography_Spain = False
        #     Geography_France = False

        # elif Geography_Germany == "Spain":
        #     Geography_Spain = True
        #     Geography_Germany = False
        #     Geography_France = False

        # elif Geography_Germany == "France":
        #     Geography_France = True
        #     Geography_Germany = False
        #     Geography_Spain = False

        # Gender_Male = request.form["Gender_Male"]

        # if Gender_Male == "Male":
        #     Gender_Male = True
        #     Gender_Female = False
        # elif Gender_Male == "Female":
        #     Gender_Female = True
        #     Gender_Male = False
        # print(Gender_Female)
        if Geography_Germany == "Germany":
            Geography_Germany = 1
            Geography_Spain = 0
            Geography_France = 0

        elif Geography_Germany == "Spain":
            Geography_Spain = 1
            Geography_Germany = 0
            Geography_France = 0

        elif Geography_Germany == "France":
            Geography_France = 1
            Geography_Germany = 0
            Geography_Spain = 0

        Gender_Male = request.form["Gender_Male"]

        if Gender_Male == "Male":
            Gender_Male = 1
            Gender_Female = 0
        elif Gender_Male == "Female":
            Gender_Female = 1
            Gender_Male = 0
        prediction = model.predict(
            [
                [
                    CreditScore,
                    Age,
                    Tenure,
                    float(Balance),
                    NumOfProducts,
                    HasCrCard,
                    IsActiveMember,
                    EstimatedSalary,
                    Geography_France,
                    Geography_Germany,
                    Geography_Spain,
                    Gender_Female,
                    Gender_Male,
                ]
            ]
        )
        print(CreditScore)
        print(Age)
        print(Tenure)
        print(Balance)
        print(NumOfProducts)
        print(HasCrCard)
        print(IsActiveMember)
        print(EstimatedSalary)
        print(Geography_France)
        print(Geography_Germany)
        print(Geography_Spain)
        print(Gender_Female)
        print(Gender_Male)
        print(prediction)
        if prediction == 1:
            return render_template(
                "index.html", prediction_text="The Customer will leave the bank"
            )
        else:
            return render_template(
                "index.html", prediction_text="The Customer will not leave the bank"
            )


if __name__ == "__main__":
    app.run(debug=True)
