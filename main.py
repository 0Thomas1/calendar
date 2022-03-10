"""
2021/03/09
prime No.
input any number and the script test if its a prime no.
or 
find prime no.s in a range(biggest, smallest, middle)
"""


in_number = input("what is your number?")

def check_input(num):
    if num //1 != 0:
        print("This is not a prime number.")

def check_prime(num):
    num_list = [0] * (num + 1)
    i = 0 
    while i < len(num_list):
        num_list[i] = i
        i += 1
    #print(num_list)
    first = 1
    last = -1
    

check_prime(20)