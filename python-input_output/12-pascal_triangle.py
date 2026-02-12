#!/usr/bin/python3

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing 
    the Pascal’s triangle of n.
    """
    # Requirement: Return empty list if n <= 0
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # We already have row 0, so we build from row 1 up to n-1
    for i in range(1, n):
        # Every row starts with 1
        row = [1]
        
        # Get the previous row to calculate middle values
        prev_row = triangle[i - 1]
        
        # Each middle element is the sum of the two elements above it
        # The number of middle elements grows as 'i' increases
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
            
        # Every row ends with 1
        row.append(1)
        
        # Add the completed row to our triangle
        triangle.append(row)

    return triangle