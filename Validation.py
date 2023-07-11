class Validation:
    def validate(self):
        flag=1
        while flag:
            phone_No=str(input("Enter the phone Number:"))
            if(len(phone_No) == 10 and int(phone_No)>6000000000 and int(phone_No)<9999999999):
                break
            else:
                print("?????????????InValid phone number??????????????")
