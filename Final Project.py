import sys
import re


class FoodOrderingSystem:
    def __init__(self):
        self.user_details = {}
        self.food_item = {}
        self.food_id = len(self.food_item) + 1
        self.foodOrder = []
        self.order = []

    def add_fooditem(self, FoodName, Quantity, Price, Discount, Stock):
        self.item = {
            "Food Name": FoodName,
            "Quantity": Quantity,
            "Price": Price,
            "Discount": Discount,
            "Stock": Stock,
        }
        self.food_id = len(self.food_item) + 1
        self.food_item[self.food_id] = self.item
        print("Item Added Successfully")
        return ""

    def edit_fooditem(self):
        self.food_item[1]["Food Name"] = "Tandoori Chicken"
        self.food_item[1]["Quantity"] = "4 pieces"
        self.food_item[1]["Price"] = "240"
        self.food_item[1]["Stock"] = "100"
        self.food_item[1]["Discount"] = "2"

        self.food_item[2]["Food Name"] = "Vegan Burger"
        self.food_item[2]["Quantity"] = "1 piece"
        self.food_item[2]["Price"] = "320"
        self.food_item[2]["Stock"] = "100"
        self.food_item[2]["Discount"] = "2"

        self.food_item[3]["Food Name"] = "Truffle Cake"
        self.food_item[3]["Quantity"] = "500gm"
        self.food_item[3]["Price"] = "900"
        self.food_item[3]["Stock"] = "100"
        self.food_item[3]["Discount"] = "2"
        return ""

    def delete_fooditem(self, food_id):
        if len(self.food_item) != 0:
            if self.food_id in self.food_item.keys():
                del self.food_item[self.food_id]
                print("\nDeleted Successfully\n")
            else:
                print("Invalid Food ID\n")
        return ""

    def view_fooditem(self):
        if len(self.food_item) != 0:
            for i in self.food_item:
                print(f"ID:{i}|Food Name:{self.food_item[i]['Food Name']}|Quantity:{self.food_item[i]['Quantity']}|Price:{self.food_item[i]['Price']}|Discount:{self.food_item[i]['Discount']}|Stock:{self.food_item[i]['Stock']}")
        else:
            print("\nNo Food Items Available to View")
        return ""

    def user_reg(self):
        try:
            self.name = input("Enter Your Full Name: ")
            while True:
                phonenum = input("Enter Your Phone Number: ")
                if phonenum.isnumeric() == True:
                    if len(phonenum) == 10:
                        self.phonenum = phonenum
                        break
                    else:
                        print("Invalid Phone Number\n")
                else:
                    print("Invalid Phone Number\n")
            while True:
                regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
                email = input("Enter Your Email  here: ")
                if re.fullmatch(regex, email):
                    self.email = email
                    break
                else:
                    print("Invalid Email")
            while True:
                print("Password must Contain min 8 characters")
                Password = input("Enter Your Password Here: ")
                if len(Password) >= 8:
                    self.Password = Password
                    break
                else:
                    print("Please Enter Minimum 8 Characters\n")
            self.address = input("Enter Your Address Here: ")
            self.user_details = {"NAME": self.name, "PHONE": self.phonenum, "EMAIL": self.email, "Password": self.Password, "ADDRESS": self.address}
            print("\nAccount Created Succsessfully \n")
        except Exception as e:
            print("Something Went Wrong\n")

    def user_login(self, email, Password):
        if len(self.user_details) > 0:
            if self.user_details["EMAIL"] == email and self.user_details["Password"] == Password:
                print("Login successfully!")
                print(f"Welcome {self.user_details['NAME']}")
                return True
            else:
                print("Check email and Password again\n")
        else:
            print("This Email Is Not Registered With Us. Please Register First")
        return ""

    def user_displayprofile(self):
        print(f" Name:{self.user_details['NAME']}\n Phone Number:{self.user_details['PHONE']}\n EMAIL:{self.user_details['EMAIL']}\n ADDRESS:{self.user_details['ADDRESS']}\n ")
        return ""

    def user_updateprofile(self, Password):
        if self.user_details["Password"] == Password:
            while True:
                print("1.Update Your Name")
                print("2.Update Your Phone Number")
                print("3.Upadte Your Email")
                print("4.Update Your Address")
                print("5.Update Your Password")
                print("6.Back")
                upchoice = input("Enter Your Choice: ")
                if upchoice == "1":
                    newname = input("Enter new Name: ")
                    self.user_details["NAME"] = newname
                    print(" Name Updated")
                elif upchoice == "2":
                    newnum = input("Enter new Number: ")
                    if newnum.isnumeric() == True:
                        if len(newnum) == 10:
                            self.user_details["PHONE"] = newnum
                            print("Phone Number Updated")
                            break
                        else:
                            print("Invalid Phone Number")
                    else:
                        print("Invalid Phone Number")
                elif upchoice == "3":
                    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
                    newemail = input("Enter Your Email  here: ")
                    if re.fullmatch(regex, newemail):
                        self.user_details["EMAIL"] = newemail
                        print("Email Updated")
                        break
                    else:
                        print("Invalid Email")
                elif upchoice == "4":
                    newadd = input("Enter new Address: ")
                    self.user_details["ADDRESS"] = newadd
                    print("Address Upadted")
                elif upchoice == "5":
                    print("Password must Contain min 8 characters")
                    while True:
                        newpass = input("Enter new Password: ")
                        if len(newpass) >= 8:
                            self.user_details["Password"] = newpass
                            print("Password Updated")
                            break
                        else:
                            print("Please Enter Minimum 8 Characters")
                elif upchoice == "6":
                    break
                else:
                    print("Invalid")
        else:
            print("Wrong Password. Enter Valid Password To continue")
        return ""

    def user_placeorder(self):
        print("1", {self.food_item[1]["Food Name"]} | {self.food_item[1]["Quantity"]} | {self.food_item[1]["Price"]} | {self.food_item[1]["Discount"]})
        print("2", {self.food_item[2]["Food Name"]} | {self.food_item[2]["Quantity"]} | {self.food_item[2]["Price"]} | {self.food_item[2]["Discount"]})
        print("3", {self.food_item[3]["Food Name"]} | {self.food_item[3]["Quantity"]} | {self.food_item[3]["Price"]} | {self.food_item[3]["Discount"]})
        print("4", {self.food_item[4]["Food Name"]} | {self.food_item[4]["Quantity"]} | {self.food_item[4]["Price"]} | {self.food_item[4]["Discount"]})
        print("5", {self.food_item[5]["Food Name"]} | {self.food_item[5]["Quantity"]} | {self.food_item[5]["Price"]} | {self.food_item[5]["Discount"]})
        print("0 For End")
        print("P -- To Place Order")
        op = 1
        while op != 0:
            op = input("Enter Choice For Placing Order: ")
            if op == "1":
                foodOrder.append(self.food_item[1]["Food Name"])
            elif op == "2":
                foodOrder.append(self.food_item[2]["Food Name"])
            elif op == "3":
                foodOrder.append(self.food_item[3]["Food Name"])
            elif op == "4":
                foodOrder.append(self.food_item[4]["Food Name"])
            elif op == "5":
                foodOrder.append(self.food_item[5]["Food Name"])
            elif op == "P" or op == "p":
                print(foodOrder)
            else:
                break
        return ""


