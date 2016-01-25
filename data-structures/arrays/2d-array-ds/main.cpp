#include <iostream>
#include <vector>
#include <climits>

int main () {
    std::vector< std::vector<int> > vec(6, std::vector<int>(6));
    int max = INT_MIN;

    for (int i = 0; i < 6; i++) {
        for (int j = 0 ; j < 6; j++) {
            std::cin >> vec[i][j];
        }
    }

    for (int i = 0; i <= 3; i++) {
        for (int j = 0; j <= 3; j++) {
            int sum = vec[i][j] + vec[i][j+1] + vec[i][j+2] + vec[i+1][j+1] +
                vec[i+2][j] + vec[i+2][j+1] + vec[i+2][j+2];
            if (sum > max) {
                max = sum;
            }
        }
    }
    std::cout << max << std::endl;

    return 0;
}
