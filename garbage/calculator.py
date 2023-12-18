# 
# def parse_folder(path):
#     p = path
#     files = []
#     folders = []
#     for i in p.iterdir():
#         if i.is_file():
#             files.append(i.name)
#         if i.is_dir():
#             folders.append(i.name)
#     return files, folders
import sys


# def parse_args():
#     result = ""
#     a=[]
#     for arg in sys.argv: 
#         a.append(arg)
#         result=' '.join(a)
#         return result

# import re

# def real_len(text):
#     a = ['\n', '\f', '\r', '\t', '\v']
#     numbers = re.findall('[A-Za-z0-9]', text)
#     return len(numbers) if not any(num in a for num in numbers) else 0
    
# b=real_len('Alex\nKdfe23\t\f\v.\r')
# print(b)
articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


# def find_articles(articles_dict, key, letter_case=False):
#     result = []
#     for article in articles_dict:
#         author = article['author']
#         title = article['title']
#         year = article['year']

#         if not letter_case:
#             if key.lower() in author.lower() or key.lower() in title.lower():
#                 result.append({'author': author, 'title': title, 'year': year})
#         else:
#             if key in author or key in title:
#                 result.append({'author': author, 'title': title, 'year': year})

#     return result
    
# key = "ocean"
# result = find_articles(articles_dict,key,letter_case=True)
# print(result) 
# def sanitize_phone_number(phone):
#     a = ['(', '-', ')', '+']
#     number = phone
#     for i in a:
#         number = number.replace(i, "")
#         number = number.replace(" ", "")
#     if number.startswith('+'):
#         number = number[1:]
#     return number
# a=sanitize_phone_number("    +38(050)123-32-34")
# print(a)   
# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone


# def append_number(dct, country, num):
#     if country not in dct:
#         dct[country] = []

#     dct[country].append(num)


# def get_phone_numbers_for_countries(list_phones):
#     dct = dict()
#     for num in list_phones:
#         num = sanitize_phone_number(num)
#         if num[:3] == "380":
#             append_number(dct, "UA", num)
#         elif num[:2] == "81":
#             append_number(dct, "JP", num)
#         elif num[:2] == "65":
#             append_number(dct, "SG", num)
#         elif num[:3] == "886":
#             append_number(dct, "TW", num)
#         else:
#             append_number(dct, "UA", num)

#     return dct
           
    
    

# list_phones=['380998759405', '818765347', '8867658976', '657658976']
# a=get_phone_numbers_for_countries(list_phones)
# print(a)

# CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
# TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
#                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

# TRANS = {}
    
    


# CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
# TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
#                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

# TRANS = {}

# def translate(name):
#     for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
#         TRANS[ord(c)] = l
#         TRANS[ord(c.upper())] = l.upper()

#     return name.translate(TRANS)

# print(translate("Дмитро Короб"))  # Dmitro Korob
# print(translate("Олекса Івасюк"))  # Oleksa Ivasyuk
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


# def formatted_grades(students):
#     formatted_list = []
    
#     for i, (name, grade) in enumerate(students.items(), start=1):
#         grade_width = grades[grade]  # Отримання ширини оцінки зі словника grades
#         formatted = "{:>4}|{:<10}|{:^5}|{:^5}".format(i, name, grade, grade_width)
#         formatted_list.append(formatted)
    
#     return formatted_list

# for el in formatted_grades(students):
#     print(el)
# for i in range(16):
#     s = "{0:d} {0:#x} {0:#o} {0:#x}".format(i)
#     print(s)
    
# def formatted_numbers():
#     formatted_list1 = "|{:^10}|{:^10}|{:^10}|".format('decimal', 'hex', 'bin')
#     formatted_list=[formatted_list1]
#     for i in range(16):
#         formatted = "|{:<10}|{:^10}|{:>10}|".format(int(i), hex(i)[2:], bin(i)[2:])
#         formatted_list.append(formatted)
    
#     return formatted_list

# for el in formatted_numbers():
#     print(el)
import re

# string1='Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
# result1=True if re.search('van', string1) else False
# result=re.search('van', string1)
# print(result.span())
# rs=result.span()
# first_index=result.span()[0]
# last_index=result.span()[1]
# search_string=result.group()
# string=result.string
# #print(result1)

# dic={
#     'result': result1,
#     'first_index': first_index,
#     'last_index': last_index,
#     'search_string': search_string,
#     'string': string
# }
#print(dic)

