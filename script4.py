#!/usr/bin/env python3
"""
Folder 4 - Python test script
Unique file for multi-file workflow testing.
"""


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero in script4.py test file")
    return a / b


if __name__ == "__main__":
    print("Folder 4 - script4.py")
    print("3 * 7 =", multiply(3, 7))
    print("10 / 2 =", divide(10, 2))


