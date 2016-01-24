#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    int value;
    int pos = 0;
    int neg = 0;
    int zero = 0;

    cin >> n;

    for (int arr_i = 0;arr_i < n;arr_i++) {
        cin >> value;
        if (value > 0) {
            pos++;
        } else if (value < 0) {
            neg++;
        } else {
            zero++;
        }
    }

    cout << pos/(float)n << endl;
    cout << neg/(float)n << endl;
    cout << zero/(float)n << endl;

    return 0;
}