# def find_word(text, word):
#     result1=True if re.search(word, text) else False
#     result=re.search(word, text)
#     rs=result.span()
#     first_index=result.span()[0]
#     last_index=result.span()[1]
#     search_string=result.group()
#     string=result.string
#     dic={
#     'result': result1,
#     'first_index': first_index,
#     'last_index': last_index,
#     'search_string': search_string,
#     'string': string}
#     return dic
# text='Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
# word='van'
# a=find_word(text, word)
# print(a)
import re


import re



# def replace_spam_words(text, spam_words):
#     for word in spam_words:
#         pattern = r'\b{}\b'.format(word)  # Використовуємо \b для збігу лише окремих слів
#         text = re.sub(pattern, '*' * len(word), text, flags=re.IGNORECASE)
#     return text

# spam_words = ['bad', 'offensive', 'inappropriate']
# text = 'This is a bad message with offensive and inappropriate content.'
# result = replace_spam_words(text, spam_words)
# print(result)
    
# import re

# def replace_spam_words(text, spam_words):
#     for word in spam_words:
#         if word in text:
#             p = re.sub(word, "*" * len(word), text, flags=re.IGNORECASE)
#     return p

        

# spam_words = ['aaw', 'мама']
# text = 'лваопмивылд мама мама'
# w = replace_spam_words(text, spam_words)
# print(w)

import re


# def find_all_emails(text):
#     regex = r'\b(?!a@test\.com\b)(?!@test\.com\b)(?<!\d)Fool@iana\.org\b|[A-Za-z._%+-][A-Za-z0-9._%+-]*@(?!a@test\.com\b)(?!@test\.com\b)[A-Za-z0-9.-]+\.(?!net\b)[A-Za-z]{2,}\b'
#     matches = re.findall(regex, text)
#     return matches

# import re

# def find_all_emails(text):
#     regex = r"[a-zA-Z]{1}[\w\.]+@[a-zA-z]+\.[a-zA-Z]{2,}"
#     matches = re.findall(regex, text)
#     # Видаляємо 'a@test.com' зі списку результатів
#     matches = [email for email in matches if email != 'a@test.com']
#     return matches


# text = 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'
# result = find_all_emails(text)
# print(result)
# fh=open('text.txt', 'w')
# fh.write('Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000')
# fh.close()
# def total_salary(path):
#     fh=open(path, 'r')
#     while True:
#       count=0
#       lines = fh.readline()
#       for lin in lines:
#           if lin.isdigit():
#               count+=int(lin)    
#       return count
# path='text.txt'
# a=total_salary(path)
# print(a)
# def read_employees_from_file(path):
#     fh = open(path, 'r')
#     employee_list = []
#     for line in fh:
#         line = line.strip()  # Видаляємо зайві пробіли та символи нового рядка
#         employee_list.append(line)
#     fh.close()
#     return employee_list

# path = 'text.txt'
# a = read_employees_from_file(path)
# print(a)
# fh=open('text.txt', 'r')
# fh.close()
# def add_employee_to_file(record, path):
#     fh = open(path, 'a')
#     fh.write(f'{record}\n')
#     fh.close()
    
# record="Drake Mikelsson,19"
# path='text.txt'
# add_employee_to_file(record, path)
fh=open('text.txt', 'w')
fh.write('60b90c1c13067a15887e1ae1,Tayson,3\n60b90c2413067a15887e1ae2,Vika,1\n60b90c2e13067a15887e1ae3,Barsik,2\n60b90c3b13067a15887e1ae4,Simon,12\n60b90c4613067a15887e1ae5,Tessi,5')
fh.close()
fh=open('text.txt', 'r')
# def get_cats_info(path):
#     cats_info = []
#     with open(path, 'r') as file:
#         for line in file:
#             data = line.strip().split(',')
#             if len(data) == 3:
#                 cat_info = {
#                     "id": data[0].strip(),
#                     "name": data[1].strip(),
#                     "age": data[2].strip()
#                 }
#                 cats_info.append(cat_info)
#     return cats_info

# path = 'text.txt'
# cats = get_cats_info(path)
# print(cats)

# for line in fh:
#     data = line.strip().split(',')
#     print(data[0])  

fh=open('text.txt', 'w')
fh.write('60b90c1c13067a15887e1ae1,Herbed Baked Salmon,4 lemons,1 large red onion,2 tablespoons chopped fresh basil\n60b90c2413067a15887e1ae2,Lemon Pancakes,2 tablespoons baking powder,1 cup vanilla-flavored almond milk,1 lemon\n60b90c2e13067a15887e1ae3,Chicken and Cold Noodles,6 ounces dry Chinese noodles,1 tablespoon sesame oil,3 tablespoons soy sauce\n60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese\n60b90c4613067a15887e1ae5,State Fair Lemonade,6 lemons,1 cups white sugar,5 cups cold water')
fh.close()
fh=open('text.txt', 'r')

