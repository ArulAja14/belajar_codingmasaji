# def get_greeting():
    # return "Halo, Arul!"
# message = get_greeting()
# print(message)

# def kalkulasi(price,quantity):
#     hasil = price * quantity
#     return hasil

# Total = kalkulasi(12000, 2)
# print(Total)

def diskon(harga,persen):
    potongan = harga * (persen / 100)
    hasil = harga - potongan
    return hasil

total = diskon(100000, 10)
print(total)
#Arul