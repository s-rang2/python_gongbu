def function(*args):
    result=0
    for i in args:
        result+=i
    return result/len(args)

print(function(1,2))
print(function(1,2,3,4,5))
