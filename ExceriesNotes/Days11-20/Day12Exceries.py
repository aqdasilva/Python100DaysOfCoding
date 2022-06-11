# day 12: scope

# scope

# enemies = 1
#
# def increaseEnemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
# increaseEnemies()
# print(f"enemies outside function: {enemies}")

# local scope

# def drinkPotion():
#     potionStrength = 2
#     print(potionStrength)
#
#
# drinkPotion()

# global scope
# playerHealth = 10
#
#
# def game():
#     def drinkPotion():
#         potionStrength = 2
#         print(playerHealth)
#
#     drinkPotion()
#
#
# print(playerHealth)

# there is no block scope

# gameLevel = 3
#
#
# def createEnemy():
#     enemies = ["skeleton", "zombie", "alien"]
#     if gameLevel < 5:
#         newEnemy = enemies[0]
#     print(newEnemy)

# modify a global variable
# enemies = 1
#
#
# def increaseEnemies():
#     global enemies
#     enemies += 2
#     print(f"enemies inside function: {enemies}")
#
#
# increaseEnemies()
# print(f"enemies outside function: {enemies}")

#global cvo
pi = 3.14159
