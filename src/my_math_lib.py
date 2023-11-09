def add(a, b):
    
    assert isinstance(a, int)
    assert isinstance(b, int)

    return a + b

def add_items(numbers):
    assert all(isinstance(num, int)for num in numbers)
    return sum(numbers)

def multiply(a, b):
    
    assert isinstance(a, int)
    assert isinstance(b, int)

    return a * b

def multiply_items(numbers):
   assert all(isinstance(num, int) for num in numbers)
   result = 1
   for num in numbers:
        result *= num
   return result 