from bs4 import BeautifulSoup 
import pandas as pd  
import re
import nltk

#Read csv file with requests

train = pd.read_csv("wikipedia.annotated.csv", header=0, delimiter=",", error_bad_lines=False)

test= pd.read_csv("stack-exchange.requests.csv", header=0, delimiter=",", error_bad_lines=False)

#print(train.columns.values)

# Import BeautifulSoup into your workspace
            

# Initialize the BeautifulSoup object on a single movie review     
example1 = BeautifulSoup(train["Request"][6])  

# Print the raw review and then the output of get_text(), for 
# comparison
print train["Request"][6]
print example1.get_text()


# Use regular expressions to do a find-and-replace
letters_only = re.sub("[^a-zA-Z]",           # The pattern to search for
                      " ",                   # The pattern to replace it with
                      example1.get_text() )  # The text to search
print letters_only

lower_case = letters_only.lower()        # Convert to lower case
words = lower_case.split()               # Split into words

print words

nltk.download()  # Download text data sets, including stop words

from nltk.corpus import stopwords # Import the stop word list
print stopwords.words("english") 

# Remove stop words from "words"
words = [w for w in words if not w in stopwords.words("english")]
print words
