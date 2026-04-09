import ctypes
from typing import Any, Type, List

class DynamicArray:
    def __init__(self, dtype: Type[Any] = ctypes.c_int) -> None:
        self._length: int = 0   # Actual number of elements stored
        self._capacity: int = 1   # Current size of the allocated buffer
        self._dtype: Type[Any] = dtype   # Store the C-type
        self._ArrayType: Type[Any] = self._dtype * self._capacity  # Define the type
        self._data: ctypes.Array = self._ArrayType()   # Allocate initial buffer 

    def __len__(self) -> int:
        return self._length

    def __getitem__(self, index: int) -> Any:
        if not 0 <= index < self._length:
            raise IndexError("DynamicArray index out of range")
        return self._data[index]

    def __setitem__(self, index: int, value: Any) -> None:
        if not 0 <= index < self._length:
            raise IndexError("DynamicArray index out of range")
        self._data[index] = value

    def insert_last(self, value: Any) -> None:
        if self._length == self._capacity:
            self._resize(2 * self._capacity)
        
        self._data[self._length] = value
        self._length += 1

    def _resize(self, new_capacity: int) -> None:
        """Internal utility to resize the internal array."""
        new_array_type: Type[Any] = self._dtype * new_capacity
        new_data: ctypes.Array = new_array_type()
        
        # Copy old data to new buffer
        for i in range(self._length):
            new_data[i] = self._data[i]
            
        self._data = new_data
        self._capacity = new_capacity

    def __repr__(self) -> str:
        elements: List[Any] = [self._data[i] for i in range(self._length)]
        return f"DynamicArray({elements}, capacity={self._capacity})"
