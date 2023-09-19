import pprint
def decorate_as_strings(func):
    def wrapper(*args, **kwargs):
      result = func(*args, **kwargs)
      result = str(result)
      return result
    return wrapper

@decorate_as_strings
def list_to_strings(list1: list, list2: list) -> list:
    return list1 + list2

pprint.pprint(list_to_strings(['ale'],['kto tam?']))
