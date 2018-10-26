num= input("숫자를 입력하세요:")
numbers=num.split(",")
total=0
for n in numbers:
    total+=int(n)

print(total)
