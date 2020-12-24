import sys
from random import *
from typing import ByteString

num = 4
b = True
s = "good"
print("this" + s + str(num) + str(b))
print("this", s, num, b)  # 인자 사이 한칸 띄우기
print("%s %d" % ("this", num), s, b)
print("{1} {0}".format("this", num), s, b, end=" ")  # "\n"을 " "로 교체
print("{s} {n}".format(s="this", n=num), s, b)
print(int(0.83 * 10))

print(random() * 10)
print(randrange(1, 46))
print(randint(1, 45))

# slicing
jumin = "990120-1234567"
print("성별: " + jumin[7])
print("연도: " + jumin[0:2])
print("생년월일: " + jumin[:6])
print("뒤7자리: " + jumin[-7:])

# 문자열
string = "Python is Amazing"
print(string.lower())
print(string.upper())
print(string[0].isupper())
print(len(string))
print(string.replace("Python", "Java"))
index = string.index("n")
print(index)
index = string.index("n", index+1)
print(index)
print(string.find("n"))
print(string.find("Unknown"))
print(string.count("n"))

print("Python", "Java", sep=" vs ", end="??")
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).zfill(3).rjust(4), sep=":")
