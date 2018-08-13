import dice_and_reroll
import time
import random
my_coins = 0




#variables above

def first_fight(health):
    my_attack = 10
    enemy_attack = 10
    my_heal = 25
    enemy_hardhit = 20
    enemy_moveset = [enemy_attack, enemy_hardhit]
    e_h = health[0]
    my_health = health[1]
    fight_sequence = input('hit or heal?\n')
    if fight_sequence == 'hit':
        e_h = e_h - my_attack
        print('enemy has taken 10 damage! enemy now has', e_h, 'health left')
        time.sleep(2)
        enemy_decision = random.choice(enemy_moveset)
        my_health = my_health - enemy_decision
        print('enemy hits you dealing', enemy_decision, 'damage') 
        time.sleep(2)
        print('you now have ', my_health, '/100 hp left')
    elif fight_sequence == 'heal':
        my_health = my_health + my_heal
        if my_health > 100:
            my_health = 100
        print('You feel vigorous, you have healed your health to', my_health, '/100 hp' )
        enemy_decision = random.choice(enemy_moveset)
        my_health = my_health - enemy_decision
        print('enemy hits you dealing', enemy_decision, 'damage\n you now have ', my_health, '/100 hp left')
    healthout = (e_h,my_health)
    return healthout
my_health = 100
enemy_health = 100
healthx = (enemy_health,my_health)

while healthx[1] > 1 and healthx[0] > 1:
    healthx = first_fight(healthx)
    time.sleep(2)
if healthx[1] < 1:
    print('you lost')
else:
    print('you won')
    my_coins = my_coins + 10
    print('you now have', my_coins,'coins!')



