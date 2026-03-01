#include <iostream>

#include "math_utils.h"

int main() {
    if (add(2, 3) != 5) {
        std::cerr << "Expected 2 + 3 == 5\n";
        return 1;
    }

    if (add(-1, 1) != 0) {
        std::cerr << "Expected -1 + 1 == 0\n";
        return 1;
    }

    std::cout << "All tests passed.\n";
    return 0;
}
