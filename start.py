import os

def main():
    os.system("behave features\SignUp.feature")
    os.system("behave features\Login.feature")
    os.system("behave features\HotelSearch.feature")
    os.system("behave features\Subscribe.feature")
    os.system("behave features\ContactUs.feature")





if __name__ == "__main__":
    main()