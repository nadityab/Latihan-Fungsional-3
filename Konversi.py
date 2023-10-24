# Fungsi pertama untuk mengkonversi minggu ke hari
def minggu_ke_hari(minggu):
    def inner(hari):
        def inner2(jam):
            def inner3(menit):
                return (minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit
            return inner3
        return inner2
    return inner

# Data input
data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit"
]

# Mengkonversi data input menjadi jumlah total menit dengan metode currying
output_data = []
for d in data:
    components = d.split()
    minggu = int(components[0])
    hari = int(components[2])
    jam = int(components[4])
    menit = int(components[6])
    
    total_menit = minggu_ke_hari(minggu)(hari)(jam)(menit)
    output_data.append(total_menit)

print(output_data)