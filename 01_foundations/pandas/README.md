# Pandas Data Manipulation

Learn data manipulation, cleaning, and analysis with pandas.

## Learning Objectives

- Understand Series and DataFrame structures
- Perform data cleaning and preprocessing
- Handle missing data effectively
- Master groupby operations and aggregations
- Merge and join datasets
- Apply time series operations

## File Map

| Notebook | Topic | Key Concepts |
|----------|-------|--------------|
| [`Pandas.ipynb`](Pandas.ipynb) | DataFrames & Series | Creation, indexing, operations |
| `*-exercise.ipynb` | Practice | Hands-on exercises |
| `*-solution.ipynb` | Solutions | Answer key |

## Key Topics Covered

### Data Structures
- **Series**: 1D labeled array
- **DataFrame**: 2D labeled data structure

### Data Operations
- Selection and indexing
- Boolean indexing
- SettingWithCopy warnings

### Data Cleaning
- Missing data handling (`dropna`, `fillna`)
- Data type conversion
- String operations

### Transformations
- `groupby()` and aggregations
- `pivot_table()`
- `melt()` and `pivot()`

### Merging & Joining
- `merge()`, `join()`, `concat()`
- Handling alignment gotchas

## Gotchas to Watch

1. **SettingWithCopyWarning**: Use `.loc` for chained assignment
2. **View vs Copy**: Understand when pandas returns views vs copies
3. **Index Alignment**: Operations align on index automatically
4. **Chained Indexing**: Avoid `df[i][j]` - use `df.loc[i, j]`

## Related Topics

- NumPy for array operations
- Matplotlib/Seaborn for visualization
- Scikit-learn for preprocessing
