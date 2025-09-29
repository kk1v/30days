#Day 6
#Level 1
t1 = ()

sisters = ("Kristina", "Alina")
brothers = ("Andrei", "Sawa")
siblings = sisters + brothers
print(siblings)

print(len(siblings))

siblings = list(siblings)
parents = ("Larissa", "Vladimir")
siblings.extend(parents)
siblings = tuple(siblings)
print(siblings)

#Level 2

family_members = siblings
print(family_members)

fruits = ("apple", "banana", "orange")
vegetables = ("carrot", "beans", "potatoes")
animals = ("dog", "cat", "elephant")
food_stuff_tp = fruits + vegetables + animals
print(food_stuff_tp)

food_stuff_tp = list(food_stuff_tp)
print(food_stuff_tp)

del food_stuff_tp[len(food_stuff_tp) // 2 : len(food_stuff_tp) // 2 + 2]
print(food_stuff_tp)

del food_stuff_tp[:3]
del food_stuff_tp[1:]
print(food_stuff_tp)

food_stuff_tp.clear()
food_stuff_tp = tuple(food_stuff_tp)
print(food_stuff_tp)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)