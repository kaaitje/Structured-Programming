def average(my_list):
    gemiddelde = sum(my_list) / len(my_list)
    return gemiddelde


mylist = [1, 1, 1, 1, 1]
print(average(mylist))


def average_lists(my_lists):
    newlist = []
    for i in range(len(my_lists)):
        gemiddelde = average(my_lists[i])
        newlist.append(gemiddelde)
    return newlist


mylists = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
print(average_lists(mylists))
