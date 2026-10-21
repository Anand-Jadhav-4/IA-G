#include<bits/stdc++.h> // Include necessary libraries
#include<numeric>
#include<math.h>
using namespace std;
const int INF = 1e9; // Initialize a constant for infinity
const int N = 1e7+3;
int main()
{
    // 4. Loop from n to m to generate the Fibonacci series.
    //    a. Set the next element in the Fibonacci series to curr_sum.
    //    b. Update curr_sum by adding the newly calculated element.
    //    c. Subtract the element that is n steps back to maintain the sliding window of size n.
    //    d. Increment the variable k to keep track of the current position in the array.
    // 5. Print the generated Fibonacci series.
