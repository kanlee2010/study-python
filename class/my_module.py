def price(people):
    print(people, "명 가격은", people*10000, "원 입니다")


if __name__ == "__main__":
    print("모듈을 직접 실행하는 경우")
    price(10)
else:
    print("외부에서 모듈 호출")
