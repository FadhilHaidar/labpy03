from random import random

# Meminta input nilai n dari pengguna
n = int(input("Masukkan nilai N: "))

# Menampilkan n bilangan acak yang kurang dari 0.5
for i in range(n):
    bilangan_acak = random()
    if bilangan_acak < 0.5:
        print(f"Data ke-{i + 1} => {bilangan_acak}")
print("Selesai")
