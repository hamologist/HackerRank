#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int t;
    cin >> t;

    for(int a0 = 0; a0 < t; a0++){
        int n;
        int x,y;
        cin >> n;

        if (n % 3 == 0) {
            x = n / 3;
            y = 0;
        } else if (n % 3 == 1 && n >= 10) {
            x = (n - 10) / 3;
            y = 2;
        } else if (n % 3 == 2 && n > 2) {
            x = (n - 5) / 3;
            y = 1;
        } else {
            x = 0;
            y = 0;
            cout << "-1";
        }

        cout << string(x*3, '5') << string(y*5, '3') << endl;
    }
    return 0;
}
