def countZero(numbers):
    # ADD ADDITIONAL CODE HERE!
    return len([i for i in range(len(numbers)) if numbers[i] == 0])


print(countZero([0, 4, 0, -2, 4, 0]))  # 3
print(countZero([1, 0, -2, 4, 0, 0, -7, 0, 5]))  # 4
