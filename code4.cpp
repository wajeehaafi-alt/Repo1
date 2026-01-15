#include <iostream>
#include <vector>

// Folder 4 - C++ test file (code4.cpp)
int sumVector(const std::vector<int>& values) {
    int total = 0;
    for (int v : values) {
        total += v;
    }
    return total;
}

int main() {
    std::vector<int> nums{1, 2, 3, 4, 5};
    std::cout << "Folder 4 - code4.cpp test" << std::endl;
    std::cout << "Sum = " << sumVector(nums) << std::endl;
    return 0;
}


