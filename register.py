import string 
from hash_data import hash
def register_user(file_name):
    pun = set(string.punctuation)
    digit = set(string.digits)
    big_let = set(string.ascii_uppercase)
    smal_let = set(string.ascii_lowercase)
    with open(file_name,'r+') as file:
        lst = file.readlines()
        for i in range(0,len(lst)):
             lst[i] =lst[i].replace('\n','')
        list_logins = [lst[i] for i in range(0,len(lst),2)]
        while True:
            user_name = input('Введите имя пользователя: ')
            if user_name in list_logins:
                print('Имя пользователя занято введите новое! ')
                continue
            else:
                file.write(str(user_name)+ '\n')
                break
        while True:
            user_pass = input("Введите пароль: ")
            user_s = set(user_pass)
            if len(user_s & pun) > 0 and len(user_s & digit) > 0 and len(user_s & big_let) > 0 and len(user_s & smal_let) > 0 and len(user_pass)>=8:
                file.write(hash(user_pass) + '\n')
                print('Вы успешно зарегистрировались!')
                break
            else:
                print("Некоректный пароль! Попробуйте сложнее.")
                
register_user('database.txt')