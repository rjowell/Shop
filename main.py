
items = ["iPhone","Oculus Headset","AirPods","Massage Gun","Air Fryer"]
prices = [600,1000,75,125,400]
currentCart = []
currentTotal = 0
print("Welcome to CONGO, Mr. Russ' healthier alternative to Amazon")



def checkout():
  global currentTotal
  for items in currentCart:
    if items == "iPhone":
      currentTotal += 600
    if items == "Oculus Headset":
      currentTotal += 1000
    if items == "AirPods":
      currentTotal += 75
    if items == "Massage Gun":
      currentTotal += 125
    if items == "Air Fryer":
      currentTotal += 400
  print("TOTAL: $"+str(currentTotal))
  wantToPay = input("Do you want to pay now?")
  if wantToPay == "Yes":
    print("Thanks, payment received. Have a great day!")


def shop():
  print("ITEMS AVAILABLE:")
  print("1 - iPhone ($600)")
  print("2 - Oculus Headset ($1000)")
  print("3 - AirPods ($75)")
  print("4 - Massage Gun ($125)")
  print("5 - Air Fryer ($400)")
  userChoice = input("Which item do you want?\r\n")
  currentCart.append(items[int(userChoice)-1])
  keepGoing = input("Do you want to Keep (S)hopping or (C)heckout?\r\n")
  if keepGoing == "S":
    return shop()
  elif keepGoing == "C":
    return checkout()
  else:
    return homeScreen()

def homeScreen():
  print("----------------------------")
  print("Items in Cart: "+str(len(currentCart)))
  print("----------------------------")
  print("What do you want to do?")
  firstInput = input("A - SHOP B - CHECKOUT\r\n")
  if firstInput == "A":
    return shop()
  elif firstInput == "B":
    return checkout()
  else:
    print("Please try again!")
    return homeScreen()

homeScreen()

