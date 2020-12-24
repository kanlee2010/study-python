class BigNumErr(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    num1 = int(input("첫번째 숫자 : "))
    num2 = int(input("두번째 숫자 : "))
    print(num1, " / ", num2, " = ", int(num1/num2))
    if num1 > 10:
        raise BigNumErr("입력값: {}".format(num1))
except ValueError:
    print("에러 입력 오류")
except ZeroDivisionError as err:
    print("0으로 나눌 수 없습니다")
    print(err)
except BigNumErr as err:
    print("큰 수 입니다")
    print(err)
except Exception as err:
    print("알수 없는 오류: ", err)
finally:
    print("계산기 종료")
