# Predicting_Cryptocurrency_Price_with_LSTM_ARIMA_NLP

#### Models Deployed
Artificial Recurrent Neural Network (RNN): Long-Short Term Memory, Natural Language Processing (NLP), Sentiment Analysis, Time Series (ARIMA)

#### Techniques Employed
Data Mining, Exploratory Data Analysis, Feature Engineering, Text Mining, Data Visualization, Machine Learning, Time Series Analysis, Financial Analysis, Parallel Processing

#### Tools Employed
Pickle, Beautiful Soup, TensorFlow, VADER, TextBlob, Keras, pyplot, statsmodels, Trading View API, Twitter API, various news API

### Context
Cryptocurrency has become an important investment asset as the public is looking for an alternative investment. As the first cryptocurrency, Bitcoin (BTC) is still the most prevalent cryptocurrency, and as such, its price fluctuation is widely anticipated. Given the recent rise in cryptocurrency, this project focuses on predicting BTC using a few techniques and insights. <br>

BTC price is volatile because of the following issues: <br>
(i) Lack of regulations<br>
(ii) Supply limitation/scarcity<br>
(iii) Correlation with other assets/stock market<br>
(iv) Lack of investment infrastructure<br>

### Datasets
To accommodate the issues causing price volatility, we collected data which could be categorized into 4 groups: <strong> Industry Insights, Selected Bitcoin Price Indicators, Sentiment Analysis and Fiat-Based Assets Indicators. </strong> Overall, 1,646,826 data points & 123,791 entries from 20 data sources were collected. <br>

The clean aggregated dataset has 41,403 data points, 1,488 entries and 30 selected features. <br>

### Chosen Model & Performance
To process news articles panel datasets, NLP and sentiment analysis were done. The sentiment was then translated as a feature in the dataset. <br>

Time series (ARIMA) and RNN (LSTM) model were then adopted to predict the price. January 2018 - September 2021 (4 years data) was chosen as the prediction horizon as it included the last Cryptocurrency "Winter" cycle and the latest Cryptocurrency "Boom & Crash" cycle due to recent BTC halving. LSTM was found to be a better model than ARIMA. <br>

The final LSTM model had 4 hidden layers with ~20% dropouts, 50 epochs and validation horizon of 5 months. The model gives MAPE of 7% and RMSE of 3,627.
<br>
### Collaborators
Felipe Chapa Chamorro (@FelipeChapa)<br>
Wong Cheng An (@wca91)<br>
Widya Salim (@salimwid)<br>
Sahil Sharma (@)<br>
Ankit Malhotra (@)<br>
Donghwan Kim (@hwaneest)
