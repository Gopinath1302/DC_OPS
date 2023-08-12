# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 07/02/2023
# Last Modified Date : 07/08/2023
# Reviewed by        : Silpa Madhusoodanan
# Reviewed on        : 20/02/2023

import re
from user import User
from DB_connection import query_execute, loading_animation
from datetime import date, datetime


class Service:
    __service_price = 1000
    __service = "Nominal service Charges"

    # User-defined function to check where a user is eligible to get a service or not
    @staticmethod
    def check_service_eligible(customer_id):
        query = "Select sum(price) from service where cus_id = %s and p_status = 'Pending';"
        result = query_execute(3, query, (customer_id,))
        try:
            if result[0] > 10500:
                status = True
        except TypeError:
            status = True
        else:
            if result[0] > 10000:
                status = False
            else:
                status = True
        return status

    # User-defined function to update a users request into the DB
    @classmethod
    def add_service(cls, __customer_id, date, timestamp, service_id):
        global service_price, service
        prompt = (
            "Enter the service you need...\n1.Hardware Service\tRs 5000\n2.Software Service\tRs 1500\n3.General "
            "Service\tRs 3000\n")
        valid_choice = [1, 2, 3]
        user_choice = User.get_user_choice(prompt, valid_choice)
        if user_choice == 1:
            service = 'Hardware Service'
            service_price = 5000
        elif user_choice == 2:
            service = "Software Service"
            service_price = 1500
        elif user_choice == 3:
            service = "General Service"
            service_price = 3000
        query = "insert into service values (%s, %s, %s, %s, %s, %s, 'Pending');"
        values = (__customer_id, service_id, service, service_price, date, timestamp)
        query_execute(1, query, values)

    # User-defined function to rise a service request
    @staticmethod
    def rise_service_request(__customer_id, name):
        status = Service.check_service_eligible(__customer_id)
        if not status:
            print("We are apologizing to say this, ", name,
                  "\nYou already having too many pending bills \nEnsure you pay the pending bills")
            return 0
        text = "-> Service initiation <-"
        print("_" * 105, "\n", text.center(105))
        print("_" * 105, "\n")
        timestamp = Service.get_timestamp(2)
        dates = Service.get_timestamp(3)
        service_id = Service.generate_service_id(__customer_id, name)
        query = "insert into service values ( %s, %s, 'Nominal Service', 1000, %s, %s, 'Pending');"
        values = (__customer_id, service_id, dates, timestamp)
        query_execute(1, query, values)
        Service.add_service(__customer_id, dates, timestamp, service_id)
        valid_choice = [1, 2]
        prompt = "Want to add another service \n 1.Yes or 2.No\n"
        while True:
            user_choice = User.get_user_choice(prompt, valid_choice)
            if user_choice == 1:
                print("\n")
                Service.add_service(__customer_id, dates, timestamp, service_id)
            elif user_choice == 2:
                loading_animation(1, word='Uploading data')
                break

    # User-defined function to generate a service ID
    @staticmethod
    def generate_service_id(__customer_id="", name=""):
        name = re.sub(r"\s+", " ", name)
        name = name.upper()
        value = str(Service.get_timestamp(4))
        value = value.replace("-", "")
        service_id = "SER" + name[:2] + value[:3:-1]
        return service_id
        # pass

    # User-defined function to perform Timestamping
    @staticmethod
    def get_timestamp(case=0):
        # gets the current timestamp
        value = datetime.now()
        timestamp = datetime.timestamp(value)
        # gets the current month
        current_month = value.month
        # gets the current year
        current_year = value.year
        # gets the current date
        value = date.today()
        # Format the datetime object as a string
        dt = datetime.fromtimestamp(timestamp)
        # Format the datetime object as a string
        formatted_datetime = dt.strftime("%Y-%m-%d %H:%M:%S")
        current_time = datetime.now().time()
        time_string = current_time.strftime("%I:%M:%S %p")
        # function call for timestamp
        if case == 1:
            return timestamp
        # function call for date and time
        elif case == 2:
            return formatted_datetime
        # function call for date
        elif case == 3:
            return value
        # function call for time with local format
        elif case == 4:
            return time_string
        # function call for time with current month
        elif case == 5:
            return current_month
        # function call for time with current year
        elif case == 6:
            return current_year

    # Under development
    # User-defined function to get a validated model name
    @staticmethod
    def get_model_name():
        global model
        flag = True
        while flag:
            model = input("Enter the Model name\n")
            if 0 < len(model) < 40:
                if Service.validate_name(2, model):
                    flag = False
                else:
                    flag = True
            else:
                flag = True
        return model

    # User-defined function to  validated model name
    @staticmethod
    def validate_name(case, name):
        pattern1 = r"^[A-Za-z\- ]+$"
        pattern2 = r"^[A-Za-z0-9\- ]+$"
        if case == 1:
            rule = re.compile(pattern1)
        else:
            rule = re.compile(pattern2)
        result = re.match(rule, name)
        if result is not None:
            return True
        else:
            return False

    # User-defined function to get a validated device name
    @staticmethod
    def get_device_name():
        flag = True
        device_name = ""
        prompt = "Please select the device category to which the device for servicing belongs\n\t\t1.Laptop\t\t\t\t\t\t2.Phone\n\t\t3.Earphones or Headphones\t\t4.Television\n\t\t5.Gaming consoles\t\t\t\t6.Personal Computers(Desktop pc)\n\t\t7.Smart watches\t\t\t\t\t8.Other\nSelect the device category\n"
        valid_choice = [1, 2, 3, 4, 5, 6, 7, 8]
        while flag:
            userchoices = User.get_user_choice(prompt, valid_choice)
            if userchoices == 1:
                device_name = 'Laptop'
                flag = False
            elif userchoices == 2:
                device_name = 'Phone'
                flag = False
            elif userchoices == 3:
                device_name = 'Earphones'
                flag = False
            elif userchoices == 4:
                device_name = 'Television'
                flag = False
            elif userchoices == 5:
                device_name = 'Console'
                flag = False
            elif userchoices == 6:
                device_name = 'Computers'
                flag = False
            elif userchoices == 7:
                device_name = 'Smart watch'
                flag = False
            elif userchoices == 8:
                device_name = input("Enter the device name\n")
                print(len(device_name))
                if 0 < len(device_name) < 50:
                    print(1)
                    if Service.validate_name(1, device_name):
                        flag = False
                    else:
                        flag = True
                else:
                    flag = True
        return device_name

    # User-defined function to get a validated defect details
    @staticmethod
    def get_defect_details():
        global defect
        flag = True
        while flag:
            defect = input("Explain the faults that encountered while using this device:\n")
            if 10 <= len(defect) <= 100:
                flag = False
            else:
                print("Defect description should be between 10 and 200 characters.")
        return defect

    # User-defined function to get a device usage
    @staticmethod
    def get_device_usage():
        flag = True
        prompt = "How do you use the device ?\n\t1.Minimal\t2.Nominal\t3.Extensive\n"
        valid_choices = [1, 2, 3]
        while flag:
            user_choice = User.get_user_choice(prompt, valid_choices)
            if user_choice == 1:
                usage = "Minimal"
                flag = False
            elif user_choice == 2:
                usage = "Nominal"
                flag = False
            elif user_choice == 3:
                usage = "Extensive"
                flag = False
            else:
                flag = True
        return usage

    # User-defined function to rise a detailed service request
    @staticmethod
    def rise_request(__customer_id=""):
        text = "-> Service initiation <-"
        print("_" * 105, "\n", text.center(105))
        print("_" * 105)
        time = Service.get_timestamp(2)
        device_name = Service.get_device_name()
        model_name = Service.get_model_name()
        defect_description = Service.get_defect_details()
        usaage = Service.get_device_usage()
        status = 'Initiated'
        dates = Service.get_timestamp(3)
        query = "insert into service_request values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        query1 = "insert into services values(%s, %s, %s, %s, %s, %s, %s , %s, %s)"
        service_id = Service.generate_service_id(__customer_id, model_name)
        print("1.CustomerID:", __customer_id, "\n2.ServiceID:", service_id, "\n3.Device name:", device_name,
              "\n4.Model name:",
              model_name, "\n5.Defect:", defect_description, "\n6.Usage:", usaage, "\n7.Time:", time)
        prompt = "please ensure where all your request details are correct\n\t1.Yes\t2.No\n"
        valid_choice = [1, 2]
        user_choice = User.get_user_choice(prompt, valid_choice)
        if user_choice == 2:
            prompt = "Do you need to update the details\n\t1.Yes\t2.No\n"
            user_choice = User.get_user_choice(prompt, valid_choice)
            if user_choice == 1:
                prompt = "Which details do you need to update?\n\t\t1.Device name\n\t\t2.Model name\n\t\t3.Defect\t\t4.Usage\n"
                valid_choice = [1, 2, 3, 4]
                user_choice = User.get_user_choice(prompt, valid_choice)
                if user_choice == 1:
                    device_name = Service.get_device_name()
                elif user_choice == 2:
                    model_name = Service.get_model_name()
                elif user_choice == 3:
                    defect_description = Service.get_defect_details()
                elif user_choice == 4:
                    usaage = Service.get_device_usage()
        data = (service_id, __customer_id, device_name, None, dates, status, 0, 'Waiting', time)
        values = (
            __customer_id, service_id, device_name, model_name, defect_description, usaage, status, time, 0, 'Pending')
        query_execute(1, query, values)
        query_execute(1, query1, data)
        print("The service request has been raised. Technicians will get to the linked address and collect the "
              "device with-in 1 or 2 working days\n so please verify the address\n")
        query = "Select * from address where cus_id = %s;"
        values = (__customer_id,)
        result = query_execute(3, query, values)
        value = result[1:7]
        for i in range(len(value)):
            if i < 1:
                print("Address:", value[i])
            else:
                print("\t\t", value[i])
        prompt = "\nAre you available in this address with the defective device\n\t1.Yes\t\t2.No\n"
        valid_choices = [1, 2]
        user_choice = User.get_user_choice(prompt, valid_choices)
        if user_choice == 2:
            print("Please update the address as soon as possible in the yours details")
            User.update_user_details()

    # User-defined function to view all the pending service requests
    @staticmethod
    def view_all_service_request():
        query = "select service_id, cus_id, device_name, price, s_status, sdate from services where s_status = 'Initiated';"
        result = query_execute(4, query, values=None)
        if not result:
            text = 'There are no new services currently'
            print(text.center(105))
        else:
            print("Service_id \t\t Customer_id \t\t Device_name \t  Price \t Service_status   Service_date")
            for row in result:
                list1 = row
                print(list1[0], " \t\t ", list1[1], " \t\t ", list1[2], " \t\t ", list1[3], " \t ", list1[4], " \t  ",
                      list1[5], )

    # User-defined function to view a detailed service request
    @staticmethod
    def view_service_request():
        query = "select ser_id, cus_id, device, model, defect, usaage, rstatus, time, price, p_status from service_request where  ser_id = %s ;"
        print("Enter the Service_id to fetch the details\n")
        service_id = input()
        values = (service_id,)
        result = query_execute(4, query, values)
        if not result:
            text = "There is no such new services with the entered Service_id: " + service_id
            print(text.center(105))
        else:
            # print("Service_id  Customer_id  Device_name \t  Price \t Service_status   Service_date")
            for row in result:
                list1 = row
                print("Service_Id\t\t\t:", list1[0], "\nCustomer_Id\t\t\t:", list1[1], "\nDevice_category \t:",
                      list1[2], " \nModel_Name\t\t\t:", list1[3], "\nDefect_description  :", list1[4],
                      " \nUsage\t\t\t\t:", list1[5], "\nService_status\t\t:", list1[6], " \nTime\t\t\t\t:", list1[7],
                      "\nPrice\t\t\t\t: ", list1[8], " \nPayment_status\t\t:", list1[9])
                return service_id

    # User-defined function to assign an employee to service request
    @staticmethod
    def assign_to_service(service_id, name):
        query = "select serviced_by, timestamp from services where service_id = %s;"
        values = (service_id,)
        result = query_execute(3, query, values)
        # print(result)
        if result is None:
            text = "There is no such new services with the entered Service_id: " + service_id
            print(text.center(105))
        elif result[0] is None:
            # print("assign")
            values = (name, service_id, result[1])
            # print(values)
            query = "update services set serviced_by = %s where service_id = %s and timestamp = %s "
            query_execute(2, query, values)
        else:
            text = "The services with the entered Service_id: " + service_id + ", has been already allowed"
            print(text.center(105))

    # User-defined function for employee to self-assign to service request
    @staticmethod
    def self_assign(name):
        Service.view_all_service_request()
        service_id = Service.view_service_request()
        Service.assign_to_service(service_id, name)

    @staticmethod
    def update_service_status(name, service_id):
        query = "select serviced_by, timestamp from services where service_by = %s;"
        values = (name,)
        result = query_execute(3, query, values)
        if result is None:
            text = "There is no such new services with the entered Service_id: " + service_id
            print(text.center(105))
        elif result[0] is None:
            # print("assign")
            values = (name, service_id, result[1])
            # print(values)
            query = "update services set serviced_by = %s where service_id = %s and timestamp = %s "
            query_execute(2, query, values)
        else:
            text = "The services with the entered Service_id: " + service_id + ", has been already allowed"
            print(text.center(105))
