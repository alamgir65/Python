person = {'Name':'Alamgir','Age':22,'Adress': 'Naokhali', 'Ex' : 'Fayeza'}
print(person)
print(person.keys())
print(person.values())
person['job'] = 'Facebooker'
print(person)
print(person['Ex'])

for key,value in person.items():
    print(f"key -> {key} : value -> {value}")