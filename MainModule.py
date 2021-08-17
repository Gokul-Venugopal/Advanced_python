def is_prime(num):
    num_prime=True
    if num==1 or num==0:
         num_prime=False
    for i in range(2, (num)):
        if num % i==0:
            num_prime = False
            break
    return num_prime
