'''Johan going to the church and there are n stairs to reach to Prayer hall.
Johan can move either 1 step, 2 step or 3 steps at a time.
Implement a method to count how many possible ways Johan can run up the stairs.'''

#dynamic programming approach
def possible_ways(n) :
    state = [0] * (n + 2)
    state[0] = 1
    state[1] = 1
    state[2] = 2

    for i in range(3, n + 1) :
        state[i] = state[i - 1] + state[i - 2] + state[i - 3]
    return state[n]

#calling function
#n = input()
#print(possible_ways(n))

#test cases
def test_case_1():
    n = 100 #time complexity is O(n)
    assert possible_ways(n) == 180396380815100901214157639
def test_case_2():
    n = 12
    assert possible_ways(n) == 927
def test_case_3():
    n = 1
    assert possible_ways(n) == 1