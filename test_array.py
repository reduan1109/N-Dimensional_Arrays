"""
Tests for our array class
"""
from array_class import Array

def test_str_1d():
    arrayA = Array((5,), 0, 1, 2, 3, 4)
    stringA = "(5,) = [0, 1, 2, 3, 4]"
    assert str(arrayA) == stringA

#Tests of __radd__ is not needded as it is commutative
def test_add_1d():
    # Integers
    arrayA = Array((5,), 0, 1, 2, 3, 4)
    arrayB = Array((5,), 1, 2, 3, 4, 5)
    arrayC = Array((5,), 1, 3, 5, 7, 9)
    assert arrayA + arrayB == arrayC
        
    arrayA = Array((5,), 0, 1, 2, 3, 4)
    numB = 4
    arrayC = Array((5,), 4, 5, 6, 7, 8)
    assert arrayA + numB == arrayC
    
    # Floats
    arrayA = Array((5,), 0.5, 1.5, 2.5, 3.5, 4.5)
    arrayB = Array((5,), 1.5, 2.5, 3.5, 4.5, 5.5)
    arrayC = Array((5,), 2.0, 4.0, 6.0, 8.0, 10.0)
    assert (arrayA + arrayB) == arrayC
        
    arrayA = Array((5,), 0.5, 1.5, 2.5, 3.5, 4.5)
    numB = 4.5
    arrayC = Array((5,), 5, 6, 7, 8, 9)
    assert arrayA + numB == arrayC
    
    # Bools
    # Not supported for bools

def test_sub_1d():
    # Integers
    arrayA = Array((5,), 0, 1, 2, 3, 4)
    arrayB = Array((5,), 1, 2, 3, 4, 5)
    arrayC = Array((5,), -1, -1, -1, -1, -1)
    assert arrayA - arrayB == arrayC
    
    arrayA = Array((5,), 0, 1, 2, 3, 4)
    arrayB = Array((5,), 1, 2, 3, 4, 5)
    arrayC = Array((5,), 1, 1, 1, 1, 1)
    assert arrayB - arrayA == arrayC
    
    # Ints reveresd
    arrayA = Array((5,), 0, 1, 2, 3, 4)
    numB = 1
    arrayC = Array((5,), -1, 0, 1, 2, 3)
    assert arrayA - numB == arrayC
    
    arrayA = Array((5,), 0, 1, 2, 3, 4)
    numB = 1
    arrayC = Array((5,), 1, 0, -1, -2, -3)
    assert numB - arrayA == arrayC
    
    # Floats
    arrayA = Array((5,), 0.5, 1.5, 2.5, 3.5, 4.5)
    arrayB = Array((5,), 1.5, 2.5, 3.5, 4.5, 5.5)
    arrayC = Array((5,), -1.0, -1.0, -1.0, -1.0, -1.0)
    assert arrayA - arrayB == arrayC
    
    arrayA = Array((5,), 0.5, 1.5, 2.5, 3.5, 4.5)
    arrayB = Array((5,), 1.5, 2.5, 3.5, 4.5, 5.5)
    arrayC = Array((5,), 1.0, 1.0, 1.0, 1.0, 1.0)
    assert arrayB - arrayA == arrayC
    
    # Floats reversed
    arrayA = Array((5,), 0.5, 1.5, 2.5, 3.5, 4.5)
    numB = 1.5
    arrayC = Array((5,), -1.0, 0.0, 1.0, 2.0, 3.0)
    assert arrayA - numB == arrayC
    
    arrayA = Array((5,), 0.5, 1.5, 2.5, 3.5, 4.5)
    numB = 1.5
    arrayC = Array((5,), 1.0, 0.0, -1.0, -2.0, -3.0)
    assert numB - arrayA == arrayC
    
    # Bools
    # Not supported for bools

