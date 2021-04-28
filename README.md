# Diggitbyte - coding assignment
Problem statement - '''Johan going to the church and there are n stairs to reach to Prayer hall.
Johan can move either 1 step, 2 step or 3 steps at a time.
Implement a method to count how many possible ways Johan can run up the stairs.'''

The programming language used - Python, version - 3.7

The given problem can be solved in 2 possible ways-
1. Recursive method
2. Dynamic programming

But, the challenge here is to choose the best approach based on the time and space complexities. Let's go through both the algorithms and decide which one to be considered as the best algorithm.

**1. Recursion algorithm**

-> A recursive function needs to be created with accepts only one parameter which specifies the total number of stairs to reach the prayer hall(n).

-> The possible base cases need to be checked, like if there are no stairs(n=0) and in case of only 1 or 2 stairs(n=1, n=2), then the function should return 1,1 and 2 respectively.

-> Now, if the value is greater than 2, then the function is recursive called with the values (n-1),(n-2), and (n-3) as the person can skip 2 or 3 steps, or can skip no step.

-> The values are summed up and returned.

**Time complexity** - O(3^n) - the recursive function in each state is called thrice and hence, exponential.

**Space complexity** - O(1) - no space is required to store any states.

**2. Dynamic programming** - Instead of calling the function every time we store the states in an array here.
   
   -> An array of size n+1 should be created where the first 3 variables are initialized with 1,1,2.
   
   -> Loop is run from 3 to n.

   -> The states are stored for each index as st[i] = st[i-1] + st[i-2] + st[i-3]

   -> Finally, return the summed up value.

**Time complexity** - O(n) - only one array traversal.

**Space complexity** - O(n) - to store states in an array, additional space is required.

**Running the scripts -** 

1. test_solution1.py(recursive method)

   cmd to run test-cases - pytest test_solution1.py


2. test_solution2.py(dynamic programming)
   
   cmd to run test-cases - pytest test_solution2.py