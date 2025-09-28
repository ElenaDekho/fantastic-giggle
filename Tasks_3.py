# 1. На этот раз мы хотим провести вычисления с использованием функций и получить результаты.
# Давайте рассмотрим несколько примеров:
# seven(times(five()))    #  must return 35
# four(plus(nine()))      #  must return 13
# eight(minus(three()))   #  must return 5
# six(divided_by(two()))  #  must return 3
# Требования:
# Должна быть функция для каждого числа от 0 ("ноль") до 9 ("девять")
# Должна быть функция для каждой из следующих математических операций: плюс, минус, умножение, деление
# Каждое вычисление состоит ровно из одной операции и двух чисел
# Самая внешняя функция представляет левый операнд, самая внутренняя функция представляет правый операнд
# Деление должно быть целочисленным. Например, это должно возвращать 2, а не 2.6666666...:
# eight(divided_by(three()))

def zero(f=None): return 0 if f is None else f(0)
def one(f=None): return 1 if f is None else f(1)
def two(f=None): return 2 if f is None else f(2)
def three(f=None): return 3 if f is None else f(3)
def four(f=None): return 4 if f is None else f(4)
def five(f=None): return 5 if f is None else f(5)
def six(f=None): return 6 if f is None else f(6)
def seven(f=None): return 7 if f is None else f(7)
def eight(f=None): return 8 if f is None else f(8)
def nine(f=None): return 9 if f is None else f(9)

def plus(y): return lambda x: x + y
def minus(y): return lambda x: x - y
def times(y): return lambda x: x * y
def divided_by(y): return lambda x: x // y

# Пример:
print(seven(times(five())))    # 35
print(four(plus(nine())))      # 13
print(eight(minus(three())))   # 5
print(six(divided_by(two())))  # 3

# 2. Чтобы выполнить это упражнение, вам нужно написать функцию,
# которая форматирует длительность в секундах удобным для пользователя способом.
# Функция должна принимать неотрицательное целое число. Если оно равно нулю, она просто возвращает значение "сейчас".
# В противном случае продолжительность выражается в виде комбинации лет, дней, часов, минут и секунд.
# Это гораздо проще понять на примере:
# * При значении секунды = 62 ваша функция должна возвращать значение
#     "1 минута и 2 секунды"
# * При значении секунды = 3662 ваша функция должна возвращать значение
#     "1 час, 1 минута и 2 секунды"
# Для целей этого ката год равен 365 дням, а сутки - 24 часам.
# Обратите внимание, что пробелы важны.
# Подробные правила
# Результирующее выражение состоит из таких компонентов, как 4 секунды, 1 год и т.д.
# Обычно это целое положительное число и одна из допустимых единиц измерения времени, разделенных пробелом.
# Единица измерения времени используется во множественном числе, если целое число больше 1.
# Компоненты разделяются запятой и пробелом (", "). За исключением последнего компонента,
# который разделяется "и", как это было бы написано в английском языке.
# Более значимые единицы времени будут указаны раньше, чем наименее значимые.
# Следовательно, 1 секунда и 1 год - это неверно, но 1 год и 1 секунда - это правильно.
# Разные компоненты имеют разные единицы измерения времени.
# Таким образом, нет повторяющихся единиц измерения, таких как 5 секунд и 1 секунда.
# Компонент вообще не появится, если его значение окажется равным нулю.
# Следовательно, значение 1 минута и 0 секунд недопустимо, но оно должно составлять всего 1 минуту.
# Единица измерения времени должна использоваться "как можно дольше". Это означает, что функция
# должна возвращать не 61 секунду, а 1 минуту и 1 секунду. Формально, продолжительность,
# указанная в компоненте, не должна превышать любую допустимую более значимую единицу времени.

def format_duration(seconds):
    # Возвращаем "now" для нулевого значения
    if seconds == 0:
        return "now"

    # Определяем единицы времени: (секунды в единице, название единицы)
    units = [(31536000, "year"), (86400, "day"), (3600, "hour"), (60, "minute"), (1, "second")]
    parts = []  # Список для хранения ненулевых компонентов времени

    # Перебираем каждую единицу времени от самой большой к самой маленькой
    for unit_seconds, unit_name in units:
        count = seconds // unit_seconds  # Количество полных единиц
        if count:  # Если количество больше 0
            # Формируем строку с правильной формой множественного числа
            parts.append(f"{count} {unit_name}{'s' if count > 1 else ''}")
            seconds %= unit_seconds  # Обновляем оставшиеся секунды

    # Возвращаем результат: один компонент или несколько через запятую и "and"
    return parts[0] if len(parts) == 1 else ", ".join(parts[:-1]) + " and " + parts[-1]

