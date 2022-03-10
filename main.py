"""
2021/03/09
prime No.
input any number and the script test if its a prime no.
or 
find prime no.s in a range(biggest, smallest, middle)
"""


in_number = int(input("what is your number?"))

def check_input(num):
    if num //1 != 0:
        print("This is not a prime number.")

def check_prime(num):
    """
    check if the input no. is prime or not
    """
    #num_list = [0] * (num + 1)
    i = 2 
    remain = 1
    while i < num and remain != 0:
        remain = num % i
        i += 1
        print(remain)
    if remain == 0:
        print("this is not a prime number.")
    else:
        print(str(num) +" is a prime number.")
    
    


check_prime(in_number)