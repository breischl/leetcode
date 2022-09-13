# This isn't a leetcode problem, just demonstrating an oddity in Python
# Default arg values are shared across all invocation of the method, so mutating the default arg (in this case, appending to the list)
# can be dangerous
def hello(name: str, names: list[str] = []):
    names.append(name)
    print(f"names: {names}")


hello("alice")
hello("bob")
hello("charlie")
