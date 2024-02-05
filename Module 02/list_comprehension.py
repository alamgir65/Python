arr = [17,578,97,67,65,45,90,85]
odds = []
for x in arr:
    if x % 2 == 1 and x % 5 == 0:
        odds.append(x)

print(odds)

odds2 = [x for x in arr if x % 2==1 and x % 5 == 0]
print(odds2)


players = ['Shakib','Mushfique','Tamim']
ages = [38,39,35]
comb = []
for player in players:
    for age in ages:
        comb.append([player,age])
print(comb)

comb2 = [[player,age] for player in players for age in ages]
print(comb2)