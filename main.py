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
    check if the input no. is prime or not,and return boolean expression
    """
    i = 2 
    remain = 1
    if num <= 1:
        return False
    while i < num and remain != 0:
        remain = num % i
        i += 1
    if remain == 0:
        return False
    else:
        return True

def find_prime(lower, higher):
    """
    find all the prime no. in the range and organize them in a list
    """    
    
    num_list = list(range(higher + 1))
    del num_list[:lower]
    prime_list = []
    
    print(num_list)
    for i in range(len(num_list)):
        if check_prime(num_list[i]) is True:
            prime_list.append(num_list[i])
        
    return prime_list
    
        

def print_list(list):
    """
    print things
    """    
    print(list)

def ini_programme():
    """
    interface to start each programme seperately
    and loop it
    """
    in_number = int(input("what is your number?"))
    if check_prime(in_number) is True:
        print(str(in_number) + " is a prime number.")
    else:
        print(str(in_number) + " is not a prime number.")

    lower = int(input("What is your lower range?"))
    higher = int(input("What is your upper range?"))
    print(find_prime(lower, higher))

    """print('Programme list: n\ 1: check prime  ')
    in_phrase = input("Which programme do you want to chose?")"""

ini_programme()

"""
in_number = int(input("what is your number?"))
check_prime(in_number)
lower = int(input("What is your lower range?"))
higher = int(input("What is your upper range?"))
find_prime(lower, higher)
"""