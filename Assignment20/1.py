total_money=0.00

def options(money):
    print("A packet of candy costs $ 1.50. You have inserted $ %.2f." % (total_money))
    print("Please insert coins:")
    print ("\tn - Nickel")
    print("\td - Dime")
    print("\tq - Quarter")
    print("\tD - Dollar")

def check_total(total_money):
    if total_money >= 1.50:
        ret_money = total_money - 1.50
        print ("Enjoy your candies. Your change is $ %.2f. Please visit again." % (ret_money))
        return True

def inserted(total_money, ins_money):
    if ins_money == "n":
        total_money += 0.05
    elif ins_money == "d":
        total_money += 0.1
    elif ins_money == "q":
        total_money +=0.25
    elif ins_money == "D":
        total_money += 1
    else:
        print("'"+ ins_money + "' is not a valid coin.")
    return total_money


while True:
    if check_total(total_money):
        break
    options(total_money)
    ins_money = str(input())
    total_money = inserted(total_money, ins_money)