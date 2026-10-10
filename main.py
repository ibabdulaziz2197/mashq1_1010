# 15
numbers = [4, 7, 12, 15, 20, 9, 8]

juft_sonlar = [son for son in numbers if son % 2 == 0]

print(juft_sonlar)


# 16
numbers = [4, 7, 12, 15, 20, 9, 8]

juft_sonlar = [son for son in numbers if son % 2 == 0]

print(juft_sonlar)

# 17
fruits = ["olma", "banan", "anor"]
fruits.append('uzum')
print(fruits)

# 18
colors = ["qizil", "yashil", "ko‘k", "sariq"]
colors.remove('ko‘k')
print(colors)

# 19
numbers = [17, 4, 25, 9, 12, 2]
numbers.sort()
print(numbers)

# 20
animals = ("mushuk", "it", "ot", "quyon")

for animal in animals:
    print(animal)


# 21
cities = ("Toshkent", "Samarqand", "Xiva", "Buxoro")

shahar = input("Shahar nomini kiritng: ")

if shahar in cities:
    print("Shahar tuple ichda mavjud")

else:
    print("Shahar tuple ichda majud")

# 22
numbers = (5, 10, 15, 20, 25, 30)

soni = len(numbers)

print("Elementlar soni:", soni)

# 23
ism = "Ali"
yosh = 15
sinf = 9

student = {
    "ism": ism,
    "yosh": yosh,
    "sinf": sinf
}

print(student)



# 24
student = {
    "ism": "Sardor",
    "yosh": 16,
    "sinf": 10
}

print(student["ism"])

# 25
car = {
    "model": "Cobalt",
    "yil": 2023
}

car["rang"] = "oq"

print(car)
