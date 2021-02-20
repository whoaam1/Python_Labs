class Squeezer:

    price = "1250 UAH"

    @staticmethod
    def avg_price():
        return Squeezer.price

    def __init__(self, color="missing values", max_number=0, power=0, producer="missing values",
                 volume="missing values", weight=0, name="missing values"):
        self.color = color
        self.maxNumber = max_number
        self.power = power
        self.producer = producer
        self.volume = volume
        self.weight = weight
        self.name = name

    def __del__(self):
        print("Deleting an instance")

    def __str__(self):
        output = ("Color: " + self.color + "\nMaximum number(L in hour): " + str(self.maxNumber) + "\nPower(кВт): "
                + str(self.power) + "\nProducer: " + str(self.producer) + "\nVolume(L): " + str(self.volume)
                + "\nWeight(kg): " + str(self.weight) + "\nName: " + str(self.name))
        return output