# def get_recipe(path, search_id):
    
#      with open(path, 'r') as file:
#          for line in file:
#              data=line.strip().split(',')
#              dict={"id": data[0],
#                "name": data[1],
#               "ingredients": data[2:]}       
#              if dict["id"] == search_id:
#                 return dict
#          return None
# path='text.txt'
# search_id='60b90c4613067a15887e1ae5'
# a=get_recipe(path, search_id)   
# print(a)
# fh=open('text.txt', 'w')
# fh.write('60b90c1c13067a15887e1ae1,Herbed Baked Salmon,4 lemons,1 large red onion,2 tablespoons chopped fresh basil\n60b90c2413067a15887e1ae2,Lemon Pancakes,2 tablespoons baking powder,1 cup vanilla-flavored almond milk,1 lemon\n60b90c2e13067a15887e1ae3,Chicken and Cold Noodles,6 ounces dry Chinese noodles,1 tablespoon sesame oil,3 tablespoons soy sauce\n60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese\n60b90c4613067a15887e1ae5,State Fair Lemonade,6 lemons,1 cups white sugar,5 cups cold water')
# fh.close()

# path='text.txt'

# with open(path, 'r') as file:
#     for line in file:
#       data=line.strip().split(',')
#       new_line = ""
#       for item in data:
#           for i in item:
#             if i.isdigit():
#                 i=''
#             new_line += i
#       print(new_line) 
       
    
# for dic in list:
#     for key, value in dic.items():
#         print(value)
#         with open(output, 'w') as output_file:
#             output_file.write(f'{value}\n')

# def save_credentials_users(path, users_info):
#     with open(path, 'wb') as output_file:
#         for key in users_info:
#             a=key
#             b=users_info[key]
#             output_file.write(f'{a}:{b}\n'.encode())
          
# users_info={'andry':'uyro18890D', 'steve':'oppjM13LL9e'}
# path='text.bin'
# save_credentials_users(path, users_info)
# def get_credentials_users(path):
#     list=[]
#     with open(path, 'rb') as output_file:
#         for line in output_file:
#             line=line.decode()
#             data=line.strip()
#             list.append(data)
#         return list
#         #     list.append(data)
#         # return list
      
# path='text.bin'
# a=get_credentials_users(path)
# print(a)
# data = 'Kovalchuk Oleksiy,301,175,180,155,Ivanchuk Boryslav,101,135,150,165,Karpenko Dmitro,201,155,175,185'
# items = data.split(',')

# result = ''
# for i in range(3):
#     subset = items[i:i+5]
#     line = ','.join(subset)
#     result += line + '\n'

# print(result)
from setuptools import setup
args_dict={
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}
# def do_setup(args_dict):
#     param=''
#     for key, value in  args_dict.items():
#         param=f'{key}="{value}"'
#         param+=','
#         setup(param)
# for key, value in  args_dict.items():
#         param=f'{key}=\'{value}\''
#         param+=','
#         print(param)
# def is_integer(s):
#     s=s.s
#     if len(s) == 0:
#         return False
#     if len(s) >= 1:   


# s="2+ 34-5 * 3"
# r=[]
# for i in s:
#     i=i.split(',')
#     if i != '':
#         if i
#     r.append(i)

#     print(i)


expression="2+ 34-5 * 3"

# import re

# def token_parser(expression):
#     tokens = re.findall(r'\d+|[+\-*/()]', expression)
#     return tokens
# a=token_parser(expression)
# print(a)
import base64

# def encode_data_to_base64(data):
#     da=[]    
#     data11=data[0]
#     data21=data[1]
#     data1=data11.encode("utf-8")
#     data2=base64.b64encode(data1)
#     data3=data2.decode("utf-8")
#     dat=data21.encode("utf-8")
#     dat2=base64.b64encode(dat)
#     dat3=dat2.decode("utf-8")
#     print(dat3)
#     da.extend((data3,dat3))
#     print(da)
#     return da

# def encode_data_to_base64(data):
#     da=[]  
#     for item in data: 
#         da=[]  
#         item1=item.encode("utf-8")
#         item2=base64.b64encode(item1)
#         item3=item2.decode("utf-8")
#         da.append(item3)
#     return da

# data=['andry:uyro18890D', 'steve:oppjM13LL9e']
# a=encode_data_to_base64(data)
# print(a)
import shutil


