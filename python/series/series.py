def slices(series, length):
    if length < 1:
        raise ValueError("Length has to be larger than 0.")

    if length > len(series):
        raise ValueError("Length has to be smaller than length of series.")

    return [series[i:i+length] for i in range(len(series) - length + 1)]
