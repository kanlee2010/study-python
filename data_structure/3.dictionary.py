cabinet = {3: "유재석", 100: "김태호", "A-3": "손님"}
print(cabinet[3])  # overrun 하면 종료됨
print(cabinet.get(100))  # overrun 하면 None 반환
print(cabinet.get(5, "비어있음"))
print(cabinet.get("A-3"))
print(cabinet.items())
print(3 in cabinet)
print(5 in cabinet)
cabinet["A-3"] = "조세호"
print(cabinet)
del cabinet["A-3"]
print(cabinet)
print(cabinet.keys())
print(cabinet.values())
cabinet.clear()
print(cabinet)
