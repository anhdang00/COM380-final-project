import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk.tokenize
import re
from nltk.corpus import stopwords
import os 
  
analyzer = SentimentIntensityAnalyzer()
# Folder Path 
path =r"C:\Users\anhth\OneDrive\Desktop\Fall 2023\COM380\final-pj\tokens\neg"
  
# Change the directory 
os.chdir(path) 
list = []
  
# iterate through all file 
for file in os.listdir(): 
  file_path = f"{path}\{file}"
  with open(file_path, 'r') as f: 
    list.append(f.read())

#create a set of stop words, connectors, articles
stop_words = set(stopwords.words('english'))
#remove punctation and numbers
cleanedText = re.sub(r'[^a-zA-Z]', ' ', ''.join(list))
tokens = nltk.word_tokenize(cleanedText)
commonWords = nltk.FreqDist(w.lower() for w in tokens if w not in stop_words)
print("Reviews with high helpful votes")
print(commonWords.most_common(15))

# Folder Path 
path =r"C:\Users\anhth\OneDrive\Desktop\Fall 2023\COM380\final-pj\tokens\pos"
  
# Change the directory 
os.chdir(path) 
list = []
  
# iterate through all file 
for file in os.listdir(): 
  file_path = f"{path}\{file}"
  with open(file_path, 'r') as f: 
    list.append(f.read())

#create a set of stop words, connectors, articles
stop_words = set(stopwords.words('english'))
#remove punctation and numbers
cleanedText = re.sub(r'[^a-zA-Z]', ' ', ''.join(list))
tokens = nltk.word_tokenize(cleanedText)
commonWords = nltk.FreqDist(w.lower() for w in tokens if w not in stop_words)
print(commonWords.most_common(15))
