#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <regex>

int main() {
    std::string time;
    std::smatch matches;
    std::regex reg ("([0-9]{2}):([0-9]{2}):([0-9]{2})(AM|PM)");
    int hours;
    std::string hours_str;

    std::cin >> time;
    std::regex_search(time, matches, reg);

    if (matches[1] == "12" && matches[4] == "AM") {
        hours = 0;
    } else if (matches[1] == "12" && matches[4] == "PM") {
        hours = 12;
    } else {
        if (matches[4] == "PM") {
            hours = stoi(matches[1]) + 12;
        } else {
            hours = stoi(matches[1]);
        }
    }

    hours_str = std::to_string(hours);
    if (hours < 10) {
        hours_str.insert(0, 1, '0');
    }

    std::cout << hours_str << ":" << matches[2] << ":" << matches[3] << std::endl;

    return 0;
}