# Примеры использования:
print(format_duration(0))      # "now"
print(format_duration(1))      # "1 second"
print(format_duration(62))     # "1 minute and 2 seconds"
print(format_duration(3662))   # "1 hour, 1 minute and 2 seconds"
print(format_duration(120))    # "2 minutes"
print(format_duration(3600))   # "1 hour"
print(format_duration(86400))  # "1 day"
print(format_duration(31536000)) # "1 year"
print(format_duration(90061))  # "1 day, 1 hour, 1 minute and 1 second"
print(format_duration(253374061)) # "8 years, 12 days, 13 hours, 41 minutes and 1 second"

# 3. In this kata, you will write a function that returns the positions and the values of the "peaks"
# (or local maxima) of a numeric array.
# For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3 with a value of 5 (since arr[3] equals 5).
# The output will be returned as an object with two properties: pos and peaks.
# Both of these properties should be arrays. If there is no peak in the given array,
# then the output should be {pos: [], peaks: []}.
# Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return {pos: [3, 7], peaks: [6, 3]}
# (or equivalent in other languages)
# All input arrays will be valid integer arrays (although it could still be empty),
# so you won't need to validate the input.
# The first and last elements of the array will not be considered as peaks (in the context of a mathematical function,
# we don't know what is after and before and therefore, we don't know if it is a peak or not).
# Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3] and [1, 2, 2, 2, 2] do not.
# In case of a plateau-peak, please only return the position and value of the beginning of the plateau.
# For example: pickPeaks([1, 2, 2, 2, 1]) returns {pos: [1], peaks: [2]} (or equivalent in other languages)

def pick_peaks(arr):
    """
    Возвращает позиции и значения локальных максимумов ("пиков") в массиве.
    Учитывает плато: если плато окружено меньшими значениями — возвращается только его начало.
    Первый и последний элементы не рассматриваются как пики.
    """
    # Если массив слишком короткий — пиков быть не может
    if len(arr) < 3:
        return {'pos': [], 'peaks': []}

    pos = []      # Список позиций пиков
    peaks = []    # Список значений пиков
    i = 1         # Начинаем со второго элемента (индекс 1)

    while i < len(arr) - 1:  # Не рассматриваем последний элемент
        # Шаг 1: Ищем восходящий фронт (текущий элемент > предыдущего)
        if arr[i] > arr[i - 1]:
            j = i

            # Шаг 2: Пропускаем плато (все одинаковые элементы)
            while j < len(arr) - 1 and arr[j] == arr[j + 1]:
                j += 1

            # Шаг 3: Проверяем, есть ли спад после плато (или сразу после пика)
            if j < len(arr) - 1 and arr[j] > arr[j + 1]:
                # Это пик! Добавляем начало плато (или сам пик, если плато длины 1)
                pos.append(i)
                peaks.append(arr[i])
                # Перепрыгиваем всё плато — избегаем повторной обработки
                i = j

        # Переходим к следующему элементу (если не перепрыгнули плато выше)
        i += 1

    return {'pos': pos, 'peaks': peaks}

# Пример:
print(pick_peaks([0, 1, 2, 5, 1, 0]))
# {'pos': [3], 'peaks': [5]}

print(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]))
# {'pos': [3, 7], 'peaks': [6, 3]}

print(pick_peaks([1, 2, 2, 2, 1]))
# {'pos': [1], 'peaks': [2]}  ← начало плато

print(pick_peaks([1, 2, 2, 2, 3]))
# {'pos': [], 'peaks': []}    ← не пик — справа выше

print(pick_peaks([1, 2, 2, 2, 2]))
# {'pos': [], 'peaks': []}    ← плато на краю — не пик

print(pick_peaks([1, 2, 3, 2, 1, 2, 2, 2, 1]))
# {'pos': [2, 5], 'peaks': [3, 2]}

