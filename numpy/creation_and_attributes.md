## Properties

### Most important attributes

```python
a = np.array([1, 2, 3])
a.ndim  # number of axis in the array
a.shape  # (m, n)  output for 2D array
a.size  # total number of elements
a.dtype  # type of elemets in the array
a.itemsize  # size in bytes of each element
```

## Creating arrays

```python
np.eye(3)  # for Identity matrix
np.eye(3,5)  # where the diagonal is along the 3 diagonal dimension
np.random.randint(0, high=10, size=5)  # creates a random array of 5 elements from 0 to 9 
np.random.random(20)  # create a random array of size 20 whose elements belong to [0, 1]
```

### Creating array fill with value

```python
np.full(3,2, 10)
```

### Using a range

```python
np.arange(10)
```

### Using linspace given how many numbers you want

```python
np.linspace(1., 4., 6)
```

#### Using logspace

```python
np.logspace(0,1,10)
```

#### Diag method
