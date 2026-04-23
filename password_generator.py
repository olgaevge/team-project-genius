import random

a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
b = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
c = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
d = ["", "", "", "", "", ""]

while True:
    try:
        digit = int(
            input("Выберите из скольки цифр должен состоять пароль (6, 9 или 12) ")
        )

        if digit == 6:
            password = "".join(random.sample(a, 6))
            print(password)
            break
        elif digit == 9:
            password = "".join(
                random.sample(c, 3) + random.sample(b, 3) + random.sample(a, 3)
            )
            print(password)
            break
        elif digit == 12:
            password = "".join(
                random.sample(c, 3)
                + random.sample(d, 1)
                + random.sample(b, 3)
                + random.sample(a, 3)
                + random.sample(d, 1)
            )
            print(password)
            break
        else:
            print("Такого варианта ответа нет. Введите число еще раз.")

    except ValueError:
        print("Ошибка: введите целое число!")
