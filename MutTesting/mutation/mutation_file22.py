

def CalculatePower(N, X):
    P = 1
    for i in range(1, (X + 1)):
        P = (P ^ N)
    return P

def test_example_function():
    assert (CalculatePower(2, 3) == 8)
# Test
def test_example_function():
    assert CalculatePower(2, 3) == 8
