# Класс неравенства
class Inequality:
    def __init__(self, a: str, b: str, c: str, step_discriminant: bool, sign_of: str):
        # Очищаем от пробелов
        a, b, c = a.replace(' ', ''), b.replace(' ', ''), c.replace(' ', '')

        # Проверяем коэффициенты содержание только чисел, если есть другие символы, то вызываем ошибку
        if not ((a.replace('.', '').replace('-', '').isdigit() or a == '')
                and (b.replace('.', '').replace('-', '').isdigit() or b == '')
                and (c.replace('.', '').replace('-', '').isdigit() or c == '')):
            raise TypeError('Ошибка! Коэффициенты должны быть числами')

        # >,<,>=,<= 0
        if sign_of.split(';')[0] == 'more':
            if sign_of.split(';')[1] == 'strict':
                self.s_sgn_of = '>0'
                self.sgn_of = 'more'
            else:
                self.s_sgn_of = '≥0'
                self.sgn_of = 'more_or_equals'
        else:
            if sign_of.split(';')[1] == 'strict':
                self.s_sgn_of = '<0'
                self.sgn_of = 'less'
            else:
                self.s_sgn_of = '≤0'
                self.sgn_of = 'less_or_equals'

        # Коэффициенты
        # Инициализируем коэфф-ты
        self.a, self.b, self.c = (float(a) if a != '' else 1.0,
                                  float(b) if b != '' else 1.0,
                                  float(c) if c != '' else 0.0)

        # Преобразование коэффициентов в строку
        # 1 коэфф.
        if a == '0':
            raise ArithmeticError('Ошибка! Коэффициент а не может быть равен 0')
        elif self.a == 1:
            self.s_a = 'x²'
        elif self.a == -1:
            self.s_a = '-x²'
        else:
            self.s_a = a + 'x²'
        # 2 коэфф.
        if self.b == 1:
            self.s_b = '+x'
        elif self.b == -1:
            self.s_b = '-x'
        elif self.b == 0:
            self.s_b = ''
        elif self.b > 0:
            self.s_b = '+' + b + 'x'
        else:
            self.s_b = b + 'x'
        # 3 коэфф
        if self.c == 0:
            self.s_c = ''
        elif self.c < 0:
            self.s_c = c
        elif self.c > 0:
            self.s_c = '+' + c

        # конечная строка
        self.to_str = self.s_a + self.s_b + self.s_c + self.s_sgn_of

        # добавочные поля
        self.steps, self.stepD = [], step_discriminant  # FOR EXAMPLE !!!!

        # Решение
        self.__solve()

    # Решаем неравенство
    def __solve(self):
        # Если коэффициент a меньше 0
        if self.a < 0:
            # умножаем коэффициенты на -1
            self.a *= -1
            self.b *= -1
            self.c *= -1
            t_str = ''
            idx = 0
            for i in self.to_str:
                if i == '-' and idx != 0:
                    t_str += '+'
                elif i == '-' and idx == 0:
                    pass
                elif i == '+':
                    t_str += '-'
                elif i == '>':
                    t_str += '<'
                    self.sgn_of = 'less'
                elif i == '<':
                    t_str += '>'
                    self.sgn_of = 'more'
                elif i == '≥':
                    t_str += '≤'
                    self.sgn_of = 'less_or_equals'
                elif i == '≤':
                    t_str += '≥'
                    self.sgn_of = 'more_or_equals'
                else:
                    t_str += i
                idx += 1
            self.steps.append(t_str + '; а<0,умножим коэффициенты на -1')
            self.steps.append(t_str.replace('>', '=').replace('<', '=').replace('≥', '=').replace('≤', '='))
        else:
            self.steps.append(self.to_str.replace('>', '=').replace('<', '=').replace('≥', '=').replace('≤', '='))

        # Находим дискриминант
        D = self.b * self.b - 4 * self.a * self.c
        D_str = 'D='
        # Переводим коэффициенты в строки
        self.s_a, self.s_b, self.s_c = [
            str(int(self.a)) if int(self.a) == self.a else str(self.a),
            str(int(self.b)) if int(self.b) == self.b else str(self.b),
            str(int(self.c)) if int(self.c) == self.c else str(self.c),
        ]
        # Если нахождение дискриминанта указывать
        if self.stepD:
            if self.b < 0:
                D_str += f'({self.s_b})'
            else:
                D_str += self.s_b
            if self.c < 0:
                D_str += '²+4*' + self.s_a + '*' + str(-self.c) + '='
            else:
                D_str += '²-4*' + self.s_a + '*' + self.s_c + '='

        if int(D) == D:
            D_str += str(int(D))
        else:
            D_str += str(D)

        if self.stepD:
            D_str += '; найдём дискриминант по формуле D=b²-4ac'
        self.steps.append(D_str)

        # Находим квадратный корень из дискриминанта
        if D >= 0:
            sqrt_D = D ** 0.5
            if sqrt_D == int(sqrt_D):
                sqrt_D = int(sqrt_D)
                if D == int(D):
                    D = int(D)
            self.steps.append('√D=√' + str(D) + '=' + str(sqrt_D))

        # Находим корни
        if D == 0:
            x = -self.b / (2 * self.a)
            if x == int(x):
                x = int(x)
            self.steps.append('x = -b / 2 * a = ' + str(x))
            self.x1, self.x2 = x, x
        elif D > 0:
            x1 = (-self.b + sqrt_D) / (2 * self.a)
            x2 = (-self.b - sqrt_D) / (2 * self.a)
            if x1 == int(x1):
                x1 = int(x1)
            if x2 == int(x2):
                x2 = int(x2)
            self.steps.append('x1 = (-b + √D) / 2 * a = ' + str(x1))
            self.steps.append('x2 = (-b - √D) / 2 * a = ' + str(x2))
            self.x1, self.x2 = x1, x2
        else:
            self.x1, self.x2 = None, None

        # Располагаем корни в порядке возрастания
        if self.x1 is not None and self.x1 > self.x2:
            self.x1, self.x2 = self.x2, self.x1

        # Приводим к виду
        if self.x1 is not None:
            if self.x1 == int(self.x1):
                self.x1 = int(self.x1)
            if self.x2 == int(self.x2):
                self.x2 = int(self.x2)

        # Выводим график
        from colorama import Fore
        w = 0
        if self.x1 is not None:
            w = self.x2 + 1
        else:
            w = 1
        print(Fore.RED + '[LOG] ' + Fore.RESET + '"' + self.sgn_of + '"')
        print(Fore.RED + '[LOG] ' + Fore.RESET + str((self.a * (w * w)) + (self.b * w) + self.c))
        # Если дискриминант больше 0
        if D > 0:
            # больше
            if self.sgn_of == 'more':
                if (self.a * (w * w)) + (self.b * w) + self.c > 0:
                    print(Fore.GREEN + '[CASE] 1.1' + Fore.RESET)
                    self.steps.append('(-∞;' + str(self.x1) + '); (' + str(self.x2) + ';+∞)')
                    self.img = 'img2'
                else:
                    print(Fore.GREEN + '[CASE] 1.2' + Fore.RESET)
                    self.steps.append('(' + str(self.x1) + ';' + str(self.x2) + ')')
                    self.img = 'img2-2'
            # меньше
            elif self.sgn_of == 'less':
                if (self.a * (w * w)) + (self.b * w) + self.c < 0:
                    print(Fore.GREEN + '[CASE] 2.1' + Fore.RESET)
                    self.steps.append('(-∞;' + str(self.x1) + '); (' + str(self.x2) + ';+∞)')
                    self.img = 'img2'
                else:
                    print(Fore.GREEN + '[CASE] 2.2' + Fore.RESET)
                    self.steps.append('(' + str(self.x1) + ';' + str(self.x2) + ')')
                    self.img = 'img2-2'
            # больше или равно
            elif self.sgn_of == 'more_or_equals':
                if (self.a * (w * w)) + (self.b * w) + self.c >= 0:
                    print(Fore.GREEN + '[CASE] 3.1' + Fore.RESET)
                    self.steps.append('(-∞;' + str(self.x1) + ']; [' + str(self.x2) + ';+∞)')
                    self.img = 'img3'
                else:
                    print(Fore.GREEN + '[CASE] 3.2' + Fore.RESET)
                    self.steps.append('[' + str(self.x1) + ';' + str(self.x2) + ']')
                    self.img = 'img3-2'
            # меньше или равно
            elif self.sgn_of == 'less_or_equals':
                if (self.a * (w * w)) + (self.b * w) + self.c <= 0:
                    print(Fore.GREEN + '[CASE] 4.1' + Fore.RESET)
                    self.steps.append('(-∞;' + str(self.x1) + ']; [' + str(self.x2) + ';+∞)')
                    self.img = 'img3'
                else:
                    print(Fore.GREEN + '[CASE] 4.2' + Fore.RESET)
                    self.steps.append('[' + str(self.x1) + ';' + str(self.x2) + ']')
                    self.img = 'img3-2'
        # Если дискриминант равен 0
        elif D == 0:
            # больше
            if self.sgn_of == 'more':
                if (self.a * (w * w)) + (self.b * w) + self.c > 0:
                    print(Fore.GREEN + '[CASE] 1.1' + Fore.RESET)
                    self.steps.append('(-∞;' + str(self.x1) + '); (' + str(self.x2) + ';+∞)')
                    self.img = 'img4-2'
                else:
                    print(Fore.GREEN + '[CASE] 1.2' + Fore.RESET)
                    self.steps.append('Решения нет')
                    self.img = 'img4'
            # меньше
            elif self.sgn_of == 'less':
                if (self.a * (w * w)) + (self.b * w) + self.c < 0:
                    print(Fore.GREEN + '[CASE] 2.1' + Fore.RESET)
                    self.steps.append('Решения нет')
                    self.img = 'img4'
                else:
                    print(Fore.GREEN + '[CASE] 2.2' + Fore.RESET)
                    self.steps.append('Решения нет')
                    self.img = 'img4'
            # больше или равно
            elif self.sgn_of == 'more_or_equals':
                if (self.a * (w * w)) + (self.b * w) + self.c >= 0:
                    print(Fore.GREEN + '[CASE] 3.1' + Fore.RESET)
                    self.steps.append('(-∞;+∞)')
                    self.img = 'img5-2'
                else:
                    print(Fore.GREEN + '[CASE] 3.2' + Fore.RESET)
                    self.steps.append(str(self.x1))
                    self.img = 'img5'
            # меньше или равно
            elif self.sgn_of == 'less_or_equals':
                if (self.a * (w * w)) + (self.b * w) + self.c <= 0 or (self.a * (self.x1 * self.x1)) + (self.b * self.x1) + self.c <= 0:
                    print(Fore.GREEN + '[CASE] 4.1' + Fore.RESET)
                    self.steps.append(str(self.x1))
                    self.img = 'img5'
                else:
                    print(Fore.GREEN + '[CASE] 4.2' + Fore.RESET)
                    self.steps.append('Решения нет')
                    self.img = 'img4'
        # Если дискриминант меньше 0
        else:
            # больше
            if self.sgn_of == 'more':
                if (self.a * (w * w)) + (self.b * w) + self.c > 0:
                    print(Fore.GREEN + '[CASE] 1.1' + Fore.RESET)
                    self.steps.append('(-∞;+∞)')
                    self.img = 'img8-2'
                else:
                    print(Fore.GREEN + '[CASE] 1.2' + Fore.RESET)
                    self.steps.append('Решения нет')
                    self.img = 'img8'
            # меньше
            elif self.sgn_of == 'less':
                if (self.a * (w * w)) + (self.b * w) + self.c < 0:
                    print(Fore.GREEN + '[CASE] 2.1' + Fore.RESET)
                    self.steps.append('Решения нет')
                    self.img = 'img8'
                else:
                    print(Fore.GREEN + '[CASE] 2.2' + Fore.RESET)
                    self.steps.append('Решения нет')
                    self.img = 'img8'
            # больше или равно
            elif self.sgn_of == 'more_or_equals':
                if (self.a * (w * w)) + (self.b * w) + self.c >= 0:
                    print(Fore.GREEN + '[CASE] 3.1' + Fore.RESET)
                    self.steps.append('(-∞;+∞)')
                    self.img = 'img8-2'
                else:
                    print(Fore.GREEN + '[CASE] 3.2' + Fore.RESET)
                    self.steps.append('Решения нет')
                    self.img = 'img8'
            # меньше или равно
            elif self.sgn_of == 'less_or_equals':
                if (self.a * (w * w)) + (self.b * w) + self.c <= 0:
                    print(Fore.GREEN + '[CASE] 4.1' + Fore.RESET)
                    self.steps.append('(-∞;+∞)')
                    self.img = 'img8-2'
                else:
                    print(Fore.GREEN + '[CASE] 4.2' + Fore.RESET)
                    self.steps.append('Решения нет')
                    self.img = 'img8'
