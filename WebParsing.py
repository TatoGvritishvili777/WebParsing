import requests
from bs4 import BeautifulSoup
import csv
file = open('Biblusi_Books.csv', 'w', encoding='utf-8_sig', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(['სათაური', 'ავტორი', 'ფასი'])
for ind in range(1, 5):
    url = 'https://ibooks.ge/books?&page=' + str(ind)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    row = soup.find('div', class_='books fix')
    books = row.find_all('div', class_='bookc left')
    for book in books:
        title_bar = book.find('div', class_='book-text')
        book_name = title_bar.h2.a.text
        author = title_bar.h3.text
        p = book.find('div', class_='book')
        price = p.span.text
        file_obj.writerow([book_name, author, price])
file.close()