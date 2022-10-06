## Conversion of pandas Series (column) to numpy 1-D array

- Given a list convert to numpy array
```python
np.array([1, 2, 3])
np.array(1, 2, 3)  # Gives TypeError
b1 = np.array([1,2,3])  # b.shape gives (3,) different than (3, 1)
```

- Given `x` as pd.Series

```python
x = x.to_numpy()
x = x.to_numpy()[:, np.newaxis]
```


