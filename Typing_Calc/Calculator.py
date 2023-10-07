from time import *
import random as r

def mistake(para, usertest):
    # to check test input and test1 
    error= 0 
    for i in range(len(para)):
        try:
            if para[i] != usertest[i]:
                error += 1
        except:
            error += 1

    return error 

def speed_time(time_s, time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed =  len(userinput)/time_R

    return round(speed)

if __name__ == '__main__':
    while True:
        check = input("Ready to Test: y/n\n")

        if check == "y" or check == 'Y':
            test = ["A paragraph is a self contained unit of discourse in writing dealing with a particular point or idea."
                    ,"My name is LocalHost" , "Welcome"]

            test1 = r.choice(test)
            print("\n*****Typing Speed Calculator*****")
            print(test1)
            print()
            print()
            time_1 = time()
            testinput = input(" Enter: ")
            time_2 = time()

            print('Spped: ', speed_time(time_1, time_2, testinput) , " w/sec")
            print("Error: " , mistake(test1, testinput))
        elif check == "N" or check == "n":
            print("Thanks for your time ")
            break
        else:
            print("Wrong Input")

