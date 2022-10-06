## Stack numpy arrays side by side

- Requires first dimension to be identical

```python
x_column_stacked = np.column_stack((x0, x1, x2, x3))
x_column_stacked = np.c_[a, b]
```

## Reshape

- The dimensions are to multiple of the size of the array to be resized
```python
a = np.arange(0, 10)
b = a.reshape(5, 2)
```

- Get the indices i, j into separated matrices
```python
x = np.indices((2, 2))  # returns two matrices (2, 2) in an array of arrays, one containing the i index, the other the j index
```

- Get
