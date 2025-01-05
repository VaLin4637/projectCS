from random import * 
data = {25032:{'Name':'Naphop Khumchawna','Age':18},24354:{'Name':'Veeraya Lekchaaum','Age':17},74512:{'Name':'Klittima Chawwadee','Age':19}}
def gen_id():
    id = lambda x : str(randint(0,9))
    num = (''.join([id(i)for i in range (5)]))
    if num in data.keys():
        print('This Name Is On Our Database')
        num = (''.join([id(i)for i in range (5)]))
    print(num)
    return num

def register():
    while True:
        try:
            id = gen_id()
            name = str(input("Your Name is : "))
            surname = str(input('Your Surname is : '))
            age = int(input("Your Age is : "))    
            fullname = name+' '+surname
            for id_member in data.keys():
                if fullname == data[id_member]['Name']:
                    print('Has IT') 
                    register() 
            data[id] = {
                'Name':fullname,
                'Age':age
                }
            con = str(input('Continue ? : '))
            if con.lower()=='n':
                break
            elif con.lower() == 'y':
                register()
            print(data)
        except ValueError: 
            print('Your Age Should Be Number Please Try Again')
        except KeyboardInterrupt:
            print('\n')
            break


while True :
    print('Programe\n[0]Exit\n[1]Register')
    choose = int(input('Choose : '))
    match choose:
        case 0 :
            break
        case 1 :
            register()
