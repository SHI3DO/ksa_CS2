def allDistinct(numbers):
    # ADD ADDITIONAL CODE HERE!
    if len(set(numbers)) < len(numbers):
        return False
    else:
        return True


print(allDistinct([1, 3, 2, 5, 2, 1]))  # False
print(allDistinct([1, 0, 2, 5, 3, 4]))  # True

print("==============================================")


def allWithinRange(numbers, lower, upper):
    # ADD ADDITIONAL CODE HERE!
    for i in range(len(numbers)):
        if not lower <= numbers[i] <= upper:
            return False
    return True


print(allWithinRange([1, 0, 2, 6, 3, 4], 0, 5))  # False
print(allWithinRange([1, 0, 2, 5, 3, 4], 0, 5))  # True

print("==============================================")


def isPermutation(numbers):
    # ADD ADDITIONAL CODE HERE!
    if allDistinct(numbers) and allWithinRange(numbers, 0, len(numbers) - 1):
        return True
    return False


print(isPermutation([1, 3, 2, 5, 2, 1]))  # False
print(isPermutation([1, 0, 2, 5, 3, 4]))  # True
print(isPermutation([1, 0, 2, 6, 3, 4]))  # False
