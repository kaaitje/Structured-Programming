'''formatieve opdracht 1.3a'''


# Give aray and wich interger you want to count
def count(arr, x):
    elements_count = {}
    for element in arr:
        # adds 1 if its already in the dict
        if element in elements_count:
            elements_count[element] += 1
        # sets to 1 if its not in the dict yet
        else:
            elements_count[element] = 1
    # returns the element you want to count
    if x in elements_count.keys():
        return elements_count.get(x)
    else:
        return 'this number in not in the array'


arr = [2, 3, 3, 3, 2, 2, 2, 1, 4]
print(count(arr, 1))
print(count(arr, 7))

'''formatieve opdracht 1.3b '''


def biggest_difference(arr):
    # subtracts i+1 for i for the lenght of the array
    difference = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
    return max(difference)


arr = [1, 10, 20, 100]
print(biggest_difference(arr))


def compare(arr):
    if all(item == 0 or 1 for item in arr):
        x = 0
        y = 1
        zeros = count(arr, x)
        ones = count(arr, y)
        if ones > zeros and zeros <= 12:
            return 'Your list is correct'
        else:
            return 'Your list is not correct'
    else:
        return "Your list does not contain only zero's and ones."


# more ones than zeros and les than 12 zero's
# zeros: 2, ones: 3
arr = [1, 1, 1, 0, 0]
print(compare(arr))

# more than 12 zero's
# zeros: 13 ones: 7
arr = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(compare(arr))

# more than 12 zero's and more ones than zeros
# zeros: 13 ones: 15
arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(compare(arr))
