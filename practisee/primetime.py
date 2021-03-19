def isprime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count + 1
    if count==2:
        return True
    return False
number_of_hours_day, number_of_parts_day = map(int,input().split())
duration_each_day_part = number_of_hours_day / number_of_parts_day
primes=[]
equiprimeinstances=0

for hours in range(2, number_of_hours_day + 1):
    if isprime(hours):
        primes.append(hours)

for prime in primes:
    equiprimes=0
    individual_instance=prime
    if prime<=duration_each_day_part:
        for part in range(number_of_parts_day-1):
            print(prime)
            individual_instance += duration_each_day_part
            print(individual_instance)
            if individual_instance in primes :
                if individual_instance <= number_of_hours_day:
                    equiprimes += 1
                    
            #individual_instance -= prime
            print('-----------')

        if equiprimes==number_of_parts_day-1:
            equiprimeinstances+=1
            print(equiprimes)
            print('@@@@@@@@@@@@@')

    else:
        break

print(equiprimeinstances,end='')
