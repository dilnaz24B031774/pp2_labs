#Python regEx exercises

#Task 1
import re
pattern = r"^ab*$"
strings = ['a','ab','abb','abc','c','b','ba','bab']
# '^' - начало строки ,'$'- конец строки
# "c" не входит в шаблон
for s in strings:
    print(f"'{s}':",bool(re.fullmatch(pattern,s)))

#Task 2
def match_a_followed_by_two_or_three_b(txt):
    txt = input()
    return re.fullmatch(r'ab{2,3}', txt) is not None
print(match_a_followed_by_two_or_three_b())

# Task 3
def find_sequences_lowercase_with_underscore(s):
    s = input()
    return re.findall(r'\b[a-z]+_[a-z]+\b', s)
print(find_sequences_lowercase_with_underscore())

# Task 4
#Найти последовательности из одной прописной буквы, за которой следуют строчные буквы.
def find_upper_followed_by_lower():
    string = input("Enter a string for Task 4: ")
    return re.findall(r'[A-Z][a-z]+', string)
print(find_upper_followed_by_lower())

# Task 5

def match_a_followed_by_anything_ending_in_b(sentence):
    sentence = input()
    return re.fullmatch(r'a.*b', sentence) is not None
print(match_a_followed_by_anything_ending_in_b())

# Task 6
def replace_space_comma_dot(a):
    a = input()
    return re.sub(r'[ ,.]', ':', a)
print(replace_space_comma_dot())

# Task 7

def snake_to_camel(b):
    b = input()
    words = b.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])
print(snake_to_camel())

# Task 8

def split_at_uppercase(c):
    c = input()
    return re.findall(r'[A-Z][^A-Z]*', c)
print(split_at_uppercase())

# Task 9

def insert_spaces_before_capitals(d):
    d = input()
    return re.sub(r'([A-Z])', r' \1', d).strip()
print(insert_spaces_before_capitals())

# Task 10
def camel_to_snake(e):
    e = input()
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', e).lower()
print(camel_to_snake())
