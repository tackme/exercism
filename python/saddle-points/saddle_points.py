from typing import Dict, List

def transpose(matrix: List[List[int]]) -> List[List[int]]:
    return [list(x) for x in zip(*matrix)]

def saddle_points(matrix: List[List[int]]) -> List[Dict[str, int]]:
    if matrix != transpose(transpose(matrix)):
        raise ValueError("This is not a matrix")


    return [
        {"row": row_index + 1, "column":colmun_index + 1}
        for row_index, row in enumerate(matrix)
        for colmun_index, item in enumerate(row)
        if item == max(row) and item == min(transpose(matrix)[colmun_index])
    ]
