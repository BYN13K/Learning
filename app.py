high = 1200
core = 400
width = 1800
cable = 25

# reserve1 = (high - 2 * cable)
# reserve15 = (high - 3 * cable)
# reserve2 = (high - 4 * cable)
# reserve3 = (high - 6 * cable)

# no_cap = ((0.7854 * (high ** 2 - core ** 2) * width) / (1000 * (cable * cable)))
# capacity1 = ((0.7854 * (reserve1 ** 2 - core ** 2) * width) / (1000 * (cable * cable)))
# capacity15 = ((0.7854 * (reserve15 ** 2 - core ** 2) * width) / (1000 * (cable * cable)))
# capacity2 = ((0.7854 * (reserve2 ** 2 - core ** 2) * width) / (1000 * (cable * cable)))
# capacity3 = ((0.7854 * (reserve3 ** 2 - core ** 2) * width) / (1000 * (cable * cable)))

class capacity():

    def __init__(self, high, core, width, cable):
        self.high = high
        self.core = core
        self.width = width
        self.cable = cable
    
    def cap(self):

        return ((0.7854 * (self.high ** 2 - self.core ** 2) * self.width) / (1000 * (self.cable ** 2)))

    def cap1(self):
        reserve1 = (self.high - 2 * self.cable)
        return ((0.7854 * (reserve1 ** 2 - self.core ** 2) * self.width) / (1000 * (self.cable ** 2)))

    
    def cap15(self):
        reserve15 = (self.high - 3 * self.cable)
        return ((0.7854 * (reserve15 ** 2 - self.core ** 2) * self.width) / (1000 * (self.cable ** 2)))


    def cap2(self):
        reserve2 = (self.high - 4 * self.cable)
        return ((0.7854 * (reserve2 ** 2 - self.core ** 2) * self.width) / (1000 * (self.cable ** 2)))


    def cap3(self):
        reserve3 = (self.high - 6 * self.cable)
        return ((0.7854 * (reserve3 ** 2 - self.core ** 2) * self.width) / (1000 * (self.cable ** 2)))


capa = capacity(high, core, width, cable)

print(capa.cap1())

