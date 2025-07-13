d={'alice': 85, 'bob': 55, 'charlie': 90}
n = input('Enter student name: ')
if n.lower() in d:
    print("{}'s marks: {}".format(n, d[n.lower()]))
else:
    print("student not found.")