obj = FoodOrderingSystem()
print(obj.add_fooditem("Idli", "2 pieces", "30", "2", "200"))
print(obj.add_fooditem("Dosa", "1 piece", "45", "5", "100"))
print(obj.add_fooditem("Upma", "1 cup", "20", "2", "100"))
print(obj.add_fooditem("Pongal", "1 cup", "30", "4", "200"))
print(obj.add_fooditem("Vada", "3 pieces", "60", "3", "300"))
print(obj.add_fooditem("Ponganalu", "6 pieces", "60", "5", "600"))
print("*" * 100)
print("The Food Items are:")
obj.view_fooditem()
print("*" * 100)
print(obj.edit_fooditem())
print("The Updated Food Items After Editing are:")
obj.view_fooditem()
print("*" * 100)
print("Deleting Food Details of ID 6")
obj.delete_fooditem(5)
print("The Updated Food Items After Delettion are:")
obj.view_fooditem()
print("*" * 200)
print("*" * 200)

while True:
    print("\n1. User Registration")
    print("2. User Login")
    print("3. Exit")
    uinput = input("Enter Your Selection: ")
    if uinput == "1":
        obj.user_reg()
    elif uinput == "2":
        email = input("Enter Your Registered Email Here: ")
        Password = input("Enter Your Password: ")
        if obj.user_login("sriharshareddy@gmail.com", "Harsha2000"):
            while True:
                foodOrder = []
                order = {}
                print("1. Place Order")
                print("2. Show Order History")
                print("3. Show Profile Details")
                print("4. Edit Profile Details")
                print("5. Back")
                uinput1 = input("Enter Your Choice: ")
                if uinput1 == "3":
                    print(obj.user_displayprofile())
                elif uinput1 == "4":
                    print(obj.user_updateprofile("Harsha2000"))
                    print("Updated Profile Detials:", obj.user_displayprofile())
                elif uinput1 == "1":
                    print(obj.user_placeorder())
                elif uinput1 == "2":
                    print(foodOrder)
    else:
        print("Thank You")
        sys.exit()


