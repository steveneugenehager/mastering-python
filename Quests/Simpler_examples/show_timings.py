# show_timings.py
"""Example of timings review using 5 approaches to the same problem.""" 
import time

limit = 100_000_000

def method1_builtin():
    """Using sum(range())"""
    return sum(range(1, limit + 1))


def method2_formula():
    """Using mathematical formula"""
    n = limit
    return n * (n + 1) // 2


def method3_loop():
    """Using for loop"""
    total = 0
    for i in range(1, limit + 1):
        total += i
    return total


def method4_list_comp():
    """Using list comprehension"""
    return sum([i for i in range(1, limit + 1)])


def method5_generator():
    """Using generator expression"""
    return sum(i for i in range(1, limit + 1))


def compare_methods():
    """Compare performance of different methods."""
    methods = [
        ("Formula", method2_formula),
        ("sum(range())", method1_builtin),
        ("Generator", method5_generator),
        ("For loop", method3_loop),
        ("List comprehension", method4_list_comp),

    ]
    
    print("Performance Comparison:")
    print("-" * 50)
    
    for name, method in methods:
        start = time.time()
        result = method()
        elapsed = time.time() - start
        print(f"{name:20} {elapsed:.4f}s - Result: {result:,}")


compare_methods()
