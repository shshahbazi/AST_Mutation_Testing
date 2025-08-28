def CalculatePower(N, X):
    P = 1
    for i in range(1, X + 1):
        P = P * N
    return P


#test
def test_example_function():
    assert CalculatePower(2, 3) == 8
