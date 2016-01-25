#include <iostream>
#include <set>
#include <string>
#include <algorithm>

int main () {
    std::string line;
    std::getline(std::cin, line);
    std::transform(line.begin(), line.end(), line.begin(), ::tolower);
    std::set<char> check(line.begin(), line.end());
    check.erase(' ');

    if (check.size() == 26) {
        std::cout << "pangram" << std::endl;
    } else {
        std::cout << "not pangram" << std::endl;
    }

    return 0;
}