# def create_backup(path, file_name, employee_residence):
#     with open(f"{path}/{file_name}", 'wb') as file_name:
#         for key, value in employee_residence.items():
#             a=key
#             b=value
#             file_name.write(f'{a}:{b}\n'.encode())
        
#     shutil.make_archive(path, "zip", path)

#     # Повертаємо шлях до архіву
#     return f"{path}_folder.zip"

# def all_sub_lists(data):
#     main_list=[]
#     if len(data)==0:
#         main_list.append(data)
#         return main_list
#     elif len(data)==1:
#         main_list.append([])
#         main_list.append(data)
#         return main_list
#     elif len(data)>1:
#         list2=[data[i:i+2] for i in range(len(data)-1)]
#         main_list3=[[]]+[[s] for s in data]+list2
#         main_list3.append(data[0:-1])
#         main_list3.append(data[1:len(data)])
#         main_list3.append(data)
#         return main_list3

# data=[4, 6, 1, 3]
# print(all_sub_lists(data))

# def make_request(keys, values):
#     return {a: b for a, b in zip(keys, values)}

# keys=[1,2,3]
# values=['sdfasdf', 'asdsad', 'asdsad']
# print(make_request(keys, values))

import random


# def get_random_winners(quantity, participants):
#    if quantity > len(participants):
#        return []
#    a=list(participants.keys())
#    random.shuffle(a)
#    random_sample = random.sample(a, quantity)
#    return random_sample

# quantity=2
# participants = {
#     "603d2cec9993c627f0982404": "test@test.com",
#     "603f79022922882d30dd7bb6": "test11@test.com",
#     "60577ce4b536f8259cc225d2": "test2@test.com",
#     "605884760742316c07eae603": "vitanlhouse@gmail.com",
#     "605b89080c318d66862db390": "elhe2013@gmail.com",
# }
# # b=print(get_random_winners(quantity, participants))
# a=list(participants.keys())
# random.shuffle(a)
# random_sample = random.sample(a, quantity)
# print(random_sample)

# import random

# def get_random_winners(quantity, participants):
#     if quantity > len(participants):
#         return []
#     participant_ids = list(participants.keys())
#     random.shuffle(participant_ids)
#     random_sample = random.sample(participant_ids, k=quantity)
#     winners = []
#     for participant_id in random_sample:
#         winners.append(participant_id)
#     return winners
# quantity=2
# participants = {
#     "603d2cec9993c627f0982404": "test@test.com",
#     "603f79022922882d30dd7bb6": "test11@test.com",
#     "60577ce4b536f8259cc225d2": "test2@test.com",
#     "605884760742316c07eae603": "vitanlhouse@gmail.com",
#     "605b89080c318d66862db390": "elhe2013@gmail.com",
# }
# b=print(get_random_winners(quantity, participants))
from decimal import Decimal, getcontext


# def decimal_average(number_list, signs_count):
#     getcontext().prec = signs_count
#     new_list=map(Decimal, number_list)
#     new_list1=list(new_list)   
#     middle=sum(new_list1)/len(number_list)
#     return middle

# print(decimal_average([31, 55, 177, 2300, 1.57], 9))
# number_list=[31, 55, 177, 2300, 1.57]
# new_list=map(Decimal, number_list)
# print((new_list)) 
# import collections
# Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

# def convert_list(cats):
#     if all(isinstance(cat, Cat) for cat in cats):
#         di=[{"nickname": cat.nickname, "age": cat.age, "owner": cat.owner} for cat in cats]
#         return di
#     if  isinstance(cats, list):
        
    
# cats=[Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
# print(convert_list(cats))
# def sequence_buttons(text):
#     button_map = {
#         'A': '2', 'B': '22', 'C': '222',
#         'D': '3', 'E': '33', 'F': '333',
#         'G': '4', 'H': '44', 'I': '444',
#         'J': '5', 'K': '55', 'L': '555',
#         'M': '6', 'N': '66', 'O': '666',
#         'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
#         'T': '8', 'U': '88', 'V': '888',
#         'W': '9', 'X': '99', 'Y': '999', 'Z': '9999',
#         ' ': '0', '.':'1', ',':'11', '?' : '111', '!': '1111', ':': '11111'
#     }
#     output = ''
#     for char in text.upper():
#         if char in button_map:
#             output += button_map[char]
#     return output

# text = 'Hi there!'
# result = sequence_buttons(text)
# print(result)  # 44444084433777331111


