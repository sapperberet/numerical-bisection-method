#include <iostream>
#include <functional>
#include <cmath>
#include <string>
#include <stdexcept>


double bisection_method(std::function<double(double)> f, double a, double b, double tol = 1e-6, int max_iter = 100) {
    if (f(a) * f(b) > 0) {
        throw std::invalid_argument("The function must change signs over the interval [a, b].");
    }

    double c;
    for (int i = 0; i < max_iter; ++i) {
        c = (a + b) / 2.0;
        double fc = f(c);

        if (std::abs(fc) < tol || (b - a) / 2.0 < tol) {
            return c;
        }

        if (f(a) * fc < 0) {
            b = c;
        } else {
            a = c;
        }
    }

    throw std::runtime_error("Bisection method did not converge within the specified iterations.");
}


std::function<double(double)> parse_function(const std::string &expr) {
    if (expr == "x^2 - 2") {
        return [](double x) { return x * x - 2; };
    } else if (expr == "sin(x)") {
        return [](double x) { return std::sin(x); };
    } else {
        throw std::invalid_argument("Unsupported expression.");
    }
}

int main() {
    std::string expression;
    std::cout << "Enter the function expression in terms of x (e.g., x^2 - 2): ";
    std::getline(std::cin, expression);


    try {
        auto f = parse_function(expression);

        double a, b;
        std::cout << "Enter the start of the interval (a): ";
        std::cin >> a;
        std::cout << "Enter the end of the interval (b): ";
        std::cin >> b;


        double root = bisection_method(f, a, b);
        std::cout << "Root found by Bisection method: " << root << std::endl;

    } catch (const std::exception &e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
