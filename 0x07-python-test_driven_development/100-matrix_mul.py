#!/usr/bin/python3
"""Module name: 100-matrix_mul.py
multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
                   or contains non-integer/float values.
        ValueError: If m_a or m_b is empty, or if m_a and m_b
                    cannot be multiplied.
        TypeError: If m_a and m_b are not rectangular.
    """
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")

    if not m_b or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")

    if not all(isinstance(value, (int, float)) for row in m_a for value in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(value, (int, float)) for row in m_b for value in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for x in range(len(m_a)):
        for y in range(len(m_b[0])):
            for z in range(len(m_b)):
                result[x][y] += m_a[x][z] * m_b[z][y]

    return result
