print("\(^o^)/ selamat datang di kalkulator sederhana \(^o^)/")
print("masukkan angka yang kalian inginkan")
print("kemudian jalankan sesuai dengan arahan ")

variabel1 = int(input("masukan angka pertama : "))
variabel2 = int(input("masukan angka kedua : "))
operator = input("masukan operator(+,*,/,-) : ")
hasil = 0
if operator == "+":
        hasil = variabel1+variabel2
elif operator == "-":
        hasil = variabel1-variabel2
elif operator == "*":
        hasil = variabel1*variabel2
elif operator == "/":
        hasil = variabel1/variabel2
else:
        print("operator tak diketahui")

print("hasil :",hasil)