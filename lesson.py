import random
import time
import operator
"""
Givein an array where every element occurs three times,
except one element which occurs only once,
find the element that occurs once.
"""

# Runtime: O(n)
# Space Complexity: O(n)


def first_pass_once(arr):

    # create dictionary
    count = {}
    # store count of all elements in dictionary
    for e in arr:
        if e not in count:
            count[e] = 0
        count[e] += 1
    # print element with smallest count
    single_element = min(count.items(), key=operator.itemgetter(1)[0])
    print(single_element)


def second_pass_once(arr):
    # Runtime: O(n log n)
    # runtime is O(nlogn) because that is the worst-case time of timsort, the built-in
    # search method
    # Space Complexity: O(1)

    # sort all elements
    arr.sort()
    # edge case -first element
    if arr[0] != arr[1]:
        print(arr[0])
        return
    # edge case -last element
    if arr[len(arr) - 1] != arr[len(arr) - 2]:
        print(arr[arr(len) - 1])
        return
    # general case - middle elements
    for i in range(1, len(arr) - 1):
        if arr[i] != arr[i-1] and arr[i] != arr[i + 1]:
            print(arr[i])
            return


# generate array of triples
test_arr = []

for i in range(0, 200):
    if i != 111333:
        test_arr.insert(random.randint(0, len(test_arr)), i)
        test_arr.insert(random.randint(0, len(test_arr)), i)
        test_arr.insert(random.randint(0, len(test_arr)), i)

test_arr.insert(random.randint(0, len(test_arr)), 111333)

start = time.time()
first_pass_once(test_arr)
end = time.time()
print(f"First Solution Total time: {end - start}")

start = time.time()
second_pass_once(test_arr)
end = time.time()
print(f"Second Solution Total time: {end - start}")
