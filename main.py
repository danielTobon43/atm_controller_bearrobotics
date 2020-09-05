#!/usr/bin/env python3.7
import sys
import time

sys.path.append("include")
import controller

#-----------------------------------------------------

if __name__ == '__main__':

    if len(sys.argv) < 1:
        print("")
        print ("Usage python3.7 %s " % sys.argv[0])
        print("")
        sys.exit(1)

    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("***   ATM controller      ***")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    while(1):
        if not controller.read_card():
            time.sleep(3) # Wait for 5 seconds
        else:
            time.sleep(4) # Wait for 5 seconds

            # Checking pin number
            while(1):
                if controller.read_pinNumber():
                    time.sleep(2) # Wait for 5 seconds
                    break

            # Loop for action
            while(1):

                # Selecting account
                while(1):
                    if controller.selectAccount():
                        time.sleep(2) # Wait for 5 seconds
                        break

                # Selecting action
                while(1):
                    if controller.select_action():
                        time.sleep(2) # Wait for 5 seconds
                        break

                if not controller.continue_action():
                    time.sleep(2) # Wait for 5 seconds
                    break