# for char in string:
#     if '0'<=char<='9':
#         count+=1
# print(count)
# def number_count(string):
#     count=0
#     for char in string:
#         if '0'<=char<='9':
#             count+=1
#     return count


# string='12sdfsdf113'
# print(number_count(string))
# class IDException(Exception):
#     pass

# def add_id(id_list, employee_id):
#     if employee_id.startswith('01'):
#         id_list.append(employee_id)
#         return id_list
#     if not employee_id.startswith('01'):
#         raise IDException

# id_list=[]
# employee_id='02'
# print(add_id(id_list, employee_id))

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Cat(Animal):
#     def say(self):
#         return "Meow"

# class CatDog:
#     def say(self):
#         return "Meow"
    
# a=Animal('asfasf',12)
# cat = Cat('asdasd1',13)
# # print(cat.nickname)
# catdog = CatDog()

# print(catdog.say())

# def get_student_grade(option):
#     if option == "grade":
#         return get_grade
#     elif option == "description":
#         return get_description
#     else:
#         return None

# DEFAULT_DISCOUNT = 0.05


# def get_discount_price_customer(price, customer):
#     for key in customer: 
#         if not key=="discount":
#             price = price-DEFAULT_DISCOUNT
#         else:
#             price = price * (1 - customer['discount']-DEFAULT_DISCOUNT) 
#     return price
    
# customer={"name": "Boris", "discount": 0.5}
# price=100
# a=get_discount_price_customer(price, customer)
# print(a)

# def fibonacci(n):
#   if n == 0:
#     return 0
#   elif n == 1:
#     return 1
#   else:
#     return fibonacci(n - 1) + fibonacci(n - 2)

# a=fibonacci()
# print(a)
# def discount_price(discount):
#     def price_asd(price):
#         price=price*(1-discount)
#         return price
#     return price_asd

# cost_15 = discount_price(0.15)
# cost_10 = discount_price(0.10)
# cost_05 = discount_price(0.05)

# price = 100
# print(cost_15(price))
# print(cost_10(price))
# print(cost_05(price))


# def normal_name(list_name):
#     a=map(lambda x: x.capitalize(), list_name)
#     return list(a)
    
    

# list_name=["dan", "jane", "steve", "mike"]
# a=normal_name(list_name)
# print(a)

# def get_emails(list_contacts):
#     # list=[]
#     a=map(list_contacts)
#     return list(a)
    
    
    
list_contacts=[{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}, 
          {
    "name": "dasdn Raymond",
    "email": "asdasd.ante@vestibul.co.uk",
    "phone": "(9asdsd2) 914-3792",
    "favorite": False,
}]

# email_list = list(map(lambda x: x["email"], list_contacts))
# print(email_list)
# for i in filter(lambda x: x % 2, range(1, 10 + 1)):
#     print(i)

# some_str = 'aaAbbB C F DDd EEe'
# for i in filter(lambda x: x.islower(), some_str):
#     print(i)

# for i in filter(lambda x: x>0, payment):
#     print(i)
# def positive_values(list_payment):
#     a=list(filter(lambda x: x>0, list_payment))
#     return a
# list_payment = [100, -3, 400, 35, -100]   
# a=positive_values(list_payment)
# print(a)
# def get_favorites(contacts):
#     a=list(filter(lambda x: x["favorite"], contacts))
#     return a

# contacts=[{
#     "name": "Allen Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
# }, {
#     "name": "Alqwden Raymond",
#     "email": "nqwdla.ante@vestibul.co.uk",
#     "phone": "(9qwd2) 914-3792",
#     "favorite": True}]
# a=get_favorites(contacts)
# print(a)

from functools import reduce


# def sum_numbers(numbers):
#     num=[x for x in numbers if x>0]
#     a=reduce((lambda x, y: x+y), num)
#     return a
# numbers=[1, -2, 3]


# b=sum_numbers(numbers)
# print(b)

class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates
        

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value==None:
            return self.coordinates.x, self.coordinates.y
        return self.coordinates.x*value, self.coordinates.y*value   
    
    def __add__(self, vector):
       vector.coordinates.x = vector
       vector.coordinates.y = vector
       self=(self.coordinates.x+vector.coordinates.x, self.coordinates.y+vector.coordinates.y)
       return self   
 
    def __sub__(self, vector):
       vector.coordinates.x = vector
       vector.coordinates.y = vector
       self=(self.coordinates.x-vector.coordinates.x, self.coordinates.y-vector.coordinates.y)
       return self   

        
    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"
    
vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

vector3 = vector2 + vector1
vector4 = vector2 - vector1

print(vector3)
print(vector4)