data = [
  {
    'name': 'John', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 42
  }
]
def get_max_age_user_name(data:list) -> str:
    """
    Return the name of the user with the maximum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the maximum age in the dictionary
    """
    name=''
    age=0
    for i in data:
        if i['age']>age:
            age=i['age']
            name=i['name']
    return name
print(get_max_age_user_name(data))