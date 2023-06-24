import requests
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer 
from sklearn.decomposition import LatentDirichletAllocation as LDA
from nltk import corpus
from nltk.corpus import stopwords


base_url = "https://www.airlinequality.com/airline-reviews/british-airways"
pages = 10
page_size = 100
reviews = []

for i in range(1, pages + 1):

    print(f"Scraping page {i}")

    # Create URL to collect links from paginated data
    url = f"{base_url}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"
    # Collect HTML data from this page
    response = requests.get(url)
    # Parse content
    content = response.content
    parsed_content = BeautifulSoup(content, 'html.parser')
    for para in parsed_content.find_all("div", {"class": "text_content"}):
        reviews.append(para.get_text())
    print(f"   ---> {len(reviews)} total reviews")
reviews_neg=[]
reviews_=reviews
for x in reviews:
	if 'Not Verified' in x:
		reviews_neg.append(x)
		reviews.remove(x)
df = pd.DataFrame()
df["reviews"] = reviews_
df.head()
df.to_csv("BA_reviews.csv")

