from smartexplain import explain_code

code = '''
import math

class Greeter:
    """Greeter class to greet people."""

    def __init__(self, name):
        """Initialize with a name."""
        self.name = name

    def greet(self):
        """Print a greeting."""
        print(f"Hello, {self.name}!")

def factorial(n):
    """Calculate factorial recursively."""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

try:
    print(factorial(5))
except Exception as e:
    print("Error:", e)

squares = [x*x for x in range(5)]
'''

print(explain_code(code))
