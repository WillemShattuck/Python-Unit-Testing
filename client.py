from src.my_math_lib import simple_math_lib

def test_str_1():
    try:
        result = add("3", 4)
    except AssertionError:
        assert True
    except:
        assert False

def test_add():
    result = add(1, 2)
    expected_result = 3

    print(f"result = {result}")

def test_multiply():
    result = multiply(3,4)
    expected_result = 12



def main():
    #result = math.add(3, 4)
    #print(f"result = {result}")
    test_str_1()
    test_add()

if __name__ == "__main__":
    main()