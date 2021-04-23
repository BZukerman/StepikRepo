# Решение Максима Маслина:
# https://github.com/mxmaslin/stepik/blob/master/Python%20-%20%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D1%8B%20%D0%B8%20%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5/3.7%20XML%2C%20%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20ElementTree%2C%20%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20lxml%204.md
# Данные для проверки:
# Denis Bulaev
# <cube color="blue"><cube color="red"><cube color="green"><cube color="green"><cube color="green"><cube color="blue"></cube><cube color="green"></cube><cube color="red"></cube></cube></cube></cube></cube><cube color="red"><cube color="blue"></cube></cube></cube>
# red = 10(2, 6, 2);  green = 18(3, 4, 5, 6);   blue = 10(1, 6, 3)
# Stepik:
# <cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>
# red: 4    green: 3    blue: 1
#
from xml.etree.ElementTree import XMLParser

xml = input()

class ColorWeights:                    # The target object of the parser
    depth = 0
    weights = {'red': 0, 'green': 0, 'blue': 0}

    def start(self, tag, attrib): # Called for each opening tag.
        self.depth += 1
        self.add_weight(attrib)

    def add_weight(self, attrib):
        self.weights[attrib['color']] += self.depth

    def end(self, tag):           # Called for each closing tag.
        self.depth -= 1

    def data(self, data):
        pass                      # We do not need to do anything with data.

    def close(self):              # Called when all data has been parsed.
        global weights_list       # Added by me to transfer output row

        weights_list = [self.weights['red'], self.weights['green'], self.weights['blue']]
        return ' '.join(list(map(str, weights_list)))

target = ColorWeights()
parser = XMLParser(target=target)
parser.feed(xml)
print(parser.close())
#
# print(weights_list)
#
# print("red =", weights_list[0], "green =", weights_list[1], "blue =", weights_list[2])