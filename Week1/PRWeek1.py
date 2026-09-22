Nama_Barang = input("Masukkan Nama Barang:")
Harga_Barang = float(input("Masukkan Harga Barang:"))
Quantity = int(input("Masukkan Jumlah Barang:"))

subtotal = Harga_Barang * Quantity

if subtotal >= 100000:
    persen_diskon = 0.10
else:
    persen_diskon = 0.0
    
nilai_diskon = subtotal * persen_diskon
total = subtotal - nilai_diskon

print("Rincian Pembayaran")
print(f"Subtotal:{subtotal}")
print(f"Diskon:{nilai_diskon}")
print(f"Total:{total}")

payment = float(input("Masukkan Payment:"))

if payment < total:
    print("Payment tidak cukup")
else:
    kembalian = payment - total
    print("Kembalian")
    #Arul