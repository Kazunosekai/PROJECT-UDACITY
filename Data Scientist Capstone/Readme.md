# Data Scientist Capstone : Indonesia Earthquake

Indonesia is one of the countries where almost all of its land is in the "Ring of Fire". understanding and learning how earthquake disasters in Indonesia are very important for the Indonesian government to mitigate things that might hurt the people of Indonesia.

We will create a machine learning model that can predict future earthquake events based on recorded data of previous earthquake events. This machine-learning model can be developed for other strategic purposes.

## Project Overview
The dataset I'm using here is eartquake in an Indonesia from [Kaggle](https://www.kaggle.com/code/elmajoadriel/indonesia-earthquake-analysis-and-insight/data). The Machine Learning models used are:

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
