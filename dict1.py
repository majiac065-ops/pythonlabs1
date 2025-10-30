dict1 = {'a' : 1, 'b' : 2}
print("Dictionary 1:", dict1)
dict2 = {'c' : 3, 'd' : 4}
print("Dictionary 2:",  dict2)
merged_dict=dict1.copy()
merged_dict.update(dict2)
print("Merged Dictionary:", merged_dict)


