# file name must start with 'test' for the tests to find it

def addition(a, b): # Make a or find a function to test
    return a + b

def test_(): # to make a test function it must be 'test_'
    a = 2
    b = 3
    result = addition(a, b)

    assert result == 5 # given what you want it to do, put the results here as an assert

# Run 