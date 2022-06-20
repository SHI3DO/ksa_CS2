def square(a):
    # ADD ADDITIONAL CODE HERE!
    return [a[i] ** 2 for i in range(len(a))]


L = [3, 1, 5, 2, 4]
print(square(L))  # [9,1,25,4,16]
print(L)  # [3,1,5,2,4]
print(square([7, 6, 3, 1, 5, 8, 2, 4]))  # [49,36,9,1,25,64,4,16]
