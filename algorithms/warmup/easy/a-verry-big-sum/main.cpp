#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int n;
    long long int x;
    long long int answer = 0;

    cin >> n;

    for (int arr_i = 0;arr_i < n;arr_i++) {
        cin >> x;
        answer += x;
    }

    cout << answer << endl;
    return 0;
}

