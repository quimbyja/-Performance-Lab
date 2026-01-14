import sys

class Ellipse:
    def __init__(self):
        self.ellipse_file = sys.argv[1]
        self.dots_file = sys.argv[2]


    def read_ellipse(self):
        with open(self.ellipse_file, "r", encoding="utf-8") as file:
            lines = file.readlines()
        line1 = lines[0].strip()
        line2 = lines[1].strip()

        x0, y0 = map(float, line1.split())
        a, b = map(float, line2.split())

        return x0, y0, a, b

    def read_dots(self):
        dots = []
        with open(self.dots_file, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                x, y = map(float, line.split())
                dots.append((x, y))
        return dots

    def dots_in_space(self, x, y, x0, y0, a, b):
        s = ((x - x0) ** 2) / (a ** 2) + ((y - y0) ** 2) / (b ** 2)

        if abs(s - 1.0) < 1e-9:
            return "0 - точка лежит на окружности"
        elif s < 1.0:
            return "1 - точка внутри"
        else:
            return "2 - точка снаружи"

    def run(self):
        x0, y0, a, b = self.read_ellipse()
        dots = self.read_dots()

        for x, y in dots:
            position = self.dots_in_space(x, y, x0, y0, a, b)
            print(position)


if __name__ == "__main__":
    ellipse = Ellipse()
    ellipse.run()
