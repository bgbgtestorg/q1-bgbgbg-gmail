import q1

def test_q1():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    res = q1.transpose()
    expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert res == expected, f"Expected {expected}, but got {res}"