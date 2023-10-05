from math import sqrt 

def primes(N):
    nums = []
    for i in range(2, int(sqrt(N))+1): 
        if N % i != 0: 
            nums.append(i)
    return nums


# def primes(N):
#     nums = [] 
#     j = 2 
#     while j < int(sqrt(N)+1) and is_prime(j):
#         nums.append(j)
#         j += 1 
#     return max[nums] 

print(primes(65))




        

                   

            


        