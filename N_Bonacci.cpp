#include<bits/stdc++.h>
#include<numeric>
#include<math.h>
using namespace std;
const int INF = 1e9;
const int N = 1e7+3;
int main()
{
    int n, m; cin>>n>>m;
    
    int arr[m], k = 0;
    for(int i=0; i<n-1; i++)
        arr[i] = 0;
    arr[n-1] = 1;
    int curr_sum = 1;
    for(int i=n; i<=m; i++){
        arr[i] = curr_sum;
        curr_sum += arr[i];
        curr_sum -= arr[k];
        k++;
    }

    for (int i = 0; i < m; i++)
    {
        cout<<arr[i]<<" ";
    }
    

    return 0;
}