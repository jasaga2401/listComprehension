
# List Comprehension

# storing square numbers
storeSquaresInRange = [x**2 for x in range(1, 11)]
print(storeSquaresInRange)

# storing the max value of square values from 1-10
maxSumSquares = max(x**2 for x in range(1, 11))
print(maxSumSquares)

# Output list of even numbers
evenNum = [x for x in range(2, 51) if x % 2 == 0]
print(evenNum)

# Output list of odd numbers
oddNum = [x for x in range(2, 51) if x % 2 == 1]
print(oddNum)

