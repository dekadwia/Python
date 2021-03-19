#Import Library
from bs4 import BeautifulSoup
import requests
url ='https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'

# Meminta server mengambil URL
requests.get(url)
#Jika hasil [200] maka server membolehkan kita mengakses websitenya

halaman = requests.get(url)
halaman.text

# Parser-lxml :  merubah format htmml menjadi python
soup = BeautifulSoup(halaman.text, 'lxml')
soup

#Mengakses tag header 
soup.header

#Mengakses tag div 
soup.div

#Tag adalah sesuatu yg diawali tanda <, dan biasanya berwarna ungu
#sedangkan attribute adalah yg berwarna merah/orange

#mengambil tag di h1
soup.h1

#mengambil string dari tag di dalam tag (nested tag)
soup.header.p
soup.header.p.string

#Attribute fungsinya membedakan tag yg satu dengan tag yg lain

#mengambil tag a dalam <header>
a_awal = soup.header.a
a_awal

#mendapatkan attributenya saja
a_awal.attrs
a_awal['data-target']

#Menambahkan attribute baru
a_awal['attribute-baru']  = 'ini attribute baru'
a_awal.attrs

#attribute baru juga muncul di a secara keseluruhan
a_awal

#Mencari attribute tertentu dalam sebuah tag
soup.find('div', {'class':'side-collapse in'})
soup.find('div', {'id':'layout-footer'})
soup.find('div', class_ = 'side-collapse in')

#Menggunakan find_all
soup.find_all('h4', class_ = 'pull-right price')

#Slicing find all
soup.find_all('h4', class_ = 'pull-right price') [2:5]

#Menggunakan filter beberapa tag sekaligus 
soup.find_all(['h4', 'a', 'p'])
soup.find_all(['div', 'header'])
soup.find_all(id=True)
soup.find_all(class_=True)

#filter berdasarkan nama
nama = soup.find_all('a', class_='title')

#filter berdasarkan harga
harga = soup.find_all('h4', class_='pull-right price')

#filter review
reviews = soup.find_all('p', class_='pull-right')

#filter deskripsi
deskripsi = soup.find_all('p', class_ = 'description')

#mengambil string dari list_find _all
nama_produk_list = []
for i in nama :
    name = i.text
    nama_produk_list.append(name)
    
harga_list = []
for i in harga :
    price = i.text
    harga_list.append(price)
    
review_list = []
for i in reviews :
    riviw = i.text
    review_list.append(riviw)
    
deskripsi_list = []
for i in deskripsi :
    desk = i.text
    deskripsi_list.append(desk)

import pandas as pd
tabel = pd.DataFrame({'Nama Produk' : nama_produk_list,
                      'Harga' : harga_list,
                      'Reviews' : review_list,
                      'Deskripsi' : deskripsi_list})


