#Melihat type data
bil = 3.6
type(bil)

#Modulus di python
6%2

#Pangkat
2**3

#indexing dan slicing
item_saya = ["ikan", 'ayam', 'bebek']
item_saya[2]

#Slicing character
"aku bisa belajar python"[1:5]

#Mengambil semua string 
"Belajar Python itu mudah"[:]

#aturan slicing : [awal:jarak:step]
"Belajar Python itu mudah"[2::2]

#indexing mundur
"Belajar Python itu mudah"[::-1]

#Mengganti variabel. String tidak bisa dengn cara seperti ini
var1 = [1,2,3,4,5]
var1[2] = 100

#Mengganti atau menambah sebuah variabel type character
nama = 'Bambang'
nama = nama +'Suyoto'

#Method di Python 
#Merubah menjadi huruf besar semua
var1 = 'Makanan itu adalah 4 sehat 5 sempurna'
var1.upper() #tidak merubah nila var1
#Merubah nilai var1
var1 = var1.upper()

#Membagi satu list menjadi beberapa variabel
var1.split()

#Membagi split berdasarkan huruf A
var1.split['A']

#Print method and formatting 
print("ini ada {} buah apel".format('10'))
print("urutan pemenang lomba lari adalah {2} {0} {1}".format('Aji', 'Bambang', 'Budi'))
#angka dalam curly bracket akan mengambil index dari character yg ada pada format()
print("urutan pemenang lomba lari adalah {a} {c} {b}".format(c='Aji', b='Bambang', 
                                                             a='Budi'))
phi = 22/7
print('untuk menghitung luas lingkaran gunakanlah phi = {}'.format(phi))

luas1= 667.8
luas2 = 700
print('Luas tanah yg dimiliki pak Budi adalah {a:8.3f} {b=5.2f}'.format(a = luas1, b= luas2))
#angka 8 menunjukkan jumalh spasinya, dan 3f merupakan 3 angka dibelakang koma

#Fungsi Len : Menghitung jumlah karakter
keranjang = [1,2.1, 'Apel']
#looping dengan len
for i in range(len(keranjang)) :
    print(keranjang[i])

for i in keranjang:
    print (keranjang[i])
#Menambahkan isi list 
jeruk =['jeruk']
keranjang = keranjang + jeruk

buah_lagi = ['anggur', 'nanas', 'jeruk bali', 'apel washington']
keranjang = keranjang.append(buah_lagi)
len(keranjang)

#menghilangkan item di list
baru = [1,2,3,4,5,6]
baru.pop() #Menghilangkan 1 item terakhir dalam list
baru.pop(1) #menghilangkan index pada item ke dua

#Mengurutkan Variabel 
variabel = [1,2,5,7,9]
variabel.sort()
var_baru =['a','c','b']
var_baru.sort()

#Mengurutkan variabel secara descending 
variabel.reverse()

#Nested List
isi = [1,2,3,4,5,[6,7,8,[9,10,11,'target',12]]]
#mengambil target dari nested list
isi[5][3][3]

#Membuat list dengan cara lain 
var = list()

#membuat nested list dan looping 
ganjil = [1,3,5,7,9]
genap = [2,4,6,8,10]
bilangan = [ganjil, genap]
for i in bilangan:
    print(i)
    
for j in i:
    print(j)

#Belajar Dictionaries : Untuk membuat database
dict1= {'k1':'ayam', 'k2':'kambing', 'k3':'sapi'}
dict1
dict1['k2']

dict2 = {'k1': 'ayam', 'k2' : 30, 'k3':['a', 'b', 20.5], 'k4':{'k5': 'apel', 'k6' :'jeruk', 'k7' : 'pisang'}}
#slicing dictionaries
dict2['k4']['k6']
#mengganti item di dictionaries
dict2['k3'] = 'Change Item'
dict2
#melihat key items 
dict2.keys()
#melihat isi dari items
dict2.values()
#melihat pasangan antar item
dict2.items()
#merubah menjadi huruf capital semua pada dictionaries
capital = print(dict2['k4']['k7'].upper())

#Tipe data Tuples : Tipe data tuple adalah tipe data yg tidak bisa diubah
keranjangt = (1,2,3,4,5)
t1 = (1,2,4.5, 'a''c')
type(t1)
#slicing tuple
keranjangt[2]
#Mengganti data di tupple
keranjangt = keranjangt[0],keranjangt[1], 'jeruk', keranjangt[3], keranjangt[4] 
keranjangt
#cara lain adalah mengganti menjadi list
keranjangt = list(keranjangt)
keranjangt
#meruba kembali menjadi bentuk tupple
keranjangt = tuple(keranjangt)
type(keranjangt)
#Methods di tuple
tu1 = (1,2,3,4,5,2,2,2,2,2)
tu1.count(2)
tu1.index(2)

