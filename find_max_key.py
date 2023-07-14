data = {
    1: 'a', 
    2: 'b', 
    3: 'c'
  }
def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    return max(data.keys())
print(find_max_key(data))