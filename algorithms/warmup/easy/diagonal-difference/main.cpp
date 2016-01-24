#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    int primary = 0;
    int secondary = 0;

    cin >> n;
    vector< vector<int> > a(n,vector<int>(n));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> a[i][j];
        }
    }

    for (int i = 0; i < n; i++) {
        primary += a[i][i];
        secondary += a[i][n-i-1];
    }

    cout << abs(primary - secondary) << endl;

    return 0;
}
