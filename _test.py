# test_example.py

def test_addition():
    result = 1 + 1
    assert result == 2

def test_subtraction():
    result = 5 - 3
    assert result == 2

def test_multiplication():
    result = 3 * 4
    assert result == 12

def test_division():
    result = 10 / 2
    assert result == 5

def test_string_concatenation():
    result = "Hello, " + "World!"
    assert result == "Hello, World!"

def test_list_contains_item():
    my_list = [1, 2, 3, 4, 5]
    assert 3 in my_list

def test_dictionary_key_exists():
    my_dict = {'key1': 'value1', 'key2': 'value2'}
    assert 'key1' in my_dict

def test_boolean_logic():
    a = True
    b = False
    assert a and (not b)

# Add more test functions as needed
