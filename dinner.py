import random

x = {}
x[1] = "Cyclone Anayas"
x[2] = "Indian Food"
x[3] = "Wings"
x[4] = "mediterranean"
x[5] = "Colombian"
x[6] = "5guys" 
x[7] = "sushi"
x[8] = "pizza"
x[9] = "tacos"
x[10] = "macdonalds"


picker = random.randint(1, 11)

print("Your dinner tonight will be " + str(x[picker]))

#for x in range(10):
#  print random.randint(1,101)
