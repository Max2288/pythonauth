from hash_data import hash
def auth_user(file_name):
    with open(file_name,'r') as file:
        lst = file.readlines()
        for i in range(0,len(lst)):
             lst[i] =lst[i].replace('\n','')
        list_logins = [lst[i] for i in range(0,len(lst),2)]
        list_passwords = [lst[i] for i in range(1,len(lst)+1,2)]
        login_index = 0
        while True:
            user_name = input('Введите имя пользователя: ')
            for i in range(0,len(list_logins)):
                if list_logins[i] == user_name:
                    login_index = i
                    break                  
            else:
                print('Такого пользователя не существует! Повторите попытку.')
                continue
            break
        while True:
            user_password = input('Введите пароль: ')
            if hash(user_password) == list_passwords[login_index]:
                print('Авторизация успешна!')
                break
            else:
                print('Неверный пароль! Повторите попытку!')
                continue
auth_user('database.txt')
            
        
        