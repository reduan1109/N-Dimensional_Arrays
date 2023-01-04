"""
An exercise in making a general array class. Note that operations are inplace.
"""

from functools import reduce
from itertools import chain

class Array:
    def __init__(self, shape: tuple, *values):
        """Initialize an array of n-dimensionality. Elements can only be of type; int, float, bool. Must be homogeneous (one data type).

        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either int, float or boolean.

        Raises:
            TypeError: If "shape" or "values" are of the wrong type.
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """        

        # Check if the shape is tuple.
        if not isinstance(shape, tuple):
            raise TypeError("Shape is not a tuple.")
        
        # Check type of shape and calculates array space.
        space = 0
        for i in shape:
            if not isinstance(i, int):
                raise TypeError("Shape not tuple of int(s).")
            else:
                space = i if space == 0 else space * i
        
        # Check if values are of valid types and flags the types present.
        typeInt = False
        typeFloat = False
        typeBool = False
        for i in values:
            if isinstance(i, int):
                typeInt = True
            elif isinstance(i, float):
                typeFloat = True
            elif isinstance(i, complex):
                typeBool = True
            else:
                raise TypeError("Value(s) are not int, float or bool.")
            
        # Checks if the values are homogeneous based on previously mentioned flags.
        if not ((typeInt ^ typeFloat) | (typeFloat ^ typeBool)):
            raise ValueError("Value(s) are not homogeneous.")
            
        # Check that the amount of values corresponds to the shape.
        if len(values) != space:
            raise ValueError(f'Number of values does not fit within the shape. {len(values)} values against {space} spaces.')
        
        # Set instance attributes.
        self.shape = shape
        self.length = len(values)
        self.array = self._arrayGen(shape, values)
    
    def __str__(self):
        """Returns a nicely printable string representation of the array.

        Returns:
            str: A string representation of the array.
        """
        self.flat_array()
        
        return str(self.shape) + " = " + str(self.array)
    
    def __getitem__(self, index):
        """Returns value on index.

        Args:
            index (int): The one dimensional index (left to right) that you want to retrieve a value from.
        
        Returns:
            value (int, float, bool): The value you're trying to retrieve from the array.
        
        Raises:
            TypeError: Index must be of type in.
            ValueError: Index out of bounds.
        """
        if not isinstance(index, int):
            raise TypeError("Index has to be an int.")
        
        output = None
        try:
            output = self.array[index]
        except IndexError:
            raise ValueError("Index is out of bounds.")
        except:
            raise Exception("Something unexpected went wrong.") 
        
        return output
        
           
    def __add__(self, other):
        """Element-wise adds Array with another Array or number.
        
        If the method does not support the operation with the supplied arguments (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.
        
        Raises:
            TypeError: Other is not Array or int.
            NotImplemented: The operation you're trying to do is not implemented.
            
        """      
        
        # Check that the method supports the given arguments (check for data type and shape of array).
        ## Array check.
        if isinstance(other, Array):
            if len(other.shape) != len(self.shape) and other.length == self.length:
                raise NotImplemented("The shape of the two arrays is not equal.")
            else:
                return Array(self.shape, *[sum(x) for x in zip(other.flat_array(), self.flat_array())])

        ## int/float check.
        elif isinstance(other, (int, float)):
            output = self.flat_array()
            
            for i in range(len(output)):
                output[i] += other
            
            return Array(self.shape, *output)
        else:
            raise TypeError("Other is not Array, float or int")
            
    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        
        return self.__add__(other)

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.

        If the method does not support the operation with the supplied arguments (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.

        Returns:
            Array: the difference as a new array.

        """
        # Check that the method supports the given arguments (check for data type and shape of array)
        if isinstance(other, Array):
            if len(other.shape) != len(self.shape) and other.length == self.length:
                raise NotImplemented("The shape and size have to be the same")
            
            return Array(self.shape, *[sum([y,-x]) for x, y in zip(other.flat_array(), self.flat_array())])

        elif isinstance(other, (int, float)):
            output = self.flat_array()
            
            for i in range(len(output)):
                output[i] -= other
            
            return Array(self.shape, *output)
        else:
            raise TypeError("Other is not Array, float or int")

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.

        If the method does not support the operation with the supplied arguments (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number being subtracted from.

        Returns:
            Array: the difference as a new array.

        """
        
        # Check that the method supports the given arguments (check for data type and shape of array)
        if isinstance(other, Array):
            if len(other.shape) != len(self.shape) and other.length == self.length:
                raise NotImplemented("The shape and size have to be the same")
            
            return Array(self.shape, *[reduce(x) for x in zip(self.flat_array(), other.flat_array())])

        elif isinstance(other, (int, float)):
            output = self.flat_array()
            
            for i in range(len(output)):
                output[i] = other - output[i]
            
            return Array(self.shape, *output)
        else:
            raise TypeError("Other is not Array, float or int")

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with 'other'.

        """
        # Check that the method supports the given arguments (check for data type and shape of array)
        if isinstance(other, Array):
            if len(other.shape) != len(self.shape) and other.length == self.length:
                raise NotImplemented("The shape and size have to be the same")
            
            return Array(self.shape, *[x*y for x, y in zip(other.flat_array(), self.flat_array())])

        elif isinstance(other, (int, float)):
            output = self.flat_array()
            
            for i in range(len(output)):
                output[i] *= other
            
            return Array(self.shape, *output)
        else:
            raise TypeError("Other is not Array, float or int")

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with 'other'.

        """
        # Hint: this solution/logic applies for all r-methods
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.

        If the two array shapes do not match, it should return False. If 'other' is an unexpected type, return False.

        Args:
            other (Array): The array to compare with this array.

        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.

        """
        return other.array == self.array if isinstance(other, Array) else False
        
    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.

        If 'other' is an array and the two array shapes do not match, this method should raise ValueError. If 'other' is not an array or a number, it should return TypeError.

        Args:
            other (Array, float, int): The array or number to compare with this array.

        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if 'other' is a number, it returns True where the array is equal to the number and False
                   where it is not.

        Raises:
            ValueError: if the shape of self and other are not equal.

        """
        
        if other.shape != self.shape:
            raise ValueError("Shape is not equal")
        
        if not isinstance(other, Array):
            raise TypeError("Other is not array")
       
        return Array(self.shape, *[x==y for x, y in zip(other.flat_array(), self.flat_array())])
        


    def min_element(self):
        """Returns the smallest value of the array.

        Only needs to work for type int and float (not boolean).

        Returns:
            float: The value of the smallest element in the array.

        """
        values = self.flat_array()
        
        if not isinstance(values[0], (int, float)):
            raise TypeError("Mean not supported for bools")
        
        tmpMin = None
        for i in values:
            if tmpMin == None:
                tmpMin = i
            elif tmpMin > i:
                tmpMin = i
        
        return tmpMin

    def mean_element(self):
        """Returns the mean value of an array

        Only needs to work for type int and float (not boolean).

        Returns:
            float: the mean value
        """
        values = self.flat_array()
        
        if not isinstance(values[0], (int, float)):
            raise TypeError("Mean not supported for bools")
        
        mult = 0
        tmpMean = None
        for i in values:
            if tmpMean == None:
                tmpMean = i
                mult+=1
            else:
                tmpMean += i
                mult += 1
        
        return tmpMean/mult

    def _arrayGen(self, shape, values) -> list:
        # Generate matrix
        for i in range(1, len(shape) + 1):
            # 'world_array' is the essentially the dimention we're working on. 
            # It has to be reset for every dimention because we're starting work on a new dimention/world
            world_array = []
            
            # 'point_array' is the point in the dimention we're in. It's where the values are stored
            point_array = int(len(values) / shape[-i])
            
            # For each point there is space in the dimention/axis/point we create an array with the right values for that space.
            # We essentially divy up the values to the array 'dimention_array' 
            for j in range(0, point_array):
                dimention_array = []
                
                # We gotta make sure that we're giving the array the right amount of values, therefore 'shape[-i]' (and because we're working backwards)
                for k in range(0, shape[-i]):    
                    dimention_array.append(values[k + j * shape[-i]])
                
                # Giving the world were working on its values
                world_array.append(dimention_array)
                    
            values = world_array
        
        return values[0]
    
    def flat_array(self):
        """Flattens the N-dimensional array of values into a 1-dimensional array.
        
        Returns:
            list: flat list of array values.
        """
        flat_array = self.array
        
        for _ in range(len(self.shape[1:])):
            flat_array = list(chain(*flat_array))
            
        return flat_array