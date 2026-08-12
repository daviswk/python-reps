"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.  # noqa: E501
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


# TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


# TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.  # noqa: E501
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.


def preparation_time_in_minutes(number_of_layers):
    """Calculate prepation time in minutues.

    Parameters:
       number_of_layers (int): Number of layers being added.
       total_time (int): Numbers of layers times prepation time.
    Returns:
        int: The preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function takes the number of layers being used in the recipe and multiplies it by the 'PREPARATION_TIME'.
    """  # noqa: E501
    return number_of_layers * PREPARATION_TIME


# TODO (student): define the 'elapsed_time_in_minutes()' function below.


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate elapsed time in minutues.

    Parameters:
       number_of_layers (int): Number of layers being added.
       elapsed_bake_time (int): Time since lasagna has started baking in the oven.
    Returns:
        int: total elapsed time since preparation and cook time

    Function takes the number of layers being used and the elapsed bake time
    and adds them together for a total elpased time.
    """
    layer_time = number_of_layers * PREPARATION_TIME
    return layer_time + number_of_layers + elapsed_bake_time


# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
