#Fahrentheit to centigrade
import time



print('Fahrentheit to Centigrade converter')
time.sleep(1.5)
print('Choose convertion: \n')
time.sleep(1.5)
print('Fahrentheit to Celcius')
time.sleep(0.8)
print('Celcius to Fahrentheit')
time.sleep(0.8)
print('\nType "F" if you want to convert Fahrentheits or "C" if Celcius\n')

choice = input('(F/C): ')

while True:

    
    if choice == 'F':
        
        another_one = 'yes'
        
        while True:
        
            if another_one == 'yes':
                fahrentheit_text = input('\nInput value in fahrentheits to convert: ')
                fahrentheit_int = int(fahrentheit_text)
            
                conversion_to_centigrade = round((fahrentheit_int - 32)/1.8,3)

                print('',fahrentheit_int,'\tFahrentheits are equal to:\n',conversion_to_centigrade,'\tCelcius')
                another_one = input('\nOnce again?: (yes/no) ')
                
            elif another_one == 'no':
                break

            else:
                print('Ups, you may typed wrong value')
                another_one = input('Try again: (yes/no) ')

    elif choice == 'C':
        
        another_one = 'yes'

        while True:

            if another_one == 'yes':
                celcius_text = input('\nInput value in centigrades to convert: ')
                celcius_int = int(celcius_text)

                convertion_to_fahrentheit = round((celcius_int*1.8)+32,1)

                print('',celcius_int,'\tCentigrades are equal to:\n',convertion_to_fahrentheit,'\tFahrentheits')
                another_one = input('\nOnce again?: (yes/no) ')
                
            elif another_one == 'no':
                break
            
            else:
                print('Ups, you may typed wrong value')
                another_one = input('Try again: (yes/no) ')
    
    print('Do you want to change convertion?')
    choice = input('(F/C): ')

    if choice != 'F' and choice != 'C':
        break
        
input('Press ENTER to exit')
