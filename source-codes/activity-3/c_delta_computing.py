# Computing Implementation (C/Δ) - Fibonacci using algorithm

def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_val = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_val)
    return sequence

# Example usage
terms = 10
print(f"Fibonacci Sequence (First {terms} terms):")
print(fibonacci(terms))