#Multiple assignment & tuple
a,b,c,d = 1,2,3,4
a
d
a=b=c=d = 'yes'
a
#Mengganti dengan cara multiple assignment
a,b = 1,2
a
b
a,b = b,a
#Multiple assignment with tuple
tas = ('rambutan', 41, 9.87, [1,2,3,4])
item1, item2, item3, item4 = tas
item1

#Tipe data sets : untuk elemen yg bersifat unik(tanpa duplikasi), dan tidak berurutan
set1 = set()
set1.add('kuning')
set1.add('biru')
set1

list_angka = [1,2,3,4,4,4,4,5,5,5,6,7]
set_list_angka = set(list_angka)
set_list_angka

#Conditional
berat = 80
if(berat >100) :
    print('Overweight')
elif(0<=berat<=50) :
    print('too tiny')
elif(berat>50 and berat < 80):
    print('ideal weight')
else:
    print('almost ideal')

#for loops
for i in 'saya belajar python':
    print(i)
#Print for loops menyamping    
for i in 'saya belajar python':
    print(i, end='')

#contoh lain for loops 
angka = [1,2,3,4,5,6,7,8,9,10]
jumlah = 0
for i in angka:
    jumlah = jumlah + i
    print('Hasil Penjumlahan pada iterator ke {} adalah {}'.format(i, jumlah))
    
#Penggunaan looping dan conditionals
jumlah = 0 
for i in 'saya belajar python':
    jumlah = jumlah + 1
    if(i == 'a'):
        print('hey kamu berada di huruf A indeks ke-', jumlah)
        
#latihan for loop
angka_lat = [1,2,3,4,5,6,7,8,9,10]
for i in angka_lat:
    if(i%2==0):
        print('Angka {} adalah bilangan genap'.format(i))
    else:
        print('Angka {} adalah bilangan ganjil'.format(i))
        
#for loop untuk tuple
box1 = ((1,2), (3,4), (5,6))
for i in box1:
    print(i)
    
for a,b in box1:
    print(a)
    print(b)
    
#While Loops 
indeks = 0
while True:
    print("Saya berhasil menjalankan while loop")
    indeks = indeks +1
    if indeks == 10:
        break

#another example
x = 0
while x <50:
    print('Bilangan x saat ini adalah', x)
    x = x +2
    
#Function continue in loop 
angka2 = [1,2,3,4,5,6,7,8,9,10]
for i in angka2:
    if(i%2==0):
        continue
    else:
        print("Ini adalah angka-", i)
        
#Pass function in loop 
for i in 'saya pandai':
    if(i=='a'):
        pass
    else:
        print(i)
        
        
#Range in Loop
for i in range(0,21,3): #range(awal, akhir, naik brp step)
    print(i)

#Generate list dengan range
angka_3 = print(list(range(1,11)))

#Fungsi Enumarate
kata ='abcdefghij'
for i in enumerate(kata) :
    print(i)
    
for a,b in enumerate(kata) :
    print(a)
    print(b)
    
#Zip function
list1= [1,2,3,4,5]
list2= ['a', 'b', 'c', 'd', 'e']
list3= [100,200,300,400,500]
for i in zip(list1,list2, list3):
    print(i)
    
list(zip(list1, list2, list3))

#Item Checking : Mengecek apakah ada item tersebut di dalamnya
'v' in 'aku belajar'
kotak1 = {'a' : 100, 'b' : 200, 'c':300}
'a' in kotak1

#Mengecek values di dictionaries
200 in kotak1.values()

#Advance for loops
#Cara1
isi = list(range(1,11))
#Cara 2
isi2=list()
for i in range(1,11):
    isi2.append(i)
isi2
#Cara3
isi3 = [i for i in range(1,11)]
isi3
#Cara4
isi4 = [(i**2/2) for i in range(1,11)]
isi4
#memasukkan if dalam loop
isi5 = [i for i in range(1,11)if i%2==0] #hanya angka genap saja
isi5
#menambhakan else pada loop
isi6 = [i if i%2==0 else 'ganjil' for i in range(1,11)]
isi6
#cara lain if else
isi7 = []
for i in range(1,11):
    if i%2==0:
        isi7.append(i)
    else:
        isi7.append('Ganjil')
