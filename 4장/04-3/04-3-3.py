f = open('abc.txt', 'r')
lines = f.readlines()  # 모든 라인을 읽음
f.close()

rlines = reversed(lines)  # 읽은 라인을 역순으로 정렬

f = open('abc.txt', 'w')
for line in rlines:
    line = line.strip()  # 포함되어 있는 줄바꿈 문자 제거
    f.write(line)
    f.write('\n')  # 줄바꿈 문자 삽입
f.close()
