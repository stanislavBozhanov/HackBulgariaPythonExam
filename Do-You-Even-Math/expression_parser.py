class ExpressionParser():
    def __init__(self, filename):
        self.filename = filename

    def get_lines(self):
        content = open(self.filename).read()
        return content.split('\n')

    def get_expressions_data(self, lines):
        data = []
        for line in lines:
            line = line.split(' ')
            data.append([int(line[0]), line[1], int(line[2]), 0])
        return data

    def plus(self, x, y):
        return x + y

    def minus(self, x, y):
        return x - y

    def power(self, x, y):
        return x ** y

    def muliply(self, x, y):
        return x * y

    def divide(self, x, y):
        return round(x / y, 2)

    def get_expressions_answers(self, data):
        for item in data:
            if item[1] == '+':
                item[3] = self.plus(item[0], item[2])
            elif item[1] == '-':
                item[3] = self.minus(item[0], item[2])
            elif item[1] == '^':
                item[3] = self.power(item[0], item[2])
            elif item[1] == '*':
                item[3] = self.muliply(item[0], item[2])
            elif item[1] == '/':
                item[3] = self.divide(item[0], item[2])
            else:
                print('Wrong operator')
        return data

    def do_math(self):
        lines = self.get_lines()
        data = self.get_expressions_data(lines)
        data = self.get_expressions_answers(data)
        return data
