import random
hp=100
attack=10
coins=0
potions=3
monsters=["Goblin","Skeleton","Zombie","Orc"]
print("===== MONSTER BATTLE =====")
while hp>0:
 print("\n1. Fight")
 print("2. Stats")
 print("3. Shop")
 print("4. Quit")
 choice=input("Choose: ")
 if choice=="1":
  monster=random.choice(monsters)
  monster_hp=random.randint(30,60)
  print(f"\nA {monster} appeared")
  while monster_hp>0 and hp>0:
   print(f"\nYour HP: {hp}")
   print(f"{monster} HP: {monster_hp}")
   print("1. Attack")
   print("2. Heal")
   action=input("Choose:")
   if action=="1":
    damage=random.randint(attack-2,attack+5)
    monster_hp-=damage
    print(f"You dealt {damage} damage")
    if monster_hp>0:
     damage=random.randint(5,15)
     hp-=damage
     print(f"The {monster} hit you for {damage} damage")
   elif action=="2":
    if potions>0:
     hp=min(100,hp+25)
     potions-=1
     print("You healed 25 HP")
    else:
     print("You have no potions")
   else:
    print("Invalid choice")
  if hp<=0:
   print("\n YOU Lost")
  else:
   reward=random.randint(10,25)
   coins+=reward
   print(f"\nYou defeated the {monster}")
   print(f"You earned {reward} coins")
 elif choice=="2":
  print("\n===== STATS =====")
  print(f"HP: {hp}/100")
  print(f"Attack: {attack}")
  print(f"Coins: {coins}")
  print(f"Potions: {potions}")
 elif choice=="3":
  print("\n===== SHOP =====")
  print("1. Potion - 10 coins")
  print("2. Attack +5 - 25 coins")
  shop=input("Choose: ")
  if shop=="1" and coins>=10:
   coins-=10
   potions+=1
   print("You bought a potion")
  elif shop=="2" and coins>=25:
   coins-=25
   attack+=5
   print("Your attack increased")
  else:
   print("Not enough coins")
 elif choice=="4":
  print("Thanks for playing")
  break
 else:
  print("Invalid choice")