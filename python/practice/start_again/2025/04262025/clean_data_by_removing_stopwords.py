#   https://www.geeksforgeeks.org/create-inverted-index-for-file-using-python/
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwrods
nltk.download('stopwords')
for i in range(1):
    text_tokens = word_tokenize(read)
token_without_sw = [ word for word in text_tokens if not  word in stopwrods.words()]
print (token_without_sw)


