balance = float(input("enter intial balance: "))
def desosit(balance):
  amount = float(input("enter intial balance: "))
  balance = balance + amount
  print("desosit successful. ")
  return balance

def withdraw(balance):
  amount = float(input("enter intial balance: "))
  if amount > balance:
    print("not enough balance")
  else:
   balance = balance - amount
  print("withdraw successful.")
  return balance

def check_balance (balance):
  print("current balance: " , balance)
  return

while True:
  print("1. desosit")
  print("2. withdraw")
  print("3. check balance")
  print("4. exit")
  choise = int(input("enter your choise: "))
  if choise == 1:
    balance = desosit(balance)
  elif choise == 2:
    balance = withdraw(balance)
  elif choise == 3:
    check_balance(balance)
  elif choise == 4:
    print("exiting program")
    break
  else:
    print("invalid choise")
                       
                         

