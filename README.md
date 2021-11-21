# Movie Review Analysis using NLP 🎞️🎥


### Project Link ->  https://movie-review-analysis-nlp.herokuapp.com/ 🌐🌐

![enter image description here](https://miro.medium.com/max/1920/1*eycKZ9TADFBcO8w_CSejwA.png)

Sentiment Analysis refers to detecting the polarity of any comment whether it is having a positive meaning or negative. It has multiple applications for example in checking review of a newly launched movie , for checking sentiment about any movement like kissan andolan and also for automatic feedback classification and many more. 

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://sars-covid19-xray-detection.herokuapp.com/)&nbsp;[![Build passing](https://img.shields.io/badge/Build-Passing-brightgreen.svg?style=flat-square)](https://sars-covid19-xray-detection.herokuapp.com/)&nbsp;[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://foodeazy.herokuapp.com/)&nbsp;[![License](https://img.shields.io/badge/license-MIT-brightgreen)](https://sars-covid19-xray-detection.herokuapp.com/)&nbsp;![Made with Love in India](https://madewithlove.org.in/badge.svg)

**Project Link** - ***https://movie-review-analysis-nlp.herokuapp.com/***




![enter image description here](https://github.com/ritik-sys/movie-review-analysis-using-NLP/blob/main/Screenshots/Screenshot4.png)

 ## Flowchart
![enter image description here](https://github.com/ritik-sys/movie-review-analysis-using-NLP/blob/main/Screenshots/Screenshot5.png)

## DATA PREPROCESSING🚀
Text is messy, people love to throw in attempts at expressing themselves more clearly by adding extravagant punctuation and spelling words incorrectly. However, machine learning models can’t cope with text as input, so we need to map the characters and words to numerical representations.
Basic pre-processing for text consists of removing non-alphabetic characters, stop words (a set of very common words like the, a, and, etc.) and changing all words to lowercase.

## Bag of Words 🚀
We obtain the vocabulary list from the corpus (whole text dataset). The length of the vocabulary list is equal to the length of the vector that will be output when we apply Bag of Words (BOW). For each item (could be an entry, sentence, line of text), we transform the text into a frequency count in the form of a vector. In this case, we limit it to the top 5000 words to restrict the dimensionality of the data. We code this by setting up a count vectorizer from sklearn’s library, fit it on the training data and then transform both the training and test data.

## Word2Vec 🚀
Word2vec (Word to Vector) is a two-layer neural net that processes text. Its input is a text corpus and its output is a set of vectors: feature vectors for words in that corpus. The algorithm was created by Google in 2013. The 50-D space can be visualised by using classical projection methods (e.g. PCA) to reduce the vectors to two-dimensional data that can be plotted on a graph.


## Tf-Idf 🚀
This is short for Term-frequency-Inverse-Document-Frequency and gives us a measure of how important a word is in the document.
Term frequency (the same as for bag of words):Inverse document frequency measures how rare a term is across all documents (the higher the value, the rarer the word).
We combine these two to get Tf-Idf.To implement this representation, we use the TfidfTransformer function from sklearn’s library. Fitting occurs on the training set and the values for the same words are determined for the test set.



 ## UI/UX
 ### Screenshot-1![enter image description here](https://github.com/ritik-sys/movie-review-analysis-using-NLP/blob/main/Screenshots/Screenshot2.png)
 ### Screenshot-2![enter image description here](https://github.com/ritik-sys/movie-review-analysis-using-NLP/blob/main/Screenshots/screenshot1.png)
 ### Screenshot-3![enter image description here](https://github.com/ritik-sys/movie-review-analysis-using-NLP/blob/main/Screenshots/Screenshot3.png)
## Tech Stack and Tools 💻

 - [Python]
 - [Google Colab]
 - [Anaconda]
 - [Flask]
 - [Keras]

## Installation :zap:

 **1. Clone this repo by running the following command :-**
 ```bash
  git clone https://github.com/ritik-sys/movie-review-analysis-using-NLP.git
  cd movie-review-analysis-using-NLP
 ```
 
 **2. Now start the  server  by running the following command :-**
 ```bash
 python app.py
 ```
 
 **4.** **🎉  Open your browser and go to  `https://localhost:3000`**
 
## Contributors 🤝
 - [**Ritik Kumar**](https://github.com/ritik-sys)  

 
 
## 🤩 Don't forget to give this repo a ⭐ if you like this repo and want to appreciate efforts
 

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](https://forthebadge.com)


## References
<a id="1">[1]</a> 
Bag of Words Meets Bags of Popcorn. (n.d.). Retrieved from https://www.kaggle.com/c/word2vec-nlp-tutorial/

<a id="1">[2]</a> 
Gandhi, R. (2018, May 5). Naïve Bayes Classifier. Retrieved from https://towardsdatascience.com/naive-bayes-classifier-81d512f50a7c

<a id="1">[3]</a> 
Gandhi, R. (2018, May 5). Naïve Bayes Classifier. Retrieved from https://towardsdatascience.com/naive-bayes-classifier-81d512f50a7c