isi7

#Function
def cetak_kalimat():
    print('ternyata belajar python itu mudah!')
cetak_kalimat()    

#contoh lain : menambahkan variabel dengan fungsi
list1 = list(range(1,11))
list1.append(12)
list1

#Fungsi dengan return
def perkalian(a,b):
    return(a*b)
kali = perkalian(7, 9)
kali
type(kali)

def perkalian(a,b):
    print(a+b)
jumlah = perkalian(7, 9)
jumlah #Beda print dengan return, jika return fungsi dr kali akan melekat dan akan memiliki type data. namun jika print tidak
type(jumlah)

#Default Function
def belajar(var='Python'):
    print('Saya sedang belajar' + var)
belajar(' Matematika')

def belajar(var=' Python'):
    print('Saya sedang belajar' + var)
belajar() #Akan menampilkan hasil deafult

#Deteksi Ganji-Genap dengan function
def ganjil_genap(a):
    if(a%2==0):
        print("genap")
    else:
        print("ganjil")
ganjil_genap(3)
ganjil_genap(4)

#Latihan Fungsi
def cek_kalimat (var):
    if 'Python' in var:
        return True
    else:
        return False

cek_kalimat('Saya suka Python')

#Cara Lain
def cek_kalimat(var):
    return 'Python' in var
cek_kalimat('Python')

#Args : Kita bisa memasukkan banyak variabel tanpa mendefinisikan banyak variabel
def jumlah(*args):
    return sum((args))
jumlah(1,2,3,4,5)

#Sum in tuple
sum((1,2,3,4))
#sum in List
sum([1,2,3])

#Another Args : Hasil dari Args adalah tuple
def cek_args(*args):
    print(args)
cek_args(1,2,3,4)

#kwargs : Hasil dari kwargs akan menjadi dictionary
def cek_kwargs(**kwargs):
    print(kwargs)
cek_kwargs(anak=86)
 
#Another Example
def cek_berat (**kwargs):
    if 'Budi' in kwargs:
        print('Berat Budi tergolong ke katergori{}'.format(kwargs['Budi']))
    else:
        print('Budi tidak ada di database')
cek_berat(Budi=' kurus', Joko = ' gemuk')        

#Menggabungkan fungsi args dan kwargs
def fungsiku (*args, **kwargs):
    print('Saya ingin membeli {} {} secara tunai'.format(args[1], kwargs['makanan']))
fungsiku(23,56,10, buah='apel', makanan = 'sate')

'''
Urutan Eksekusi Python :
    L(Local) : variabel ini bersifat lokal, yang biasanya berada di dalam fungsi(def)/lambda
                tertentu.
    E(Enclosing function Local) : variabel ini berada di dalam fungsi (def/lambda)
            mulai dari lingkup terdalam hingga keluar.
    G(Global) : Variabel ini diddefinisikan diluar, biasanya di tahap awal
    B(Built-in) : variabel bawaan python seperti list, str, upper dll
'''

#LEGB
kalimat = "saya adalah global"
def cetak():
    kalimat = 'saya adalah local'
    def eksekusi():
        print('Halo hasilnya adalah ' + kalimat)
    
    eksekusi()
cetak()

#Contoh Lain
angka =99
def tulis (angka):
    print(f'Angka={angka}') #akan sama dengan print('Angka = {}'.format{angka})
tulis(angka)
#Another Example
angka =99
def tulis (angka):
    print(f'Angka={angka}') #akan sama dengan print('Angka = {}'.format{angka})
#Mendefinisikan ulang sebuah variabel global di fungsi
angka =300
print(f'Angkanya sekarang saya ubah menjadi{angka}')
tulis(angka)
print(angka)

#Map function pakai cara for loop
def kali10(num):
    return num*10
angka = [30,60,90]
for item in map(kali10,angka):
    print(item)
#Map function with map dirctly
list(map(kali10,angka))
#Map in tuple
angka = (10,20,30)
tuple(map(kali10,angka))

#function with string
def jumlah_kata(kata):
    if len(kata)%2==0:
        return('Genap')
    else:
        return('Ganjil')
jumlah_kata('akdkiasnciascs')

berat_murid = [45,55,60,40,80,101,92,77]
for i in (berat_murid):
    if berat_murid > 100:
       print("overweight")
    elif berat_murid[i] < 60:
       print("murid ke "+i+" terlalu kurus")
    elif berat_murid[i] == 60:
       print("murid ke "+i+" beratnya tepat 60")
    else:
       print("murid ke "+i+" ideal")

