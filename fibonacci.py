# initialize the first two numbers of the series
a = 0
b = 1

# print the first two numbers
print(a)
print(b)

# loop to generate the next 25 numbers of the series
for i in range(23):
    # calculate the next number of the series
    c = a + b
    # print the next number
    print(c)
    # update the values of a and b for the next iteration
    a, b = b, c