def bubble_sort(data):
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j][0] > data[j + 1][0]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True

        if not swapped:
            break

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

bubble_sort(data)

print("\nData setelah diurutkan (Bubble Sort):")
print("Nama\tAlamat")
for item in data:
    print(item[0] + "\t" + item[1])
