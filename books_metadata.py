import requests
import json

def books_data(book_name):
  url = "https://www.googleapis.com/books/v1/volumes?q="+book_name
  data = []
  data = requests.get(url)
  if data!=[]:
    return data.json()['items'][0]['volumeInfo']
  else:
    return data