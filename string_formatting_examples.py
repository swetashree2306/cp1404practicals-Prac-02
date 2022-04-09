"""
Use string formatting
"""
name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

print("{1} {0} for about ${2:,.0f}!".format(name, year, cost))


"""
Using a for loop with the range function and string formatting
"""
for i in range(0, 200, 50):
    print("{:5}".format(i))
