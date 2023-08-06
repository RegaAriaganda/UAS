def selection_sort(data):
    n = len(data)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if data[j][0] < data[min_index][0]:
                min_index = j

        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]

data = [
    ["Fahmi", "Jakarta"],
    ["Romi", "Solo"],
    ["Andri", "Jakarta"],
    ["Fadillah", "Banyuwangi"],
    ["Ruli", "Bandung"],
    ["Rudi", "Bali"],
    ["Dendi", "Purwokerto"],
    ["Zaki", "Madiun"]
]

print("Data sebelum diurutkan:")
print("Nama\tAlamat")
for item in data:
    print(item[0] + "\t" + item[1])

selection_sort(data)

print("\nData setelah diurutkan (Selection Sort):")
print("Nama\tAlamat")
for item in data:
    print(item[0] + "\t" + item[1])
