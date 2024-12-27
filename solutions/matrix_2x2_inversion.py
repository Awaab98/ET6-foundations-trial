#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for testing and validating the inversion of a 2x2 matrix.

This module provides a function that computes the inverse of a given
2x2 matrix. The function raises appropriate errors for invalid inputs
or singular matrices.

Created on 2024-12-26
Author: Awaab98
"""


def matrix_2x2_inversion(matrix):
    """
    Compute the inverse of a 2x2 matrix.

    Args:
        matrix (list[list[float]]): A 2x2 matrix to be inverted.

    Returns:
        list[list[float]]: The inverse of the input matrix.

    Raises:
        ValueError: If the matrix determinant is zero (non-invertible).
        TypeError: If the matrix contains non-numeric elements.
        AssertionError: If the matrix is not 2x2 in shape.
    """
    assert len(matrix) == 2 and all(len(row) == 2 for row in matrix), (
        "Input must be a 2x2 matrix."
    )

    a, b = matrix[0]
    c, d = matrix[1]

    # Compute determinant
    determinant = a * d - b * c
    if determinant == 0:
        raise ValueError("Matrix is not invertible (determinant is zero).")

    # Validate numeric elements
    if not all(
        isinstance(element, (int, float)) for row in matrix for element in row
    ):
        raise TypeError("Matrix elements must be numeric.")

    # Compute and return the inverse
    inverse = [
        [d / determinant, -b / determinant],
        [-c / determinant, a / determinant],
    ]
    return inverse
