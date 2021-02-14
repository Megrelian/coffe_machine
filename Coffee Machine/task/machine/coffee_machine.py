class CoffeeMachine:
    water = 400
    milk = 540
    coffee = 120
    cups = 9
    money = 550

    supply_list = [water, milk, coffee, cups, money]

    inp_string = ""

    def __init__(self):

        def print_supply(wat, mil, coff, cup, mon):
            print("The coffee machine has:")
            print(wat, "of water")
            print(mil, "of milk")
            print(coff, "of coffee beans")
            print(cup, "of disposable cups")
            print("$" + str(mon), "of money")

        def check_for_resource(wat=0, mil=0, coffe=0, cup=0):
            if self.supply_list[0] - wat < 0:
                print("Sorry, not enough water!")
                return False
            elif self.supply_list[1] - mil < 0:
                print("Sorry, not enough milk")
                return False
            elif self.supply_list[2] - coffe < 0:
                print("Sorry, not enough coffee beans")
                return False
            elif self.supply_list[3] - cup < 0:
                print("Sorry, not enough disposable cups")
                return False
            else:
                return True

        def main_action(self,):
            while self.inp_string != "exit":
                self.inp_string = input("Write action (buy, fill, take, remaining, exit):\n")
                if self.inp_string == "remaining":
                    print_supply(self.supply_list[0], self.supply_list[1], self.supply_list[2], self.supply_list[3], self.supply_list[4])
                elif self.inp_string == "buy":
                    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                    option = input()
                    if option == "1":
                        if check_for_resource(wat=250, coffe=16, cup=1):
                            print("I have enough resources, making you a coffee!")
                            self.supply_list[0] = self.supply_list[0] - 250
                            self.supply_list[2] = self.supply_list[2] - 16
                            self.supply_list[3] = self.supply_list[3] - 1
                            self.supply_list[4] = self.supply_list[4] + 4
                    elif option == "2":
                        if check_for_resource(wat=350, coffe=20, cup=1, mil=75):
                            print("I have enough resources, making you a coffee!")
                            self.supply_list[0] = self.supply_list[0] - 350
                            self.supply_list[2] = self.supply_list[2] - 20
                            self.supply_list[3] = self.supply_list[3] - 1
                            self.supply_list[4] = self.supply_list[4] + 7
                            self.supply_list[1] = self.supply_list[1] - 75
                    elif option == "3":
                        if check_for_resource(wat=200, coffe=20, cup=1, mil=100):
                            print("I have enough resources, making you a coffee!")
                            self.supply_list[0] = self.supply_list[0] - 200
                            self.supply_list[2] = self.supply_list[2] - 12
                            self.supply_list[3] = self.supply_list[3] - 1
                            self.supply_list[4] = self.supply_list[4] + 6
                            self.supply_list[1] = self.supply_list[1] - 100
                    elif option == "back":
                        continue
                elif self.inp_string == "fill":
                    inp_water = int(input("Write how many ml of water do you want to add:\n"))
                    self.supply_list[0] = self.supply_list[0] + inp_water
                    inp_milk = int(input("Write how many ml of milk do you want to add:\n"))
                    self.supply_list[1] = self.supply_list[1] + inp_milk
                    inp_coffee = int(input("Write how many grams of coffee beans do you want to add:\n"))
                    self.supply_list[2] = self.supply_list[2] + inp_coffee
                    inp_cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))
                    self.supply_list[3] = self.supply_list[3] + inp_cups
                elif self.inp_string == "remaining":
                    print_supply(wat=self.supply_list[0], mil=self.supply_list[1], coff=self.supply_list[2], cup=self.supply_list[3], mon=self.supply_list[4])
                elif self.inp_string == "take":
                    print("i gave you $" + str(self.supply_list[4]))
                    self.supply_list[4] = 0

        main_action(self)


cofee = CoffeeMachine()
