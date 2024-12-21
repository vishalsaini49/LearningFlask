from flask import Flask, request
import pickle

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ping", methods=['GET'])
def ping():
    return "<p>Hi! You pinged me, Thanks</p>"

@app.route("/Aboutus", methods=['GET'])
def aboutus():
    return "<p>Hi! My Name is Vishal Saini</p>"

model_pickle = open('clf.pkl',mode='rb')
clf = pickle.load(model_pickle)

@app.route("/prediction", methods=['POST'])
def prediction():
    req = request.get_json()
    print(req)

# Loan_Status({'N':0, 'Y':1})

    if req['Gender'] == 'Male':
        Gender = 0
    else:
        Gender = 1

    if req['Married'] == 'No':
        Married = 0
    else:
        Married = 1

    if req['Education'] == 'Graduate':
        Education = 0
    else:
        Education = 1

    if req['Self_Employed'] == 'Yes':
        Self_Employed = 0
    else:
        Self_Employed = 1

    if req['Property_Area'] == 'Rural':
        Property_Area = 0
    elif req['Property_Area'] == 'Semiurban':
        Property_Area = 0
    else:
        Property_Area = 1

    if req['Dependents'] == '3+':
        Dependents = 3

    LoanAmount = req['LoanAmount']
    Loan_Amount_Term = req['Loan_Amount_Term']
    Credit_History = req['Credit_History']
    Total_Income = req['ApplicantIncome'] + req['CoapplicantIncome']

    pred = clf.predict([[Gender, Married, Dependents, Education, Self_Employed, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area, Total_Income]])
    if pred == 0:
        res = "Not Approved"
    else:
        res = "Approved"
    return {"Loan Approval Status" : res}