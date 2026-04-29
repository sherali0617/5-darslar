import os 
os.system("cls")


# cars ={
#     "Spark":12000,
#     "Malibu":35000,
#     "Cobolt":28000,
#     "Tracker":28000
# }
# mx=0
# a=""
# mn=cars["Spark"]
# b="Spark"
# for i,j in cars.items():
#     if mx<j:
#         mx=j
#         a=i
# for i,j in cars.items():
#     if mn>j:
#         mn=j
#         b=i
# print("max:",a,mx)
# print("min:",b,mn)
# s=0
# for i,j in cars.items():
#     s=j+s
# print("ortachasi",s/4)


# 2.m
# movies = {
#     "Titanic": 1997,
#     "Avatar": 2009,
#     "Inception": 2010,
#     "Interstellar": 2014
# }

# for i,j in movies.items():
#     if j>2000:
#         print(i)


# 3.m
# speed = {
#     "Tesla": 250,
#     "BMW": 240,
#     "Mercedes": 260,
#     "Audi": 230
# }

# a=list(speed.values())
# a.sort()
# a=a[::-1]
# for i in a:
#     for j,s in speed.items():
#         if i==s:
#             print(f"{j}:{s}")


# 4.m
# user=input("User:")

# professions = {
#     "Doston": "Dasturchi",
#     "Cristiano Ronaldo": "Futbolchi",
#     "Elon Musk": "Tadbirkor",
#     "Messi": "Futbolchi"
# }
# b=professions.get(user)

# if user not in professions:
#     print("Bunday user yoq!!")
# if professions[user]==b:
#     print(b)


professions = {
    "Bill Gates": "Dasturchi",
    "Cristiano Ronaldo": "Futbolchi",
    "Elon Musk": "Tadbirkor",
    "Messi": "Futbolchi"
}
a = input("Ism kriting: ")

b = professions.get(a)

if b:
    print(f"{a}ning kasbi {b}")
else:
    print("Bunday ism yoq?")


# 5.m
# car_count = {
#     "Chevrolet": 120,
#     "Toyota": 95,
#     "BMW": 60,
#     "Kia": 75
# }

# a= list(car_count.values())

# d = max(a)
# s = min(a)


# for i,j in car_count.items():
#     if j == d:
#         print("Eng kop sotilgani: ",i)
#     if j == s:
#         print("Eng kam sotilgani: ",i)
        

    

       