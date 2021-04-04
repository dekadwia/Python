'''
Ini adalah script untuk tahapan Feature Engineering

Di pembelajaran kali ini kita akan memproses hal yang berkaitan dengan:
1. Nilai kosong (NA atau nan)
2. Variabel yang berhubungan dengan waktu (Tahun)
3. Variabel yang tidak berdistribusi normal
4. Menghilangkan variabel jarang untuk tipe kategori
5. Merubah format data string ke numerik untuk tipe kategori
6. Menyamakan rentang data nilai untuk beberapa variabel
'''

# Mengimpor library dasar yang diperlukan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

import warnings
warnings.simplefilter(action='ignore') # menghilangkan warning yang muncul

# Mengimpor dataset
# Link download harga_rumah.csv : https://cutt.ly/ul3frWb
dataku = pd.read_csv('harga_rumah.csv')

# Membagi data menjadi 2 yaitu training set dan test set
# Sebelumnya kita impor library dari scikit learn untuk membagi dataset menjadi 2
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(dataku,
                                                    dataku['SalePrice'],
                                                    test_size=0.1,
                                                    random_state=10)  # WAJIB mengisi random_state

# Mengatasi data NA untuk jenis data kategori
kolom_na_kategori = [kolom for kolom in dataku.columns if dataku[kolom].isnull().sum() > 0 and 
            dataku[kolom].dtypes=='O']

# Menghitung persentase dari data kategori yang kosong
dataku[kolom_na_kategori].isnull().mean()*100

# Mengganti data kategori yang kosong dengan sebutan 'Kosong'
X_train[kolom_na_kategori] = X_train[kolom_na_kategori].fillna('Kosong')
X_test[kolom_na_kategori] = X_test[kolom_na_kategori].fillna('Kosong')

# Memastikan bahwa kita tidak memiliki data nan di training set
X_train[kolom_na_kategori].isnull().sum()

# Memastikan tidak ada data kosong untuk tipe kategori di test set
X_test[kolom_na_kategori].isnull().sum()

# Mengatasi data NA untuk jenis data numerik
kolom_na_numerik = [kolom for kolom in dataku.columns if dataku[kolom].isnull().sum() > 0 and 
            dataku[kolom].dtypes!='O']

# Menghitung persentase dari data numerik yang kosong
dataku[kolom_na_numerik].isnull().mean()*100

# Mengganti data numerik kosong dengan modus
for kolom in kolom_na_numerik:
    # Menghitung modus
    hitung_modus = X_train[kolom].mode()[0] # [0] adalah untuk mengeluarkan indeksnya
    # Menambahkan kolom baru mendeteksi data kosong per barisnya
    X_train[kolom+'_na'] = np.where(X_train[kolom].isnull(), 1, 0) # jika ada kosong diisi 1, jika tidak diisi 0
    X_test[kolom+'_na'] = np.where(X_test[kolom].isnull(), 1, 0)
    # Memasukkan modus ke baris yang kosong
    X_train[kolom] = X_train[kolom].fillna(hitung_modus)
    X_test[kolom] = X_test[kolom].fillna(hitung_modus)

# Memastikan bahwa kita tidak memiliki data numerik kosong di training set
X_train[kolom_na_numerik].isnull().sum()

# Memastikan bahwa kita tidak memiliki data nan di test set
X_test[kolom_na_numerik].isnull().sum()

# Menghitung tahun berlalu untuk 4 variabel yang berhubungan dengan Tahun
def tahun_berlalu(data, col):
    data[col] = data['YrSold'] - data[col]
    return data

# Mengganti setiap kolom 'Tahun' menjadi selisihnya terhadap 'YrSold'
for kolom in ['YearBuilt', 'YearRemodAdd', 'GarageYrBlt']:
    X_train = tahun_berlalu(X_train, kolom)
    X_test = tahun_berlalu(X_test, kolom)

# Merubah variabel yang tidak normal menjadi mendekati normal (memudahkan proses regresi linear)
for kolom in ['LotFrontage', 'LotArea', '1stFlrSF', 'GrLivArea', 'SalePrice']:
    X_train[kolom] = np.log(X_train[kolom])
    X_test[kolom] = np.log(X_test[kolom])

# Memastikan kolom-kolom yang di log-transformed tidak memiliki data kosong
kolom_log = ['LotFrontage', 'LotArea', '1stFlrSF', 'GrLivArea', 'SalePrice']
X_train[kolom_log].isnull().sum()
X_test[kolom_log].isnull().sum()

