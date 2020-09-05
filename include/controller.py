#!/usr/bin/env python3.7
import os
import sys
from random import *
import time

# import card

#-----------------------------------------------------
card_status = 'notpresent'
pin_number = ''
account = ''
balance = 0
deposit = 0
withdraw = 0

def read_card():

    global card_status
    print("")
    print("------------------------------")
    # card_status = sys.argv[1]
    print("-> Insert card 'present' for card inserted")
    card_status = input("-> status: ")
    if card_status == 'present':
        print("-> card inserted!")
        return True
    else:
        card_status = 'notpresent'
        print("-> card not inserted!")
        return False

def read_pinNumber():
    global pin_number
    print("")
    print("------------------------------")
    pin_number = input("-> insert pin number: ")
    print("-> cheking pin number...please wait")
    if not pin_number.isnumeric():
        print("-> pin number is not valid!")
        return False
    else:
        if len(pin_number) != 4:
            print("-> pin number must be 4 digits!")
            return False
        print("-> pin number is: OK")
        return True

def selectAccount():
    global account
    print("")
    print("------------------------------")
    print("-> select account between 'current' or 'savings'")
    account = input("-> account: ")
    if account == 'current':
        print("-> account selected: " + account)
        return True
    elif account == 'savings':
        print("-> account selected: " + account)
        return True
    else:
        print("-> select between 'current' or 'savings'!")
        return False

def select_action():
    option = ''
    global balance
    global deposit
    global withdraw

    print("")
    print("------------------------------")
    option = input("-> Please select action between 'balance', 'deposit' or 'withdraw': ")
    if option == 'balance':
        balance = randint(0, 5000)    # random number between 0 and 5000 euros.
        print("processing...")
        time.sleep(2) # Wait for 5 seconds
        print_receipt()
        time.sleep(4) # Wait for 5 seconds
        print("-> balance: ",balance)
        return True
    elif option == 'deposit':
        deposit = input("-> Please insert amount to deposit (max 1000): ")
        if not deposit.isnumeric():
            print("-> deposit amount is not valid!")
            return False
        else:
            if int(deposit) > 1000:
                print("-> deposit amount is not valid, maximum 1000")
                return False
            else:
                print("processing...")
                time.sleep(2) # Wait for 5 seconds
                print_receipt()
                time.sleep(4) # Wait for 5 seconds
                print("-> deposit: ", deposit)

        return True
    elif option == 'withdraw':
        withdraw = input("-> Please insert amount to withdraw (max 200): ")
        if not withdraw.isnumeric():
            print("-> withdraw amount is not valid!")
            return False
        else:
            if int(withdraw) > 200:
                print("-> withdraw amount is not valid, maximum 200")
                return False
            else:
                print("processing...")
                time.sleep(2) # Wait for 5 seconds
                print_receipt()
                time.sleep(4) # Wait for 5 seconds
                print("-> withdraw: ", withdraw)

        return True
    else:
        print("-> select between 'Balance', 'Deposit' or 'Withdraw'!")
        return False

def print_receipt():
    print("")
    print("------------------------------")
    option = input("Do you want to print receipt? (y/n): ")
    if option == 'y':
        print("processing...")
        time.sleep(4) # Wait for 5 seconds
        return True
    elif option == 'n':
        print("Closed transaction")
        return False
    else:
        print("select between 'y' for yes or 'n' for not!")
        return True

def continue_action():
    print("")
    print("------------------------------")
    option = input("Do you want to make another transaction? (y/n): ")
    if option == 'y':
        return True
    elif option == 'n':
        print("Closed transaction")
        return False
    else:
        print("select between 'y' for yes or 'n' for not!")
        return True

def test_controller():
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("***   Testing ATM controller      ***")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    while(1):
        if not read_card():
            time.sleep(3) # Wait for 5 seconds
        else:
            time.sleep(4) # Wait for 5 seconds

            # Checking pin number
            while(1):
                if read_pinNumber():
                    time.sleep(2) # Wait for 5 seconds
                    break

            # Loop for action
            while(1):

                # Selecting account
                while(1):
                    if selectAccount():
                        time.sleep(2) # Wait for 5 seconds
                        break

                # Selecting action
                while(1):
                    if select_action():
                        time.sleep(2) # Wait for 5 seconds
                        break

                if not continue_action():
                    time.sleep(2) # Wait for 5 seconds
                    break
