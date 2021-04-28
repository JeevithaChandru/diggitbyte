'''Johan going to the church and there are n stairs to reach to Prayer hall.
Johan can move either 1 step, 2 step or 3 steps at a time.
Implement a method to count how many possible ways Johan can run up the stairs.'''

#simple recursive function
def possible_ways(n) :
    if (n == 1 or n == 0):
        return 1
    elif (n == 2):
        return 2
    else:
        return possible_ways(n - 3) + possible_ways(n - 2) + possible_ways(n - 1)

#calling function
# n = input()
# if n >=0 and n <= 25:
#     print(possible_ways(n))
# else:
#     print("Good to go with dynamic programming approach . . . ")
#     print(possible_ways(n))

def test_case_1():
    n = 5
    assert possible_ways(n) == 13
def test_case_2():
    n = 3
    assert possible_ways(n) == 4
def test_case_3():
    n = 1
    assert possible_ways(n) == 1