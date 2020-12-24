def open_account(name):
    print(name + "의 새로운 계좌 생성")
    return name


def profile(name, age=17, main_lang="Korean"):
    print("이름: {0}\t 나이: {1}\t 언어: {2}"
          .format(name, age, main_lang))


open_account("토르")
profile("토르", 29, "English")
profile("토르", main_lang="English", age=20)
profile("홍길동")


def vprofile(name, age, *language):
    print("이름: {0}\t 나이: {1}\t 언어:"
          .format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


vprofile("토르", 29, "English", "Korean", "Nordish")
