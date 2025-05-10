import pandas as pd
from bs4 import BeautifulSoup
import requests 

website = "https://books.toscrape.com/catalogue/category/books/autobiography_27/index.html" 

response = requests.get(website)

response.status_code
print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')

print(soup)

books = soup.find_all('article', {'class':"product_pod"})

print(books)

print(len(books))

data = []

for book in books:
    title = book.h3.a['title']
    price = book.find('p',class_="price_color").text.strip()
    rating_tag = book.find('p',class_="star-rating")
    rating = rating_tag.get('class')[1] if rating_tag else "No rating"
    stock = book.find('p',class_="instock availability").text.strip()
    
    data.append({
        'Title': title,
        'Price': price,
        'Rating': rating,
        'Availability': stock
    })

    

df = pd.DataFrame(data)
df.to_csv("autobiography_books.csv", index=False)
print("✅ Data saved to autobiography_books.csv")
