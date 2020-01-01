def recursion_staircase(steps, reduce):

    results_temp = staircase(steps - reduce)
    if len(results_temp) == 0:
        return [reduce]
    return [[reduce] + [result] for result in results_temp]


def staircase(steps):
    if steps == 0:
        return []

    results = list()

    if steps >= 1:
        results += recursion_staircase(steps, 1)
    if steps >= 2:
        results += recursion_staircase(steps, 2)
    if steps >= 3:
        results += recursion_staircase(steps, 3)

    return results

def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = len(staircase(n))
    if output == solution:
        print("Pass")
    else:
        print("Fail")



if __name__ == '__main__':
    n = 3
    solution = 4
    test_case = [n, solution]
    test_function(test_case)

    n = 4
    solution = 7
    test_case = [n, solution]
    test_function(test_case)

    n = 7
    solution = 44
    test_case = [n, solution]
    test_function(test_case)