# Mengatasi variabel jarang
# kita buat kolom kategori terlebih dahulu
kolom_kategori = [kolom for kolom in X_train.columns if X_train[kolom].dtypes=='O']
# Membuat fungsi mencari variabel jarang
def analisis_var_jarang(data, col, persentase):
    data = data.copy()
    # Menentukan persentase setiap kategori
    isi = data.groupby(col)['SalePrice'].count() / len(data)
    # Mengembalikan variabel yang di atas persentase kelangkaan yang kita tentukan
    return isi[isi < persentase].index

for kolom in kolom_kategori:
    # Mencari kategori yang jarang muncul
    var_jarang = analisis_var_jarang(X_train, kolom, 0.01)
    # Mengganti kategori jarang dengan string 'Jarang'
    X_train[kolom] = np.where(X_train[kolom].isin(var_jarang), 'Jarang', X_train[kolom])
    X_test[kolom] = np.where(X_test[kolom].isin(var_jarang), 'Jarang', X_test[kolom])

# Mengganti (encode) tipe data kategori menjadi tipe data numerik (untuk nanti proses membuat model dengan scikit learn)
def encode_kategori(train, test, kolom, target):
    # Mengurutkan kategori mulai dari nilai terendah untuk SalePrice nya 
    # Kita menghitung nilai rataan SalePrice setiap kategori dalam satu kolom, yg paling kecil mendapat index 0, selanjutnya 1, dst
    data_urut = train.groupby([kolom])[target].mean().sort_values().index
    # Membuat dictionary dari data yang sudah diurutkan di atas menjadi format integer
    # kita gunakan enumerate (for loop dengan mengembalikan index nya)
    # kita gunakan enumerate(data urut, start=0), artinya index dimulai dari nol
    data_ordinal = {k: i for i, k in enumerate(data_urut, start=0)} 
    # Menggunakan dictionary di atas untuk mengganti data kategori menjadi integer
    train[kolom] = train[kolom].map(data_ordinal) # map method di Pandas: mengganti nilainya dengan nilai lain
    test[kolom] = test[kolom].map(data_ordinal)

# For loop untuk fungsi encode_kategori
for kolom in kolom_kategori:
    encode_kategori(X_train, X_test, kolom, 'SalePrice')

# Mengecek NA di training dan test set
X_train.isnull().sum()
train_kosong = [kolom for kolom in X_train.columns if X_train[kolom].isnull().sum() > 0]
X_test.isnull().sum()
test_kosong = [kolom for kolom in X_test.columns if X_test[kolom].isnull().sum() > 0]

# Mengisi kolom numerik dengan modus di test set
for kolom in test_kosong:
    # Menghitung modus
    hitung_modus = X_test[kolom].mode()[0] # [0] adalah untuk mengeluarkan indeksnya
    # Menambahkan kolom baru mendeteksi data kosong per barisnya
    X_test[kolom+'_na'] = np.where(X_test[kolom].isnull(), 1, 0)
    # Memasukkan modus ke baris yang kosong
    X_test[kolom] = X_test[kolom].fillna(hitung_modus)

# Mengecek ulang test set
test_kosong = [kolom for kolom in X_test.columns if X_test[kolom].isnull().sum() > 0]

# Melihat plot semua data kategori
def analisis_kategori(data, col):
    data = data.copy()
    data.groupby(col)['SalePrice'].median().plot.bar()
    plt.title(col)
    plt.ylabel('SalePrice')
    plt.tight_layout()
    plt.show()

batas = len(kolom_kategori)
i = 1
for kolom in kolom_kategori:
    i+=1
    analisis_kategori(X_train, kolom)
    if i <= batas: plt.figure() 

# Membuat variabel kolom_training yaitu gabungan semua kolom selain kolom 'Id' dan 'SalePrice'
kolom_training = [kolom for kolom in X_train.columns if kolom not in ['Id', 'SalePrice', 'LotFrontage_na', 'MasVnrArea_na', 'GarageYrBlt_na']]

# Proses feature scaling dengan MinMaxScaler (membuat rentang data antara 0-1)
from sklearn.preprocessing import MinMaxScaler
sc_X = MinMaxScaler()
X_train[kolom_training] = sc_X.fit_transform(X_train[kolom_training]) 
X_test[kolom_training] = sc_X.transform(X_test[kolom_training])

# Menyimpan file untuk proses feature selection
X_train.to_csv('xtrain.csv', index=False)
X_test.to_csv('xtest.csv', index=False)