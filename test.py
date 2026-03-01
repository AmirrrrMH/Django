

# task coke.py
coin_1 = 5
coin_2 = 10
coin_3 = 25
cocakola = 50
# coins = [coin_1 ,coin_2 ,coin_3]
print("coin 1 = 5")
print("coin 2 = 10")
print("coin 3 = 25")
print("")
print("price of cocakola is 50 coin")
print("")
def get_coin_vorodi(a):
    User_input = int(input("enter a coin. (1/2/3): "))
    if User_input == 1:
        return coin_1
    elif User_input == 2:
        return coin_2
    elif User_input == 3:
        return coin_3
    else:print("error")
def agi_bmande(coins):
    print(f"bagi mande = {coins}")
def body_1(the_coin):
    baghi_monde_1 = 50
    while baghi_monde_1 > 0:
        bagi_mande(baghi_monde_1)
        coin = get_coin_vorodi()
        bagi_mande -= 1


body_1(2)