#/home/ibrahim/Downloads/matches_details.csv
from googlesearch import search

def google_search(query):
    for result in search(query, num_results=10):
        print(result)

query = "محمد صلاح"
google_search(query)