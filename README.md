# Diabetes-Prediction-Using-ML-Models-and-Django-Framework
## Screen Shots
![image (1)](https://user-images.githubusercontent.com/109298390/180837675-1782c406-5c60-4cb3-82a7-1409ba2ada25.png)
![image (2)](https://user-images.githubusercontent.com/109298390/180837861-a4202b9e-d1ea-4aef-972c-8b5a7884ad84.png)
![image (3)](https://user-images.githubusercontent.com/109298390/180837916-712557e0-8828-4b83-bdf7-b83d21597ce9.png)


## Description how I do

        
          •	I am going to provide a Machine Learning based solution to predict Diabetes of the
          patient in real time on the bases of different attributes e.g. blood pressure, glucose,
          BMI, age and so on.
          •	First of all, I need the training and testing dataset of diabetes patients, and I am
          using kaggle website to download the data set.
          •	This dataset is originally from the National Institute of Diabetes and Digestive an
          Kidney Diseases. The objective of the dataset is to diagnostically predict whether or not
          a patient has diabetes, based on certain diagnostic measurements included in the dataset.
          •	The datasets consist of several medical predictor variables and one target variable,
          Outcome. Predictor variables includes the number of pregnancies the patient has had, their
          BMI, insulin level, age, and so on.
          •	I am going to apply 6 to 8 ML model to check accuracy in results and then select the
          best model in this aspect.
 
 ### Following ML models are going to be implemented:Basics Setting
 
          •	Linear Regression
          •	Logistic Regression
          •	SVM (Support Vector Machine) Algo
          •	Decision Tree Algo
          •	Random Forest Algo
          •	Naïve Bayes Algo
        
 ### Django
          
          •	For front end development, I will use Django framework to build Website. 
          •	Django is basically a high-level Python web framework that enables rapid
          development of secure and maintainable websites.
          •	Following are the examples of big websites, which use the Django framework
                •	YouTube
                •	Instagram
                •	Spotify
                •	Dropbox, etc.
 #### Basics Setting
	•	First of all, create a new project in pycharm, and run command (Django-admin startproject DiabetesPrediction). You can see some default files and folder, like manage.py, etc.
	•	The next step is to start our server, for that we have to type command in terminal ()
	•	In order to run whole project and run server type following commands (1. Python manage.py runserver)
	•	There is a link shown which is link of local host where our website resides.
	•	Create folder name templates under main directory (DiabetesPrediction). This is because we want to change the main html page of our site.
	•	Now create html file named as home inside template dir, and this home.html file is going to linked with main webage. 
	•	Now you can change the title to Home and in body you can write welcome to the home page. 
	•	The next step is to link this home.html in the urls.
	•	Open urls.py
	•	There is already one url mentioned which is for admin page
	•	Create views.py file under the DiabetesPrediction/DiabetesPrediction dir.
	•	Now import views in url by writing from . import views (. Specify current dir)
	•	We have to mention another url, so for that write path(“”,  views.home)
	•	Now open views.py
	•	Create function name home(request): and in this home function return the name of html page home.html which is home. render(request, 'home.html')	
	•	For that import from django.shortcuts import render
	•	Open settings.py 
	•	Go to the TEMPLATES, ‘DIR’ : [os.path.join(BASE_DIR, ‘templates’)]
	•	Now if you refresh the webpage you can see welcome to home page!
	•	Accessing Admin panel and setting user name and password
	•	Run the following commands in terminal
	•	Python manage.py makemigrations
	•	Python manage.py migrate
	•	Python manage.py createsuperuser
	•	(username: diana, Password: diana)
	•	Now further I edit the home.html page.
	•	I am going to begin by adding a background image in home page. For that I have to create a folder named as static under the main dir.
	•	Inside static dir create another dir named as DiabetesPrediction.
	•	Inside this DiabetesPrediction dir create another dir named as images.
	•	Inside the images dir put image that you want to set as home page background image.
	•	Next, open settings.py
	•	Drag to the bottom and add few lines of code
	•	STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'))
	•	STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')
	•	Now edit home.html page to add background image and button for the next page.
	•	Create another html page named as predict under the templates dir, change the title and add some text.
	•	Open urls.py
	•	Create another path for prediction page
	•	Open views.py and create function for predict
	•	Now design predict.html page

	
