"""

        Bubble Sort :)

         0   1   2   3   4
Input    60, 12, 24, 18, 80 | Not Sorted
Output   12, 18, 24, 60, 80 | Sorted in Asc

       i:0
       0th Iteration          60, 12, 24, 18, 80
                        j:0,1,2,3,4
                        0.0   12, 60, 24, 18, 80  | swapped 12 and 60
                        0.1   12, 24, 60, 18, 80  | swapped 24 and 60
                        0.2   12, 24, 60, 18, 80  | swapped 18 and 60
                        0.3   12, 24, 18, 60, 80  | swapped nothing
                        0.4   12, 24, 18, 60, 80  | Last Element as the highest


       i:1
       1st Iteration         12, 24, 18, 60
                             12, 18, 24, 60
                             ......
                             .
                             ...
                             ....



"""


# prices = [1200, 1290, 1900, 1750, 8800] # Last Element is the highest (Consideration)
prices = [1200, 8800, 1290, 1900, 1750]
print("PRICES ARE:")
print(prices)

# i : 0 to 4
n = len(prices) # n is 5

for i in range(0, n): # 0, 1, 2, 3, 4
    # i:0, j:[4], 0, 1, 2, 3
    # i:1, j:[3], 0, 1, 2
    # i:2, j:[2], 0, 1, 2
    # i:3, j:[1], 0, 1, 2
    # i:4, j:[0]
    for j in range(0, n-i-1):
        if prices[j] > prices[j+1]:
            # Swap the Elements
            prices[j], prices[j+1] = prices[j+1], prices[j]

print("PRICES NOW ARE:")
print(prices)

# Exploration on the Loops for the above use case:)
