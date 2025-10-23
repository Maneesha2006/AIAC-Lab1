#include <iostream>
using namespace std;

// Function to find factorial using recursion
int factorial(int n) {
    if (n < 0) {
        cout << "Factorial is not defined for negative numbers." << endl;
        return -1; // Return -1 for invalid input
    } else if (n == 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

int main() {
    cout << "Factorial of 5: " << factorial(5) << endl;
    cout << "Factorial of 0: " << factorial(0) << endl;
    return 0;
}
