# DISASTER RESPONSE PIPELINE
## Part of Data Science Nanodegree Project

## Table of Contents
- **[1. Project Overview](#1)**
- **[2. Project Components](#2)**
    - **[2.1. ETL Pipeline](#2.1)**
    - **[2.2. ML Pipeline](#2.2)**
    - **[2.3. Flask Web App](#2.3)**
- **[3. Getting Started](#3)**
    - **[3.1. Project ETL Pipeline](#3.1)**
    - **[3.2. Project ML Pipeline](#3.2)**
    - **[3.3. Data Pipelines: Python Scripts](#3.3)**
    - **[3.4. Running ETL & ML Pipeline](#3.4)**
    - **[3.5. Deployment](#3.5)**
- **[4. Starter Code](#4)**
        - 

<a name="1"></a>
### 1. Project Overview

In this Project, I've learned and built on my data engineering skills to expand my opportunities and potential as a data scientist. In this project, I'll apply these skills to analyze disaster data from [Appen](“https://appen.com") to build a model for an API that classifies disaster messages.

In the Folder of "Notebook Pipeline", you'll find a data set containing real messages that were sent during disaster events. I'm creating a machine learning pipeline to categorize these events so that you can send the messages to an appropriate disaster relief agency.

This project will show off your software skills, including your ability to create basic data pipelines and write clean, organized code!. Below are a few screenshots of the web app.

https://github.com/Kazunosekai/PROJECT-UDACITY/blob/main/Disaster%20Response%20Pipeline/image/Homepage%201.png

[homepage 2](https://github.com/Kazunosekai/PROJECT-UDACITY/blob/main/Disaster%20Response%20Pipeline/image/Homepage%202.png)

<a name="2"></a>
## 2. Project Components

There are three components you'll need to complete for this project.

<a name="2.1"></a>
###  2.1. ETL Pipeline
In a Python script, `process_data.py`, write a data cleaning pipeline that:

- Loads the `messages` and `categories` datasets
- Merges the two datasets
- Cleans the data
- Stores it in a SQLite database

<a name="2.2"></a>
### 2.2. ML Pipeline
In a Python script, `train_classifier.py`, write a machine learning pipeline that:

- Loads data from the SQLite database
- Splits the dataset into training and test sets
- Builds a text processing and machine learning pipeline
- Trains and tunes a model using GridSearchCV
- Outputs results on the test set
- Exports the final model as a pickle file

<a name="2.3"></a>
### 2.3. Flask Web App
- Modify file paths for database and model as needed
- Add data visualizations using Plotly in the web app. One example is provided for you
- Running this command from app directory will start the web app where users can enter their query. 

<a name="3"></a>
## 3. Getting Started
Below are additional details about each component and tips to get you started.

I've provided some of Jupyter notebooks in folder of `notebook Pipeline` to get you started with both data pipelines. The Jupyter notebook is highly recommended to complete before getting started on the Python script.

<a name="3.1"></a> 
### 3.1. Project ETL Pipeline
The first part of your data pipeline is the Extract, Transform, and Load process. Here, you will read the dataset, clean the data, and then store it in a SQLite database. We expect you to do the data cleaning with pandas. To load the data into an SQLite database, you can use the pandas dataframe `.to_sql()` method, which you can use with an SQLAlchemy engine.

Feel free to do some exploratory data analysis in order to figure out how you want to clean the data set. Though you do not need to submit this exploratory data analysis as part of your project, you'll need to include your cleaning code in the final ETL script, `process_data.py`.

<a name="3.2"></a>
### 3.2. Project ML Pipeline
For the machine learning portion, you will split the data into a training set and a test set. Then, you will create a machine learning pipeline that uses NLTK, as well as scikit-learn's Pipeline and GridSearchCV to output a final model that uses the `message` column to predict classifications for 36 categories (multi-output classification). Finally, you will export your model to a pickle file. After completing the notebook, you'll need to include your final machine learning code in `train_classifier.py`.

<a name="3.3"></a>
### 3.3. Data Pipelines: Python Scripts
After you complete the notebooks for the ETL and Machine Learning (ML) pipeline, you'll need to transfer your work into Python scripts, `process_data.py` and `train_classifier.py`. If someone in the future comes with a revised or new dataset of messages, they should be able to easily create a new model just by running your code. These Python scripts should be able to run with additional arguments specifying the files used for the data and model.

<a name="3.4"></a>
### 3.4. Running ETL & ML Pipeline
Run the following commands in the project's root directory to set up your database and model.

1. To run ETL pipeline that cleans data and stores in database
   ```
   python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db
   ```
2. To run ML pipeline that trains classifier and saves
   ```
   python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl
   ```

<a name="3.5"></a>
### 3.5. Deployment
Open a new terminal window. You should already be in the `../Disaster Response Pipeline/App` folder, but if not, then use terminal commands to navigate inside the folder with the `run.py` file.

  - Go to `app` folder/directory with type : `cd app`

  - Run your web app with type : `python run.py`
    

Your web app should now be running if there were no errors and than go to ```http://0.0.0.0:3001```

<a name="4"></a>
## 4. Starter Code
The coding for this project can be completed using the Project Workspace IDE provided. Here's the file structure of the project:
```sh
    - app
        | - template
            | |- master.html  # main page of web app
            | |- go.html  # classification result page of web app
        |- run.py  # Flask file that runs app

    - data
        |- disaster_categories.csv  # data to process 
        |- disaster_messages.csv  # data to process
        |- DisasterResponse.db # database to save clean data to
        |- process_data.py # ETL Pipeline
        |- YourDatabaseName.db 
    
    - Img #result with screen shoot
        |- Homepage 1.png
        |- Homepage 2.png
        |- Homepage gif 1.gif
        |- Homepage gif 2.gif
        
    - models
        |- train_classifier.py
        |- classifier.pkl  # saved model 
    
    - Notebook Pipeline # project reference 
        |- ETL Pipeline Preparation.ipynb 
        |- ML Pipeline Preparation.ipynb 
        |- categories.csv
        |- DB_Preparation.db
        |- DisasterResponse.db
        |- messages.csv
        |- model.pkl
 
    - README.md
```


```python

```