#Tests of __rmul__ is not needded as it is commutative
def test_mul_1d():
    # Integers
    arrayA = Array((5,), 0, 1, 2, 3, 4)
    arrayB = Array((5,), 1, 2, 3, 4, 5)
    arrayC = Array((5,), 0, 2, 6, 12, 20)
    assert arrayA * arrayB == arrayC
        
    arrayA = Array((5,), 0, 1, 2, 3, 4)
    numB = 4
    arrayC = Array((5,), 0, 4, 8, 12, 16)
    assert arrayA * numB == arrayC

    # Floats
    arrayA = Array((5,), 0.5, 1.5, 2.5, 3.5, 4.5)
    arrayB = Array((5,), 1.0, 2.0, 3.0, 4.0, 5.0)
    arrayC = Array((5,), 0.5*1.0, 1.5*2.0, 2.5*3.0, 3.5*4.0, 4.5*5.0)
    assert arrayA * arrayB == arrayC
        
    arrayA = Array((5,), 0.5, 1.5, 2.5, 3.5, 4.5)
    numB = 4.0
    arrayC = Array((5,), 0.5*4.0, 1.5*4.0, 2.5*4.0, 3.5*4.0, 4.5*4.0)
    assert arrayA * numB == arrayC
    
    # Bools
    # Not supported for bools

def test_eq_1d():
    # Ints true
    arrayA = Array((5,), 1, 2, 3, 4, 5)
    arrayB = Array((5,), 1, 2, 3, 4, 5)
    assert arrayA == arrayB
    
    # Ints not true
    arrayA = Array((5,), 1, 2, 3, 4, 6)
    arrayB = Array((5,), 1, 2, 3, 4, 5)
    assert arrayA != arrayB
    
    # Floats true
    arrayA = Array((5,), 1.0, 2.0, 3.0, 4.0, 5.0)
    arrayB = Array((5,), 1.0, 2.0, 3.0, 4.0, 5.0)
    assert arrayA == arrayB
    
    # Floats not true
    arrayA = Array((5,), 1.0, 2.0, 3.0, 4.0, 6.0)
    arrayB = Array((5,), 1.0, 2.0, 3.0, 4.0, 5.0)
    assert arrayA != arrayB
    
    # Bools true
    arrayA = Array((5,), True, False, True, False, True)
    arrayB = Array((5,), True, False, True, False, True)
    assert arrayA == arrayB
    
    # Bools not true
    arrayA = Array((5,), True, False, True, False, True)
    arrayB = Array((5,), True, False, True, False, False)
    assert arrayA != arrayB


def test_same_1d():
    # Integers
    arrayA = Array((5,), 1, 2, 3, 4, 6)
    arrayB = Array((5,), 1, 2, 3, 4, 5)
    arrayC = Array((5,), True, True, True, True, False)
    assert arrayA.is_equal(arrayB) == arrayC
    
    # Floats
    arrayA = Array((5,), 1.0, 2.0, 3.0, 4.0, 6.0)
    arrayB = Array((5,), 1.0, 2.0, 3.0, 4.0, 5.0)
    arrayC = Array((5,), True, True, True, True, False)
    assert arrayA.is_equal(arrayB) == arrayC
    
    # Bools
    arrayA = Array((5,), False, True, False, True, True)
    arrayB = Array((5,), False, True, False, True, False)
    arrayC = Array((5,), True, True, True, True, False)
    
def test_smallest_1d():
    # Integers
    arrayA = Array((5,), 1, 2, 3, 4, 6)
    numB = 1
    assert arrayA.min_element() == numB
    
    # Floats
    arrayA = Array((5,), 1.0, 2.0, 3.0, 4.0, 6.0)
    numB = 1.0
    assert arrayA.min_element() == numB
    
    # Opperation not supported for bools

def test_mean_1d():
    # Integers
    arrayA = Array((4,), 1, 2, 3, 4)
    numB = 2.5
    assert arrayA.mean_element() == numB
    
    #Floats
    arrayA = Array((4,), 1.1, 2.1, 3.1, 4.1)
    numB = sum([1.1, 2.1, 3.1, 4.1])/4.0
    assert arrayA.mean_element() == numB
    
    # Opperation not supported for bools



