#include <iostream>
#include <string>
#include <cmath>

int main () {
    int t;
    std::cin >> t;

    for (int i = 0; i < t; i++) {
        int start, end;
        int answer = 0;
        std::cin >> start >> end;

        answer = (int)(floor(sqrt(end)) - ceil(sqrt(start)) + 1);

        std::cout << answer << std::endl;
    }

    return 0;
}
