# NumPy Gotchas and Common Pitfalls

This document covers common mistakes and unintuitive behaviors in NumPy.

## 1. Views vs Copies

### The Issue
Slicing an array returns a **view**, not a copy. Modifying the slice modifies the original.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
slice_arr = arr[1:4]  # This is a VIEW, not a copy

print("Original arr:", arr)        # [1 2 3 4 5]
print("Slice:", slice_arr)          # [2 3 4]

slice_arr[0] = 99
print("After modifying slice:")
print("Original arr:", arr)        # [ 1 99  3  4  5] - ORIGINAL CHANGED!
print("Slice:", slice_arr)          # [99  3  4]
```

### When You Get a Copy
- Using `np.copy(arr)` or `arr.copy()`
- Fancy indexing: `arr[[1, 2, 3]]`
- Boolean indexing: `arr[arr > 0]`

```python
# This creates a COPY
copy_arr = arr[1:4].copy()  # Explicit copy
copy_arr[0] = 99
print("Original arr:", arr)  # [1 2 3 4 5] - Unchanged
```

### How to Detect
```python
# Check if arrays share memory
np.shares_memory(arr, slice_arr)  # True if they share memory
np.may_share_memory(arr, slice_arr)  # May share memory
```

---

## 2. Broadcasting Gotchas

### The Issue
Broadcasting follows specific rules that can lead to unexpected results.

```python
# Example 1: Dimensions must match from the right
arr = np.ones((3, 4))
row = np.ones(4)
result = arr + row  # Works: (3, 4) + (4,) -> (3, 4)

# Example 2: Mismatched dimensions
try:
    col = np.ones(3)
    result = arr + col.reshape(3, 1)  # Must reshape!
except ValueError as e:
    print("Error:", e)  # ValueError: operands could not be broadcast together
```

### Common Mistakes
```python
# Wrong: Creates (5,) + (3,) = Error
a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 2, 3])
# result = a + b  # ValueError!

# Right: Reshape to make dimensions compatible
b_reshaped = b.reshape(3, 1)  # or b.reshape(-1, 1)
result = a + b_reshaped  # Or reshape both to match

# Wrong: Shape (3,) + (2,) = Error
arr1 = np.array([[1, 2], [3, 4], [5, 6]])  # (3, 2)
arr2 = np.array([1, 2, 3])  # (3,)
# result = arr1 + arr2  # ValueError!

# Right: Reshape arr2 to (3, 1)
result = arr1 + arr2.reshape(3, 1)
```

### Broadcasting Rule
1. Compare shapes from right to left
2. If dimensions differ, expand the dimension with size 1
3. If neither is 1 and sizes differ -> Error

---

## 3. In-Place Operations

### The Issue
Some operations return new arrays, others modify in-place.

```python
arr = np.array([1, 2, 3, 4, 5])

# These modify IN PLACE
arr += 1
arr *= 2
np.add(arr, 1, out=arr)

# These return NEW arrays
new_arr = arr + 1
new_arr = np.add(arr, 1)  # Without out= parameter
```

---

## 4. Data Type Overflow

### The Issue
NumPy arrays have fixed size. Operations can overflow.

```python
# Integer overflow
arr = np.array([1, 2, 3], dtype=np.int8)
result = arr * 100
print("Result:", result)  # [100 200 44] - overflow!
# int8 max is 127, so 200 wraps around: 200 - 256 = -56, but with unsigned...
# Actually for int8: 200 = 200 - 256 = -56, then *3 gives -56*3 = -168, etc.

# Solution: Use larger dtype
arr = np.array([1, 2, 3], dtype=np.int64)
result = arr * 100
print("Result:", result)  # [100 200 300] - correct!
```

---

## 5. Floating Point Precision

### The Issue
Floating point operations have precision limits.

```python
# Equality comparison with floats
a = 0.1 + 0.2
b = 0.3
print(a == b)  # False! Due to floating point precision

# Solution: Use np.isclose or np.allclose
print(np.isclose(a, b))  # True
print(np.allclose(a, b))  # True

# Cumulative floating point errors
arr = np.array([0.1] * 10)
print("Sum:", arr.sum())  # 1.0 but may not be exactly 1.0
print("Expected: 1.0, Got:", np.isclose(arr.sum(), 1.0))  # True
```

---

## 6. Array vs Matrix Multiplication

### The Issue
`*` is element-wise, not matrix multiplication.

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Element-wise multiplication
print("Element-wise:", A * B)  # [[5 12], [21 32]]

# Matrix multiplication
print("Matrix product:", A @ B)  # [[19 22], [43 50]]
print("Matrix product:", np.dot(A, B))  # Same as @

# For 1D arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Element-wise:", a * b)  # [4 10 18]
print("Dot product:", np.dot(a, b))  # 32 (sum of products)
```

---

## 7. NaN Propagation

### The Issue
NaN values propagate through operations.

```python
arr = np.array([1, 2, np.nan, 4, 5])
print("Mean with NaN:", np.mean(arr))  # nan

# Solution: Use nan-aware functions
print("Mean ignoring NaN:", np.nanmean(arr))  # 3.0
print("Sum ignoring NaN:", np.nansum(arr))  # 12.0

# Or fill NaN first
arr_filled = np.nan_to_num(arr, nan=0)
print("Mean after filling:", np.mean(arr_filled))  # 2.4
```

---

## 8. Indexing with np.newaxis

### The Issue
`np.newaxis` (or `None`) adds a dimension.

```python
arr = np.array([1, 2, 3, 4, 5])

# Row vector
row = arr[np.newaxis, :]  # (1, 5)
print("Row shape:", row.shape)

# Column vector
col = arr[:, np.newaxis]  # (5, 1)
print("Column shape:", col.shape)

# Can also use None
col = arr[:, None]  # Same as [:, np.newaxis]
```

---

## Summary

| Gotcha | Solution |
|--------|----------|
| Views vs Copies | Use `.copy()` when you need a copy |
| Broadcasting errors | Check shapes, use `.reshape()` |
| In-place vs new | Be aware of which operations modify |
| Integer overflow | Use larger dtype (int64, float64) |
| Float precision | Use `np.isclose()` for comparisons |
| Element-wise `*` | Use `@` or `np.dot()` for matrix multiply |
| NaN propagation | Use `np.nanmean()`, `np.nansum()`, etc. |
