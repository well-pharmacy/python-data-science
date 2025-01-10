from typing import List, Tuple, Callable

Matrix = List[List[float]]
Vector = List[float]

def shape(A: Matrix) -> Tuple[int, int]:
    """
    Returns the number of rows and columns of the matrix A.

    Args:
    A (Matrix): A matrix represented as a list of lists.

    Returns:
    Tuple[int, int]: A tuple containing the number of rows and columns.
    """
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A: Matrix, i: int) -> Vector:
    """
    Returns the i-th row of the matrix A.

    Args:
    A (Matrix): A matrix represented as a list of lists.
    i (int): The index of the row to retrieve.

    Returns:
    Vector: The i-th row of the matrix.
    """
    return A[i]

def get_column(A: Matrix, j: int) -> Vector:
    """
    Returns the j-th column of the matrix A.

    Args:
    A (Matrix): A matrix represented as a list of lists.
    j (int): The index of the column to retrieve.

    Returns:
    Vector: The j-th column of the matrix.
    """
    return [A_i[j] for A_i in A]

def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float]) -> Matrix:
    """
    Creates a num_rows x num_cols matrix where the (i, j)-th entry is entry_fn(i, j).

    Args:
    num_rows (int): The number of rows in the matrix.
    num_cols (int): The number of columns in the matrix.
    entry_fn (Callable[[int, int], float]): A function that takes two integers (i, j) and returns the value for the (i, j)-th entry.

    Returns:
    Matrix: A matrix represented as a list of lists.
    """
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]

# Example usage:
# A = [
#     [1, 2],
#     [3, 4],
#     [5, 6],
# ]
# print(shape(A))  # Output: (3, 2)
# print(get_row(A, 1))  # Output: [3, 4]
# print(get_column(A, 1))  # Output: [2, 4, 6]

# def entry_fn(i: int, j: int) -> float:
#     return i * j
# 
# matrix = make_matrix(3, 3, entry_fn)
# print(matrix)  # Output: [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
