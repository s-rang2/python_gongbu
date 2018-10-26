data = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
result={}
for type in data:
    if type in result:
        result[type]+=1
    else:
        result[type]=1
print(result)
