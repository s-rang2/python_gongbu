a=[1,[2,3],4]
b=a[:]
a[1][0]=5
print(a)
print(b)
#해설: 1dept(깊이)까지 copy해주지만 2depth이상의 리스트는 coppy를 못해줌
#그래서 서로 다른객체지만 2depth는 서로 같은 곳을 바라보게
