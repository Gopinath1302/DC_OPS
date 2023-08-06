# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 07/02/2023
# Last Modified Date : 07/08/2023
# Reviewed by        : Silpa Madhusoodanan
# Reviewed on        : 20/02/2023

import user
from user import User, Customer, Admin
from serviceitems import Service
from payment import Payment
from payment import Bill
from DB_connection import query_execute, check_db, close_db_connection


class Home:
    name = ""
    user_choices: int = 1

    # User-defined function to display homepage
    @staticmethod
    def dashboard(user_id=""):
        text = "-> home< -"
        print("_" * 105, "\n", text.center(105))
        text = "-> Dashboard <-"
        print("_" * 105, "\n", text.center(105))
        name = Home.fetch_name(user_id)
        role = Home.check_user_role(user_id)
        if role == 'ADMIN':
            Home.admin_side_dashboard(user_id, name)
        elif role == 'CUSTOMER':
            Home.customer_side_dashboard(user_id, name)
        else:
            Home.employee_side_dashboard(user_id, name)

    # User-defined function to Admin side dashboard
    @staticmethod
    def admin_side_dashboard(user_id, name):
        flag = True
        print(name, "  signed in @", Service.get_timestamp(3).strftime("%d-%m-%Y"), " " * 50, Service.get_timestamp(4))
        valid_choice = [1, 2, 3, 4, 5]
        prompt = '\n1.Add employee\n2.Remove employee\n3.View Employees\n4.View stats\n5.Sign out\n'
        user_choices = User.get_user_choice(prompt, valid_choice)
        if user_choices == 1:
            Admin.create_user()
        elif user_choices == 2:
            Admin.remove_employee()
        elif user_choices == 3:
            Admin.view_employees()
        elif user_choices == 4:
            pass
        elif user_choices == 5:
            flag = Home.sign_out(name)
        if flag:
            Home.admin_side_dashboard(user_id, name)
        pass

    # User-defined function to employee side dashboard
    @staticmethod
    def employee_side_dashboard(user_id, name):
        global user_choices
        flag = True
        valid_choice = [1, 2, 3, 4, 5]
        print(name, "  signed in @", Service.get_timestamp(3).strftime("%d-%m-%Y"), " " * 50, Service.get_timestamp(4))
        prompt = '\n1.Service request\n2.Update service status\n3.Calculate the service cost\n4.self-assign\n5.Sign out'
        user_choices = User.get_user_choice(prompt, valid_choice)
        if user_choices == 1:
            Service.view_all_service_request()
        elif user_choices == 2:
            pass
        elif user_choices == 3:
            pass
        elif user_choices == 4:
            pass
        elif user_choices == 5:
            flag = Home.sign_out(name)
        if flag:
            Home.dashboard(user_id)

    # User-defined function to customer side dashboard
    @staticmethod
    def customer_side_dashboard(user_id, name):
        flag = True
        valid_choice = [1, 2, 3, 4, 5, 6, 7]
        print(name, "  signed in @", Service.get_timestamp(3).strftime("%d-%m-%Y"), " " * 50, Service.get_timestamp(4))
        prompt = "\n1.View your details,\n2.Update your details\n3.Service your device \n4.Your last Service details " \
                 "\n5.Make your payment\n6.Notifications\n7.Sign off\n"
        user_choices = User.get_user_choice(prompt, valid_choice)
        if user_choices == 1:
            User.print_user_details(user_id)
        elif user_choices == 2:
            User.update_user_details(user_id)
        elif user_choices == 3:
            Service.rise_service_request(user_id, name)
            # Service.rise_request(user_id)
        elif user_choices == 4:
            Bill().print_details(name, user_id)
        elif user_choices == 5:
            total = Bill.calculate_total(user_id)
            status = Payment.payment_methods(total)
            Bill.update_payment_status(user_id, status)
        elif user_choices == 6:
            Home.check_notification(user_id)
        elif user_choices == 7:
            flag = Home.sign_out(name)
        if flag:
            Home.dashboard(user_id)

    # User-defined function to check user roles
    @staticmethod
    def check_user_role(user_id):
        case = user_id[0:3]
        role = ''
        if case == 'CUS':
            role = 'CUSTOMER'
        elif case == 'ADM':
            role = 'ADMIN'
        else:
            role = 'EMPLOYEE'
        return role

    # User-defined function to fetch username or name
    @staticmethod
    def fetch_name(user_id):
        name = ''
        query = "Select * from userdata where cus_id=%s;"
        values = (user_id,)
        result = query_execute(3, query, values)
        try:
            name = result[2] + " " + result[3]
        except TypeError:
            name = result[1]
        finally:
            return name

    # User-defined function to sig-out a user
    @classmethod
    def sign_out(cls, name):
        global user_choices
        text = "-> Sign-out <-"
        print("_" * 105,"\n",text.center(105))
        print("_" * 105)
        flag = True
        valid_choice = [1, 2]
        prompt = "\nExit Application or not ?\n 1.Yes\t2.No\n"
        while flag:
            user_choices = user.User.get_user_choice(prompt, valid_choice)
            if user_choices == 1:
                text1 = "-> Signed out Successfully! <-"
                text = name + " thanks for using this application"
                print(text1.center(105))
                print(text.center(105))
                close_db_connection()
                quit()
            elif user_choices == 2:
                flag = False
                return not flag


     # User-defined function to greet and authenticate a user
    @staticmethod
    def greeting():
        user_id = ""
        text = '-> Welcome to the Application <-'
        print("_" * 105, "\n",text.center(105))
        print("_" * 105, "\n")
        prompt = "\nExisting User ?\n\t1.Yes\t2.No\n"
        valid_choice = [1, 2]
        user_choices = User.get_user_choice(prompt, valid_choice)
        check_db()
        if user_choices == 1:
            user_id = User().sign_in()
        elif user_choices == 2:
            prompt1 = "Want to register as a user or exit the application?\n\t1.Sign-up\t2.Exit\n"
            user_choices = User.get_user_choice(prompt1, valid_choice)
            if user_choices == 1:
                Customer.create_user()
                user_id = User().sign_in()
            elif user_choices == 2:
                quit()
        Home.dashboard(user_id)

    # User-defined function to check for user's notifications
    @staticmethod
    def check_notification(user_id):
        text = "-> Notifications <-"
        print("_" * 105, "\n",text.center(105))
        print("_" * 105, "\n")
        prompt = "\t" * 6 + "1.You have a pending bill amount of : Rs "
        total = Bill.calculate_total(user_id)
        if total is not None:
            print(prompt, total, "\n")
            print("please navigate to make your payments to pay the remaining bill\n\n")
        else:
            print("You have no notification")
