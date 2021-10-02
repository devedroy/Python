Dict = {1:'Geeks', 2:'For', 3:'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

Dict = {'Name':'Geeks', 1:[1, 2, 3, 4]}
print("Dictionary with Mixed Keys: ")
print(Dict)

Dict = {}
print("Empty Dictionary: ")
print(Dict)

Dict = dict({1:'Geeks', 2:'For', 3:'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)

Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as pair: ")
print(Dict)

Dict = {1:'Geeks', 2:'For', 3:{'A':'Welcome', 'B':'To', 'C':'Geeks'}}
print(Dict)

Dict = {}
print("Empty Dictionary: ")
print(Dict)

Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("Dictionary after adding 3 elements: ")
print(Dict)

Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: " )
print(Dict)

Dict[5] = {'Nested':{'1':'Life', '2':'Geeks'}}
print("\nAdding nested key: ")
print(Dict)

print(Dict[5])
print("\nAccessing a element using get: ")
print(Dict.get(5))

#Accessing a element of a nested dictionary
print(Dict[5]['Nested'])

#Using del Keyword
del Dict[0]
print("\nDeleting a specific key: ")
print(Dict)

#Deleting a key from nested Dictionary
del Dict[5]['Nested']
print("\nDeleting a key from nested Dictionary: ")
print(Dict)

#Using pop() method
pop_ele = Dict.pop(2)
print("\nDictionary after deleteion: "+ str(Dict))
print("value associated with poped key is: "+ str(pop_ele))

#Using popitem() method
pop_ele = Dict.popitem()
print("\n Dictionary after deletion: "+ str(Dict))
print("The arbitrary pair returneed is : "+ str(pop_ele))

#Using clear() method
Dict.clear()
print("\nDeleting Entire Dictionary: ")
print(Dict)
