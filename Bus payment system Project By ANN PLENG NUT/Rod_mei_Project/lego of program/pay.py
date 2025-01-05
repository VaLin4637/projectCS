data = {25032:{'Name':'Naphop Khumchawna','Age':18,'money':60},24354:{'Name':'Veeraya Lekchaaum','Age':17,'money':40},74512:{'Name':'Klittima Chawwadee','Age':19,'money':50}}
bus_stop = {1:{'BName':'Busta Shinjuku','Price':5},2:{'BName':'Tomigaya','Price':10},3:{'BName':'Sakurabashi','Price':15},4:{'BName':'Namsan Seoul Tower','Price':20},5:{'BName':'Seoul Arts Center','Price':25},6:{'BName':'Myeong-dong Entrance','Price':30},7:{'BName':'Seoul Square','Price':35},8:{'BName':'Bridge St','Price':40},9:{'BName':'Manchester Coach Station','Price':45},10:{'BName':'Manchester Shudehill','Price':50}}
user_id=int(input("Your ID :"))
def Pay():
    user_id=int(input("Your ID :"))
    print(f'HI {data[user_id]["Name"]} Stable : {data[user_id]["money"]}')
    print(data)
    money=data[user_id]['money']
    for select in bus_stop.keys():
        print(select,bus_stop[select]['BName'])

    start=int(input("Choose Start Station : "))
    stop=int(input("Choose Stop Station : "))
    start_b = bus_stop[start]['BName']
    stop_b = bus_stop[stop]['BName']

    print(f'You are from {start_b} to {stop_b}')
    user_age = data[user_id]['Age']
    if user_age >=0 and user_age <= 20:
        rate = 3
    elif user_age >=21 and user_age <= 59:
        rate = 0
    else:
        rate = 2


    pay=bus_stop[stop]['Price']-bus_stop[start]['Price']
    if pay>data[user_id]['money']:
        print('Your balance ไม่พอ')
    else:
        pay_discount=bus_stop[stop]['Price']-bus_stop[start]['Price']-rate
        stable = data[user_id]['money']-pay_discount
        data[user_id]['money'] = stable
        print(f'\nYou Have Got in Your Account For {money}\nFull Price is {pay}\n You are {user_age} years old\n You Have Got The Discount for {rate}\n So you should pay for {pay_discount}\nYour Balance is {stable}')








