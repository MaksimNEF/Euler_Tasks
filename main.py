import time

# PROBLEM 1: Multiples of 3 or 5
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23 .
#Find the sum of all the multiples of 3 or 5 below 1000.

#First simple way
start = time.time()
summa = 0
for k in range(1, 1000):
    if k % 3 == 0 or k % 5 == 0:
        summa += k
end = time.time()
print(f"Summ: {summa}")
print(f"Time: {end - start:.8f} seconds")

#Second difficult way
start1 = time.time()
summa1 = 0.5 * (333*(3+999)) + 0.5 * (199*(5+995)) - 0.5*(66*(15+990))
end1 = time.time()
print(f"Summ: {summa1}")
print(f"Time: {end1 - start1:.8f} seconds")