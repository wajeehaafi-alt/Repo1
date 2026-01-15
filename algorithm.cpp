#include <iostream>
#include <cmath>

// Test C++ Algorithm for Folder 3
class MathOperations {
public:
    static double calculateSquare(double number) {
        return number * number;
    }
    
    static double calculateSquareRoot(double number) {
        return sqrt(number);
    }
    
    static int factorial(int n) {
        if (n <= 1) return 1;
        return n * factorial(n - 1);
    }
};

int main() {
    std::cout << "Algorithm Test - Folder 3" << std::endl;
    std::cout << "Square of 5: " << MathOperations::calculateSquare(5) << std::endl;
    std::cout << "Factorial of 5: " << MathOperations::factorial(5) << std::endl;
    return 0;
}

