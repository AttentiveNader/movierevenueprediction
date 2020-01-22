# Box office revenue prediction
its a simple example on using a xgb based model (catboost)
with a bit of feature engineering  
# Data
You can get the data from the Kaggle competition (the competition has ended)
[Box office prediction](https://www.kaggle.com/c/tmdb-box-office-prediction/overview)
and the additional data is from
[additional features](https://www.kaggle.com/kamalchhirang/tmdb-competition-additional-features)

##  Data preprocessing
 only replacing missing values in different features with the a proper replacement
 ex. budget -->  mean budget by year ,
 One hot encoding the genres feature
 and generating features  like top actors  from the html files
 I got from these links which somehow seems like web scraping
 [top 1000 actors](https://www.imdb.com/list/ls058011111/)
 [top 200 directors](https://www.imdb.com/list/ls000009749/)


## Scores
with this feature engineering and optimization you can get a loss
(rmlse loss)  of about  1.95 to 2.005


*note :* you  should run the castandcrewfromhtmlfiles.py script before using the notebook
