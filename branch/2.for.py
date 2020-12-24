for waiting_no in range(5):  # [0,1,2,3,4]
    print("대기번호: {0}".format(waiting_no))

for waiting_no in range(1, 6):  # [1,2,3,4,5]
    print("대기번호: {0}".format(waiting_no))

nums = [0, 1, 2, 3, 4]
for waiting_no in nums:
    print("대기번호: {0}".format(waiting_no))

students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)
