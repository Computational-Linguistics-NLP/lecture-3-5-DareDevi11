text = input()
length = len(text)
match length:
    case _ if length <= 2:
        print("чудовищно мало")
    case _ if 2 < length <= 5:
        print("очень мало")
    case _ if 5 < length <= 10:
        print("мало")
    case _ if 10 < length <= 30:
        print("ок")
    case _ if 30 < length <= 100:
        print("много")
    case _:
        print("чудовищно много")
