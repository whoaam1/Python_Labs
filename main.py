from lab1 import Squeezer


def main():
    object1 = Squeezer("Black", "6", "0.8")
    print(object1.__str__())
    print(f"Price: {object1.avg_price()} \n")

    object2 = Squeezer("Silver", "5", "0.4", "Made in USA", "1")
    print(object2.__str__())
    print(f"Price: {object2.avg_price()} \n")

    object3 = Squeezer("White", "3", "0.6", "Made in Tokyo", "1.5", "3")
    print(object3.__str__())
    print(f"Price: {object3.avg_price()} \n")


if __name__ == '__main__':
    main()
