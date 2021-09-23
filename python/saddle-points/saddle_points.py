from typing import Dict, List

def transpose(matrix: List[List[int]]) -> List[List[int]]:
    return [list(x) for x in zip(*matrix)]

def saddle_points(matrix: List[List[int]]) -> List[Dict[str, int]]:
    if matrix != transpose(transpose(matrix)):
        raise ValueError("This is not a matrix")

    return [
        {"row": row_index + 1, "column":column_index + 1}
        for row_index, row in enumerate(matrix)
        for column_index, element in enumerate(row)
        if element == max(row) and element == min(transpose(matrix)[column_index])
    ]
