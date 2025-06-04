from smartexplain.explainer import explain_code

sample_code = """
def greet(name):
    print("Hello", name)
"""

print(explain_code(sample_code))
