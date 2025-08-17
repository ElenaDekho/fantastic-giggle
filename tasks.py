# 1. Your task is to make a function that can take any non-negative integer as an argument
# and return it with its digits in descending order.
# Essentially, rearrange the digits to create the highest possible number.
# Examples:
# Input: 42145 Output: 54421
# Input: 145263 Output: 654321
# Input: 123456789 Output: 987654321

def descending_order(num):
    temp = "".join(sorted(str(num), reverse=True))
    return int(temp, base = 10)


# 2. In this little assignment you are given a string of space separated numbers,
# and have to return the highest and lowest number.
# Examples
# high_and_low("1 2 3 4 5") # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"

def high_and_low(numbers):
    nums = list(map(int, numbers.split()))
    highest = max(nums)
    lowest = min(nums)
    return f"{highest} {lowest}"


# 3. Check to see if a string has the same amount of 'x's and 'o's.
# The method must return a boolean and be case insensitive. The string can contain any char.
# Examples input/output:
#
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(s):
    return s.lower().count("x".lower()) == s.lower().count("o".lower())


# 4. Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

def double_char(s):
    return "".join([letter*2 for letter in s])


# 5. Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# For example, the score of abad is 8 (1 + 2 + 1 + 4).
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.

def high(x):
    words = x.split()
    max_score = 0
    result = ""
    for word in words:
        score = sum(ord(letter) - ord('a') + 1 for letter in word)
        if score > max_score:
            max_score = score
            result = word
    return result


# 6. Complete the solution so that it returns true if the first argument(string)
# passed in ends with the 2nd argument (also a string).

def solution(text, ending):
    return text.endswith(ending)


# 7. Ваша задача - построить здание, которое будет представлять собой груду из n кубов.
# Куб внизу будет иметь объем n в кубе.
# Куб, указанный выше, будет иметь объем (n−1) в кубе.
# И так далее до самого верха, который будет иметь объем 1 в кубе.
# Вам задан общий объем здания m.
# Имея значение m, можете ли вы определить количество n кубов, которые вам нужно будет построить?
# Параметром функции findNb (find_nb, find-nb, findNb, ...) будет целое число m,
# и вы должны вернуть целое число n, например
# findNb(1071225) --> 45
# findNb(91716553919377) --> -1

def find_nb(m):
    if m <= 0:
        return -1
    n = 1
    total = 0
    while total < m:
        total += n ** 3
        if total == m:
            return n
        n += 1
    return -1


# 8. Complete the function so that it finds the average of the three scores passed to it
# and returns the letter value associated with that grade.
# 90 <= score <= 100                  'A'
# 80 <= score < 90                    'B'
# 70 <= score < 80                    'C'
# 60 <= score < 70                    'D'
# 0 <= score < 60                     'F'
# Tested values are all between 0 and 100. There is no need to check for negative values or values greater than 100.

def get_grade(s1, s2, s3):
    avg = (s1 + s2 + s3) / 3
    if 90 <= avg:
        return 'A'
    elif 80 <= avg:
        return 'B'
    elif 70 <= avg:
        return 'C'
    elif 60 <= avg:
        return 'D'
    return 'F'


# 9. Given a list of integers, determine whether the sum of its elements is odd or even.
# Give your answer as a string matching "odd" or "even".
# If the input array is empty consider it as: [0] (array with a zero).

def odd_or_even(arr):
    return "odd" if sum(arr)%2 else "even"


# 10. Implement the function unique_in_order which takes as argument a sequence and returns a list of items
# without any elements with the same value next to each other and preserving the original order of elements.
# For example:
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

def unique_in_order(sequence):
    result = []
    for elem in sequence:
        if len(result) == 0:
            result.append(elem)
        elif elem == result[-1]:
            continue
        else:
            result.append(elem)
    return result






