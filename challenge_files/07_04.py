class Shape:
    width = 5
    height = 5
    printChar = "#"

    def printRow(self, i):
        raise NotImplementedError(
            "Will be implemented by children extending this class"
        )

    def print(self):
        print(
            f"{self.__class__.__name__}, width = {self.width}, height = {self.height}"
        )
        for i in range(self.height):
            self.printRow(i)
        print("")


class Square(Shape):
    def printRow(self, i):
        print(self.printChar * self.width)


class Triangle(Shape):
    def printRow(self, i):
        print(self.printChar * (i + 1))


class Triangle2(Shape):
    width = Shape.height * 2
    spaceChar = " "

    def printRow(self, i):
        printWidth = (2 * i) + 1
        spaceWidth = int(self.width / 2) - i
        print(self.spaceChar * spaceWidth + self.printChar * printWidth)


class Triangle3(Shape):
    spaceChar = " "

    def printRow(self, i):
        spaceWidth = int((self.width - i - 1) / 2)
        if i % 2 == 1:
            spaceWidth = spaceWidth + 1
        printWidth = i + 1
        if printWidth % 2 == 0:
            printWidth = printWidth - 1
        print(self.spaceChar * spaceWidth + self.printChar * printWidth)


s = Square()
t1 = Triangle()
t2 = Triangle2()
t3 = Triangle3()

s.print()
t1.print()
t2.print()
t3.print()

t4 = Triangle3()
t4.width = 11
t4.height = 11
t4.print()
