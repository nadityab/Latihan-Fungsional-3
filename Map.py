list_data = [3.1, "Hello", 1, 2.7, "Python", 55, 7, "world", 3, 71, 4, 12, "AI"]

# Filter untuk memisahkan nilai float, int, dan string
data_float = list(filter(lambda x: isinstance(x, float), list_data))
data_int = list(filter(lambda x: isinstance(x, int), list_data))
data_string = list(filter(lambda x: isinstance(x, str), list_data))

# Map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
def map_to_units(number):
    if isinstance(number, int):
        satuan = number % 10
        puluhan = (number // 10) % 10
        ratusan = number // 100
        return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}
    else:
        return number

data_int_mapped = list(map(map_to_units, data_int))

# Output
print("Data Float:", data_float)
print("Data Int:")
for item in data_int_mapped:
    print(item)
print("Data String:", data_string)
