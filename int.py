# Data input
data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit"
]

# Fungsi untuk memfilter hanya nilai integer dari string
def filter_integers(text):
    return ''.join(filter(str.isdigit, text))

# Menggunakan filter untuk mengambil hanya nilai integer dari setiap data
filtered_data = [filter_integers(d) for d in data]

# Memisahkan nilai integer menjadi list berisi angka-angka
split_data = [list(filtered) for filtered in filtered_data]

print(split_data)