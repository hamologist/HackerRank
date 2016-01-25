#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int t;
    cin >> t;

    for(int a0 = 0; a0 < t; a0++){
        int n;
        int x;
        int count = 0;
        cin >> n;
        string n_str = to_string(n);

        for (auto x_char : n_str) {
            x = x_char - '0';
            if (x != 0 && n % x == 0) {
                count++;
            }
        }
        cout << count << endl;
    }

    return 0;
}

