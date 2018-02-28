def first(l):
    return l[0]

# this is a appended to the file
def test_first():
    assert first([1, 2, 3]) == 1
    assert first([]) == None
