print("\(^o^)/ selamat datang di kalkulator sederhana \(^o^)/")
print("masukkan angka yang kalian inginkan")
print("kemudian jalankan sesuai dengan arahan ")

angka1 = int(input("masukan angka pertama : "))
angka2 = int(input("masukan angka kedua : "))
operator = input("masukan operator(+,*,/,-) : ")
hasil = 0
if operator == "+":
        hasil = angka1+angka2
elif operator == "-":
        hasil = angka1-angka2
elif operator == "*":
        hasil = angka1*angka2
elif operator == "/":
        hasil = angka1/angka2
else:
        print("operator tak diketahui")

print("hasil :",hasil)