# Q1
sum = 0
for value in L:
    sum = sum + value

# Q2
sum = 0
for i in range(len(L)):
    sum = sum + L[i]

# Q3
sum = 0
i = 0
while i < len(L):
    sum = sum + L[i]
    i = i + 1

# Q4 
sum = 0
i = 0
while i < len(L):
    sum = sum + L[i]
    i = i + 2

# Q5
# Precondition: len(L) % 4 == 0
sum = 0
i = 0
while i < len(L):
    sum = sum + L[i]
    i = i + len(L) // 4

#Assume k = len(L)
# beginning of 1st iteration: i is equal to 0
# beginning of 2nd iteration: i is equal to  k // 4
# beginning of 3rd iteration: i is equal to   k // 4  + k // 4 = k /2
# beginning of 4th iteration: i is equal to  3 * k / 4
# i is equal to k, so k < k evaluates to False. Will not execute 5th iteration.

# Q8
sum = 0
for val1 in L:
    for val2 in L:
        sum = val1 - val2

# Q9
sum = 0
for i in range(k * k):
    sum = sum + i
    
# Q10
sum = 0
for i in range(10):
    for j in range(len(L)):
        sum = sum + i + j
