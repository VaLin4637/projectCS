data = {25032:{'Name':'Naphop Khumchawna','Age':18,'money':10},24354:{'Name':'Veeraya Lekchaoum','Age':17,'money':40},74512:{'Name':'Klittima Chawwadee','Age':19,'money':50}}

user_id=int(input("Your ID : "))
money=data[user_id]['money']
name=data[user_id]['Name']
print(f'Hi {name} Your Balance is {money}')
topup=int(input('Topup : '))
money += topup
data[user_id]['money'] = money
print('Successfully ! ! ! ! ')
print('Thank You For Top Up')
print(f'Account : {name} Has Balance is {money}')