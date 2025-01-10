from typing import List, Tuple

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

# Example usage:
# A = [
#     [1, 2],
#     [3, 4],
#     [5, 6],
# ]
# print(shape(A))  # Output: (3, 2)
# print(get_row(A, 1))  # Output: [3, 4]
# print(get_column(A, 1))  # Output: [2, 4, 6]
