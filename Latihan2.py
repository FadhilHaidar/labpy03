# Modal awal
modal_awal = 100000000

# List laba untuk setiap bulan
laba_bulan = [0, 0, 0.1 * modal_awal, 0.1 * modal_awal, 0.5 * modal_awal, 0.5 * modal_awal, 0.5 * modal_awal, 0.2 * modal_awal]

# Menampilkan laba per bulan
total_laba = 0
for i in range(len(laba_bulan)):
    print(f"Laba bulan ke-{i + 1} sebesar: {laba_bulan[i]}")
    total_laba += laba_bulan[i]

# Tampilkan total laba
print(f"Total laba adalah: {total_laba}")
