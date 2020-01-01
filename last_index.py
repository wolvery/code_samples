
def last_index(arr, target, last_target_index=None, current_index=0):

    if len(arr) == current_index:
        return -1 if last_target_index is None else last_target_index

    if arr[current_index] == target:
        last_target_index = current_index

    return last_index(arr, target, last_target_index, current_index+1)


def test_function(test_case):
    arr = test_case[0]
    target = test_case[1]
    solution = test_case[2]
    output = last_index(arr, target)
    if output == solution:
        print("Pass")
    else:
        print("False")



if __name__ == '__main__':
    arr = [1, 2, 5, 5, 4]
    target = 5
    solution = 3

    test_case = [arr, target, solution]
    test_function(test_case)

    arr = [1, 2, 5, 5, 4]
    target = 7
    solution = -1

    test_case = [arr, target, solution]
    test_function(test_case)

    arr = [91, 19, 3, 8, 9]
    target = 91
    solution = 0

    test_case = [arr, target, solution]
    test_function(test_case)

    arr = [1, 1, 1, 1, 1, 1]
    target = 1
    solution = 5

    test_case = [arr, target, solution]
    test_function(test_case)
