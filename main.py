"""
2021/03/09
prime No.
input any number and the script test if its a prime no.
and
find prime no.s in a range(biggest, smallest, middle)
and
TBC

"""




from pickle import APPEND


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

def prime_lst_input():
    lower = int(input("What is your lower range?"))
    higher = int(input("What is your upper range?"))
    prime_lst = find_prime(lower, higher)
    return prime_lst


def twin_primes(lst):
    """
    from a sorted prime list, find all twin primes
    """
    twin_prime_lst = []
    for i in range(len(lst)-1):
        if lst[i+1] - lst[i] == 2:
            twin_prime_lst.append(lst[i])
            twin_prime_lst.append(lst[i+1])
            
            print_list(twin_prime_lst)
    
        


twin_primes(prime_lst_input())
