print("Tworzenie nowego użytkownika")

users_list = {}
user_name = input("\nPodaj nazwę użytkownika: ")

if user_name not in users_list:
    password = input("Podaj hasło: ")
    
    users_list.setdefault(user_name,password)
    print("\nStworzono nazwę użytkownika oraz przypisano podane hasło logowania")
    
while user_name in users_list:
    print("\nWitaj",user_name,"zaloguj się")
    password_log = input("Podaj hasło: ")
    
    if (user_name, password_log) in users_list.items():
        print("Zalogowano pomyślnie")
        break
    else:
        print("Nieudane logowanie")
        break
        


input('\n"ENTER" by zakończyć')
