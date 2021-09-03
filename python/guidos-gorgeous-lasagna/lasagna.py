# time it takes to bake the lasagna
EXPECTED_BAKE_TIME = 40
# time it takes to prepare a layer of lasagna
PREPARATION_TIME = 2
def bake_time_remaining(elapsed_bake_time: int) -> int:
    """
    :param elapsed_bake_time: int baking time already elapsed
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
def preparation_time_in_minutes(number_of_layers: int) -> int:
    """
    Computes the preparation time in minutes for a lasagna

    Args:
        number_of_layers (int): number of layers of the lasagna

    Returns:
        int: preparartion time in minutes
    """
    return PREPARATION_TIME * number_of_layers
def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """
    Total number of minutes elapsed while cooking the lasagna

    Args:
        number_of_layers (int): number of layers of the lasagna
        elapsed_bake_time (int): number of minutes the lasagna has been baking in the oven

    Returns:
        int: total time spent cooking the lasagna up to this point (in minutes)
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
