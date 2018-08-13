import time
import random
money_owned = [1,10,20,30,40,50]
x = random.choice(money_owned)
print('you have',x,'dollars')
drive = input('Would you like to go to the mall or the hotdog stand?')
if drive == 'mall':
    print('driving to the mall...')
    time.sleep(3)
    mall_shopping = input('would you like to buy a nail(1$), a hammer(10$) or a drill(25$)')
    if mall_shopping == 'nail':
        money_owned = money_owned - 1
        if money_owned < 0:
            money_owned = money_owned + 1
            print('you do not have enough money for this item your money remains the same.')
        print(money_owned)
    elif mall_shopping == 'hammer':
        money_owned = money_owned - 10
        if money_owned < 0:
            money_owned = money_owned + 10
            print('you do not have enough money for this item your money remains the same.')
        print(money_owned)
    elif mall_shopping == 'drill':
        money_owned = money_owned - 25
        if money_owned < 0:
            money_owned = money_owned + 25
            print('you do not have enough money for this item your money remains the same.')
        print(money_owned)
    drive = input('you can go to the hotdog stand on the way home would you like to go home or to the hotdog stand')
if drive == 'hotdog stand':
    time.sleep(3)
    hotdog_shopping = input('would you like a hotdog(3$)')
if hotdog_shopping == 'yes':
        money_owned = money_owned - 3
        if money_owned < 0:
            money_owned = money_owned + 3
            print('you do not have enough money for this item your money remains the same.')
print('you have',money_owned, 'dollars leftover.')
