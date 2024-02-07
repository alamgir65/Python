# we used labda to write any function in shortcut or one line

double_it = lambda x : 2*x
add = lambda a,b,c : a+b+c
powerd = lambda x,p : x**p

# print(double_it(99))
# print(add(81,15,73))
# print(powerd(3,3))

# map -> amra akta list er sob gula element er upor kono operation korte chaile map use korte pari
arr = [8,84,174,14,654,25,6,2]
# print(arr)
d_arr = map(double_it,arr)
#print korte hole aita ke list a convert kore nite hobe
# print(list(d_arr))

dd_arr = map(lambda x: 10*x , arr)
# print(list(dd_arr))


#uses of filter
actors = [
    {'Name' : 'Bhubli' , 'age' : 30},
    {'Name' : 'Opu' , 'age' : 38},
    {'Name' : 'Phurnima' , 'age' : 47},
    {'Name' : 'Bhobita' , 'age' : 50},
    {'Name' : 'Pakhi' , 'age' : 22},
]

juniors = filter(lambda actor : actor['age'] < 35 ,actors)
seniors = filter(lambda actor : actor['age'] >= 35 ,actors)
# print(list(juniors))
print(list(seniors))