# 4. The maximum sum subarray problem consists in finding the maximum sum
# of a contiguous subsequence in an array or list of integers:
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array.
# If the list is made up of only negative numbers, return 0 instead.
# Empty list is considered to have zero greatest sum.
# Note that the empty list or array is also a valid sublist/subarray.

def max_sequence(arr):
    # Если массив пуст — сразу возвращаем 0
    if not arr:
        return 0

    max_sum = current_sum = 0  # Инициализируем обе переменные за один шаг

    for num in arr:
        # Обновляем текущую сумму: сбрасываем в 0, если становится отрицательной
        current_sum = max(0, current_sum + num)
        # Обновляем максимальную сумму, если текущая стала больше
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

# Пример:
print(max_sequence([]))                        # 0
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6 → [4, -1, 2, 1]
print(max_sequence([1, 2, 3, 4]))             # 10 → вся последовательность
print(max_sequence([-1, -2, -3]))             # 0 → все отрицательные
print(max_sequence([-2, -1, -3, 0, -4]))      # 0 → включая ноль
print(max_sequence([5]))                      # 5
print(max_sequence([-1, 2, 3, -1, 4, -10, 5])) # 8 → [2, 3, -1, 4]

# 5. Complete the function scramble(str1, str2) that returns true if a portion of str1 characters
# can be rearranged to match str2, otherwise returns false.
# Notes:
# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

from collections import Counter

def scramble(s1, s2):
    # Считаем частоту каждого символа в первой строке
    c1 = Counter(s1)
    # Проверяем: для каждого символа во второй строке — хватает ли его в первой
    return all(c1[char] >= count for char, count in Counter(s2).items())

# Пример использования:
print(scramble('rkqodlw', 'world'))              # True
print(scramble('cedewaraaossoqqyt', 'codewars')) # True
print(scramble('katas', 'steak'))                # False
print(scramble('scriptjava', 'javascript'))      # True
print(scramble('scriptingjava', 'javascript'))   # True
print(scramble('aabbc', 'abc'))                  # True
print(scramble('abc', 'aabbcc'))                 # False
print(scramble('', 'a'))                         # False
print(scramble('a', ''))                         # True (пустая строка всегда "вмещается")

# 6. Write two functions that convert a roman numeral to and from an integer value.
# Multiple roman numeral values will be tested for each function.
# Modern Roman numerals are written by expressing each digit separately starting with the left most digit
# and skipping any digit with a value of zero. In Roman numerals:
# 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
# 2008 is written as 2000=MM, 8=VIII; or MMVIII
# 1666 uses each Roman symbol in descending order: MDCLXVI.
# Input range : 1 <= n < 4000
# In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
# Examples
# to roman:
# 2000 -> "MM"
# 1666 -> "MDCLXVI"
#   86 -> "LXXXVI"
#    1 -> "I"
#
# from roman:
# "MM"      -> 2000
# "MDCLXVI" -> 1666
# "LXXXVI"  ->   86
# "I"       ->    1
#
# Help
# +--------+-------+
# | Symbol | Value |
# +--------+-------+
# |    M   |  1000 |
# |   CM   |   900 |
# |    D   |   500 |
# |   CD   |   400 |
# |    C   |   100 |
# |   XC   |    90 |
# |    L   |    50 |
# |   XL   |    40 |
# |    X   |    10 |
# |   IX   |     9 |
# |    V   |     5 |
# |   IV   |     4 |
# |    I   |     1 |
# +--------+-------+

class RomanNumerals:
    # Статические маппинги — создаются один раз при загрузке класса
    _to_roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    _from_roman_map = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
    }

    @staticmethod
    def to_roman(val: int) -> str:
        # Используем список для сборки результата — эффективнее конкатенации строк
        result = []
        # Проходим по всем возможным римским значениям в порядке убывания
        for num, sym in RomanNumerals._to_roman_map:
            # Если значение уже 0 — выходим раньше (оптимизация)
            if val == 0:
                break
            # Считаем, сколько раз текущий символ помещается в оставшееся число
            count, val = divmod(val, num)
            # Добавляем нужное количество символов (например, 'III' для 3)
            if count > 0:
                result.append(sym * count)
        # Собираем строку за один проход
        return ''.join(result)

    @staticmethod
    def from_roman(roman_num: str) -> int:
        result = 0
        i = 0
        n = len(roman_num)  # Кешируем длину строки — не пересчитываем в цикле
        # Проходим по строке слева направо
        while i < n:
            # Проверяем сначала двухсимвольные комбинации (например, "IV", "CM")
            if i + 1 < n and roman_num[i:i + 2] in RomanNumerals._from_roman_map:
                result += RomanNumerals._from_roman_map[roman_num[i:i + 2]]
                i += 2  # Пропускаем два символа
            else:
                # Иначе обрабатываем одиночный символ
                result += RomanNumerals._from_roman_map[roman_num[i]]
                i += 1  # Пропускаем один символ
        return result


