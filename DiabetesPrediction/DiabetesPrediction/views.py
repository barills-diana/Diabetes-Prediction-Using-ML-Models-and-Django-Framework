
from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score, r2_score

def home(request):
    return render(request, 'home.html')
def predict(request):
    return render(request, 'predict.html')
def research(request):
    return render(request, 'research.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def result(request):

    # read data
    data = pd.read_csv("C:\\Users\\hp\\Google Drive\\Fiverr Work\\2022\\6. Diabetes_Prediction_Using_ML\\DiabetesPrediction\\DiabetesPrediction\\diabetes.csv")

    # feature selection
    x = data.drop(['Outcome'], axis=1)
    y = data['Outcome']

    # Train and Test dataset
    xTrain, xTest, yTrain, yTestsvm = train_test_split(x, y, test_size=0.2, random_state=0)

    # Building SVM Model
    model = svm.SVC(kernel='rbf')
    model.fit(xTrain, yTrain)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

    yPredsvm = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])

    result1 = ""
    result11 = ""
    if yPredsvm == [1]:
        result1 = "Positive"
    else:
        result1 = "Negative"



    return render(request, 'result.html', {"result2": result1})
