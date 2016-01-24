#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main () {
    int t;
    cin >> t;

    for (int a0 = 0; a0 < t; a0++) {
        int n;
        int k;
        int x;
        string x_str;
        int count = 0;
        cin >> n >> k;

        for (int a_i = 0; a_i < n; a_i++) {
            cin >> x_str;
            x = stoi(x_str);
            if (x <= 0) {
                count++;
            }
        }

        if (count < k) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }

    return 0;
}
