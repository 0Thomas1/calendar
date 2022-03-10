"""
2021/03/09
prime No.
input any number and the script test if its a prime no.
and
find prime no.s in a range(biggest, smallest, middle)
and
TBC

"""




def check_input(num):
    """
    check if the input is an integer
    """
    if num //1 != 0:
        print("This is not a prime number.")

def check_prime(num):
    """
    check if the input no. is prime or not
    """
    #num_list = [0] * (num + 1)
    i = 2 
    remain = 1
    if num >= 0 and num <= 2:
        return False
    while i < num and remain != 0:
        remain = num % i
        i += 1
        #print(remain)
    if remain == 0:
        return False
    else:
        return True

def find_prime(lower, higher):
    """
    find all the prime no. in the range and organize them in a list
    """    
    num_list = list(range(higher + 1))
    del num_list[0:lower]
    prime_list = []
    i = 0
    print(num_list)
    while i < len(num_list):
        if check_prime(num_list[i]) is True:
            prime_list.append(num_list[i])
        i += 1

    print(prime_list)
        

def print_list(list):
    """
    print things
    """    
    print(list)
in_number = int(input("what is your number?"))
check_input(in_number)
#check_prime(in_number)
lower, higher = int(input("What is your range of numbers?")).split()
find_prime(lower, higher)