score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
score_file.write("영어 : 50")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="")
print(score_file.readline())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line)
score_file.close()

with open("score.txt", "r", encoding="utf8") as score_file:
    print(score_file.read())
