# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 01:06:55 2025

@author: mkhog
"""

# Write code below 💖
import time
initial = time.time()

# Total Time: 0.1395 sec
#numbers = [num+2 for num in range(1000000)]
#even_numbers = [num for num in numbers if not num%2]

# Total Time: 0.3091 sec
numbers = []
for num in range(1000000):
    numbers.append(num+1
                   )
even_numbers = []
for num in numbers:
    if not num%2:
        even_numbers.append(num)
        
#print(f"Original Numbers: {numbers}")
#print(f"Even Numbers: {even_numbers}")
final = time.time()
total = final-initial
print(f"Total Time: {round(total,6)}")


'''
Using list comprehension makes code more effecient and fast

'''