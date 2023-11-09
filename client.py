import src.my_math_lib as math



def test_str_1():
    try:
        result = math.add("3", 4)
    except AssertionError:
        assert True
    except:
        assert False

def test_add():
    result = math.add(1, 2)
    expected_result = 3

    print(f"result = {result}")

def test_multiply():
    result = math.multiply(3,4)
    expected_result = 12



def main():
    #result = math.add(3, 4)
    #print(f"result = {result}")
    test_str_1()
    test_add()

if __name__ == "__main__":
    main()
