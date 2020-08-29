def __isPrime(num):
    if num > 1:
        # check for factors. if input number is less than or equal to 1, it is not prime
        # also if num % 2 != 0 its not a prime number
        for i in range(2,num):
            if (num % i) == 0:
                return False
                break
            else:
                return True
    else:
        return False

def __main__():
    num = int(input("Enter a number: "))
    if(__isPrime(num)):
        print("number ",num," is a prime number")
    else:
        print("number ",num," isnt a prime number")
        
__main__()
