'''Maximize Array Value After Rearrangement
Difficulty: Easy  Accuracy: 18.93%  Submissions: 236K+Points: 2
Given an array arr of n integers. Your task is to write a program to find the maximum value of ∑arr[i]*i, where i = 0, 1, 2,., n-1. You are allowed to rearrange the elements of the array.

Note: Since the output could be large, print the answer modulo 109+7.

        result = 0
        return sum(result + arr[i]*i for i in range(len(arr)))%mod

