# 1. Complete the function that accepts a string parameter, and reverses each word in the string.
# All spaces in the string should be retained.
# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(text):
    return ' '.join(map(lambda word: word[::-1], text.split(' ')))

# 2. You might know some pretty large perfect squares. But what about the NEXT one?
# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
# Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
# If the argument is itself not a perfect square then return either -1 or an empty value like None or null,
# depending on your language. You may assume the argument is non-negative.

def find_next_square(sq):
    """
    Возвращает следующий полный квадрат после sq, если sq сам является полным квадратом.
    Если sq — не полный квадрат, возвращает -1.
    """
    # Находим корень из числа
    root = sq ** 0.5
    # Проверяем, целый ли корень (то есть, является ли число полным квадратом)
    if root != int(root):
        return -1
    # Берём целый корень
    root = int(root)
    # Следующее целое число после корня
    next_root = root + 1
    # Возвращаем квадрат этого числа
    return next_root ** 2

# 3. This time no story, no theory. The examples below show you how to write function accum:
# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# Параметр accum - это строка, которая содержит только буквы от a..z до A..Z.

def accum(st):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(st))

# 4. You are given an array(list) strarr of strings and an integer k.
# Your task is to return the first longest string consisting of k consecutive strings taken in the array.
# Examples:
# strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2
# Concatenate the consecutive strings of strarr by 2, we get:
# treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
# folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
# trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
# blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
# abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]
# Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
# The first that came is "folingtrashy" so
# longest_consec(strarr, 2) should return "folingtrashy".
# In the same way:
# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
# n being the length of the string array, if n = 0 or k > n or k <= 0 return "" (return Nothing in Elm, "nothing" in Erlang).
# Note
# consecutive strings : follow one after another without an interruption

def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k <= 0 or k > n:
        return ""
    return max((''.join(strarr[i:i + k]) for i in range(n - k + 1)), key=len)

# 5. Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters
# and numeric digits that occur more than once in the input string. The input string can be assumed
# to contain only alphabets (both uppercase and lowercase) and numeric digits.
# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice

def duplicate_count(text):
    text = text.lower()
    return sum(text.count(c) > 1 for c in set(text))

# 6. Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

def grow(arr):
    import math
    return math.prod(arr)

# 7. Given an array of integers, return a new array with each value doubled.
# For example:
# [1, 2, 3] --> [2, 4, 6]

def maps(a):
    return [x*2 for x in a]

# 8. You're writing code to control your town's traffic lights.
# You need a function to handle each change from green, to yellow, to red, and then to green again.
# Complete the function that takes a string as an argument representing the current state of the light
# and returns a string representing the state the light should change to.
# For example, when the input is green, output should be yellow.

def update_light(current):
    return {'green': 'yellow', 'yellow': 'red', 'red': 'green'}[current]
#
# 9. A hero is on his way to the castle to complete his mission.
# However, he's been told that the castle is surrounded with a couple of powerful dragons!
# Each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry..
# Assuming he's gonna grab a specific given number of bullets '
# and move forward to fight another specific given number of dragons, will he survive?
# Return true if yes, false otherwise :)

def hero(bullets, dragons):
    return dragons*2 <= bullets

# 10. Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
# Write a function which takes a list of strings and returns each line prepended by the correct number.
# The numbering starts at 1. The format is n: string. Notice the colon and space in between.
# Examples: (Input --> Output)
# [] --> []
# ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]

def number(lines):
    return [f'{index + 1}: {line}' for index, line in enumerate(lines)]
