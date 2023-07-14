data = {
    'a': 'abc',
    'b': 'def', 
    'c': 'ghi'
}
def find_length_of_values(data: dict) -> int:
    """
    Return the sum of the length of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of the length of all values in the dictionary.
    """
    ans=0
    for i in data:
        ans+=len(data[i])
    return ans
print(find_length_of_values(data))