#include<bits/stdc++.h>
#include<numeric>
#include<math.h>
using namespace std;
const int INF = 1e9;
const int N = 1e7+3;

int normalMaxSum(int arr[], int n){
    int res = arr[0], maxEnding = arr[0];
    for(int i=0; i<n; i++){
        maxEnding = max(arr[i], maxEnding + arr[i]);
        res = max(res, maxEnding);
    }
    return res;
}

int overallMaxSum(int arr[], int n){
    int max_normal = normalMaxSum(arr, n);
    if(max_normal < 0)
        return 0;
    
    int arr_sum = 0;
    for(int i=0; i<n; i++){
        arr_sum += arr[i];
        arr[i] = -arr[i];
    }
    int max_cicular = arr_sum + normalMaxSum(arr, n);

    return max(max_normal, max_cicular);
}

int main()
{
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    cout << overallMaxSum(arr, n) << endl;
    return 0;
}