# Data Scientist Capstone : Indonesian Earthquake

Indonesia is one of the countries where almost all of its land is in the "Ring of Fire". understanding and learning how earthquake disasters in Indonesia are very important for the Indonesian government to mitigate things that might hurt the people of Indonesia.

We will create a machine learning model that can predict future earthquake events based on recorded data of previous earthquake events. This machine-learning model can be developed for other strategic purposes.

## Project Overview
The dataset I'm using here is eartquake in Indonesia from [Kaggle](https://www.kaggle.com/code/elmajoadriel/indonesia-earthquake-analysis-and-insight/data). The Machine Learning models used are:

1. XGB Classifier
2. K-Nearest Neighbors Classifier
3. AdaBoost Classifier

Metrics that we’ll use for evaluating the models are accuracy and F1-score metric. We choose accuracy as a matrix because it will be used as a reference for algorithm performance if the data set has a very close number of False Negatives and False Positives. However, if the numbers are not close, then I should use the F1 Score as a reference.

## Summary
This article is intended to:

- Beginner Machine Learning model building
- Analyze datasets with simple visualizations
- Train Various Machine Learning Models to choose the most suitable one

We use simple methods to do several things such as cleaning data, exploring data, building models and evaluating models. We ended up achieved highest accuracy on XGB Classifier. In the future we can use this model (with some improvements) help to mitigate earthquake disasters, so that an early warning can be made, minimize property damage, and it is hoped that the number of earthquake victims can be reduced.

## File Description
- data/earthquaqe_id.csv : Main data from [Kaggle](https://www.kaggle.com/code/elmajoadriel/indonesia-earthquake-analysis-and-insight/data) which I renamed to earthquaqe_id.csv
- image : The image folder contains the screenshot results
- Indonesia-earthquake.ipynb : Notebook file containing Analyze datasets with simple visualizations, Beginner Machine Learning model building, and Train Various Machine Learning Models to choose the most suitable one 
- Readme.MD : Short information about the contents of the repository
    
## Software Requirements
To plot 2D data on maps in Python using matplotlib, we have to install several packages from matplotlib, namely basemap and basemap-data.

How To install this package ? you can see [here.](https://github.com/Kazunosekai/PROJECT-UDACITY/blob/main/Data%20Scientist%20Capstone/requirements.txt)


    
## Blog Post
You can find my blog post: https://medium.com/@kazunobetta/the-simple-machine-learning-model-for-indonesian-earthquake-eab8447e98c5



## Reference 
- https://thecleverprogrammer.com/2020/11/12/earthquake-prediction-model-with-machine-learning/
- https://machinelearningmastery.com/develop-first-xgboost-model-python-scikit-learn/
- https://machinelearningknowledge.ai/knn-classifier-in-sklearn-using-gridsearchcv-with-example/
- https://www.datacamp.com/tutorial/adaboost-classifier-python


## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