# Преобразование числа → римское
print(RomanNumerals.to_roman(1))      # "I"
print(RomanNumerals.to_roman(4))      # "IV"
print(RomanNumerals.to_roman(9))      # "IX"
print(RomanNumerals.to_roman(58))     # "LVIII"
print(RomanNumerals.to_roman(1994))   # "MCMXCIV"
print(RomanNumerals.to_roman(1666))   # "MDCLXVI"
print(RomanNumerals.to_roman(2000))   # "MM"
print(RomanNumerals.to_roman(86))     # "LXXXVI"

# Преобразование римского → число
print(RomanNumerals.from_roman("I"))        # 1
print(RomanNumerals.from_roman("IV"))       # 4
print(RomanNumerals.from_roman("IX"))       # 9
print(RomanNumerals.from_roman("LVIII"))    # 58
print(RomanNumerals.from_roman("MCMXCIV"))  # 1994
print(RomanNumerals.from_roman("MDCLXVI"))  # 1666
print(RomanNumerals.from_roman("MM"))       # 2000
print(RomanNumerals.from_roman("LXXXVI"))   # 86

# 7. ROT13 - это простой шифр с подстановкой букв, который заменяет букву на 13 букв после нее в алфавите.
# ROT13 - это пример шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13.
# Если в строку включены цифры или специальные символы, они должны быть возвращены в том виде, в каком они есть.
# Только буквы латинского/английского алфавита должны быть сдвинуты, как в оригинальной "реализации" Rot13.

import string

def rot13(message):
    """
    Шифрует строку с помощью ROT13.
    Только латинские буквы (A-Z, a-z) сдвигаются на 13 позиций.
    Все остальные символы остаются без изменений.
    """
    # Создаём таблицу трансляции один раз (можно вынести в глобальную область для повторного использования)
    rot13_table = str.maketrans(
        string.ascii_lowercase + string.ascii_uppercase,
        string.ascii_lowercase[13:] + string.ascii_lowercase[:13] +
        string.ascii_uppercase[13:] + string.ascii_uppercase[:13]
    )
    return message.translate(rot13_table)

# Пример:
print(rot13("Hello, World!"))      # → "Uryyb, Jbeyq!"
print(rot13("ROT13 example."))     # → "EBG13 rknzcyr."
print(rot13("123!@#"))             # → "123!@#"
print(rot13("Test123"))            # → "Grfg123"
print(rot13(rot13("Secret")))      # → "Secret"  (двойное применение = оригинал)

# 8. Напиши функцию multiply_list(lst), которая принимает список чисел и возвращает их произведение.
# Если список пуст — верни 1.

import math

def multiply_list(lst):
    return math.prod(lst)

# Пример использования:
print(multiply_list([2, 3, 2]))
print(multiply_list([]))
#
# 9. Напиши функцию count_vowels(s), которая принимает строку и возвращает количество гласных букв (a, e, i, o, u) в ней.
# Считай только строчные и прописные английские гласные. Регистр не важен.

def count_vowels(s):
    vowel_letters = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for letter in s.lower():
        if letter in vowel_letters:
            count += 1
    return count

# Пример использования:
print(count_vowels("HEllO"))
print(count_vowels("Python"))

# 10. Напиши функцию reverse_words(s), которая принимает строку и возвращает новую строку,
# в которой каждое слово перевёрнуто, а порядок слов остаётся прежним.
# Пример:
# reverse_words("Hello world") → "olleH dlrow"
# reverse_words("Python is fun") → "nohtyP si nuf"
# Слова разделены ровно одним пробелом, дополнительных пробелов в начале/конце нет.

def reverse_words(s):
    return ' '.join(word[::-1] for word in s.split())

# Пример использования:
print(reverse_words("Python is fun"))