# 2D tests (Task 6)
def test_add_2d():
    # Integers
    arrayA = Array((2,2), 0, 1, 2, 3)
    arrayB = Array((2,2), 1, 2, 3, 4)
    arrayC = Array((2,2), 1, 3, 5, 7)
    assert arrayA + arrayB == arrayC
        
    arrayA = Array((2,2), 0, 1, 2, 3)
    numB = 4
    arrayC = Array((2,2), 4, 5, 6, 7)
    assert arrayA + numB == arrayC
    
    # Floats
    arrayA = Array((2,2), 0.5, 1.5, 2.5, 3.5)
    arrayB = Array((2,2), 1.5, 2.5, 3.5, 4.5)
    arrayC = Array((2,2), 2.0, 4.0, 6.0, 8.0)
    assert (arrayA + arrayB) == arrayC
        
    arrayA = Array((2,2), 0.5, 1.5, 2.5, 3.5)
    numB = 4.5
    arrayC = Array((2,2), 5, 6, 7, 8)
    assert arrayA + numB == arrayC
    
    # Bools
    # Not supported for bools


def test_mult_2d():
    # Integers
    arrayA = Array((2,2), 0, 1, 2, 3)
    arrayB = Array((2,2), 1, 2, 3, 4)
    arrayC = Array((2,2), 0, 2, 6, 12)
    assert arrayA * arrayB == arrayC
        
    arrayA = Array((2,2), 0, 1, 2, 3)
    numB = 4
    arrayC = Array((2,2), 0, 4, 8, 12)
    assert arrayA * numB == arrayC
    
    # Floats
    arrayA = Array((2,2), 0.5, 1.5, 2.5, 3.5)
    arrayB = Array((2,2), 1.5, 2.5, 3.5, 4.5)
    arrayC = Array((2,2), 1.5*0.5, 2.5*1.5, 3.5*2.5, 4.5*3.5)
    assert (arrayA * arrayB) == arrayC
        
    arrayA = Array((2,2), 0.5, 1.5, 2.5, 3.5)
    numB = 4.5
    arrayC = Array((2,2), 0.5*4.5, 1.5*4.5, 2.5*4.5, 3.5*4.5)
    assert arrayA * numB == arrayC
    
    # Bools
    # Not supported for bools


def test_same_2d():
    # Integers
    arrayA = Array((2,2), 1, 2, 3, 5)
    arrayB = Array((2,2), 1, 2, 3, 4)
    arrayC = Array((2,2), True, True, True, False)
    assert arrayA.is_equal(arrayB) == arrayC
    
    # Floats
    arrayA = Array((2,2), 1.0, 2.0, 3.0, 4.1)
    arrayB = Array((2,2), 1.0, 2.0, 3.0, 4.0)
    arrayC = Array((2,2), True, True, True, False)
    assert arrayA.is_equal(arrayB) == arrayC
    
    # Bools
    arrayA = Array((2,2), False, True, False, False)
    arrayB = Array((2,2), False, True, False, True)
    arrayC = Array((2,2), True, True, True, False)


def test_mean_2d():
    #Ints
    arrayA = Array((2,2), 1, 2, 3, 4)
    numB = 2.5
    assert arrayA.mean_element() == numB
    
    #Floats
    arrayA = Array((2,2), 1.1, 2.1, 3.1, 4.1)
    numB = sum([1.1, 2.1, 3.1, 4.1])/4.0
    assert arrayA.mean_element() == numB


if __name__ == "__main__":
    """
    Note: Write "pytest" in terminal in the same folder as this file is in to run all tests
    (or run them manually by running this file).
    Make sure to have pytest installed (pip install pytest, or install anaconda).
    """

    # Task 4: 1d tests
    test_str_1d()
    test_add_1d()
    test_sub_1d()
    test_mul_1d()
    test_eq_1d()
    test_mean_1d()
    test_same_1d()
    test_smallest_1d()

    # Task 6: 2d tests
    test_add_2d()
    test_mult_2d()
    test_same_2d()
    test_mean_2d()