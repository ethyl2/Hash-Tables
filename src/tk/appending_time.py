import time


def add_to_back(n):
    '''
    n is the number of times to add to the list
    '''
    x = []
    for i in range(0, n):
        x.append(i+1)
    return x


def add_to_front(n):
    '''
    n is the number of times to add to the list
    '''
    x = []
    for i in range(0, n):
        x.insert(0, n-i)
    return x


def get_run_time(function_to_run, n):
    start_time = time.time()
    function_to_run(n)
    end_time = time.time()
    return end_time - start_time


def compare_run_time(function_to_run_1, function_to_run2, n):
    runtime1 = get_run_time(function_to_run_1, n)
    runtime2 = get_run_time(function_to_run2, n)
    print('runtime1: ' + str(runtime1))
    print('runtime2: ' + str(runtime2))
    return runtime2 / runtime1
    # return runtime1 / runtime2 * 100

# print(add_to_back(10))
# print(add_to_front(10))


# Compare the times to run these functions
# print(get_run_time(add_to_back, 100000))
print(compare_run_time(add_to_back, add_to_front, 100000))
