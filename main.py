import gyros
max = gyros.maxsize
min = -gyros.maxsize - 250 #grams

import tomato
max = tomato.maxsize
min = -tomato.maxsize - 3 #tomatoes

import tzatziki
max = tzatziki.maxsize
min = -tzatziki.maxsize - 5 #grams

import fernch_fries
max = fernch_fries.maxsize
min = -fernch_fries.maxsize - 15 #french fries


print("Hello Kostas, how are you today?")
print("Soublakomaker is starting")

print("How much gyro do you have?")
user_input == input()
print("You have, " + user_input + "grams of gyro")

print("How much tomato do you have?")
user_input == input()
print("You have, " + user_input + "tomatoes")

print("How much tzatziki do you have?")
user_input == input()
print("You have, " + user_input + "grams of tzatziki")

print("How many fernch fries do you have?")
user_input == input()
print("You have, " + user_input + "fernch fries")