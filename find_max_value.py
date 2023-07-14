data = {
    'a' : 1, 
    'b' : 2, 
    'c' : 3
}
def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    ans=0
    for i in data:
        if data[i]>ans:
            ans=data[i]
    return ans
print(find_max_value(data))