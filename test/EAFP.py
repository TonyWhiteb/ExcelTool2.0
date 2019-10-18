def keys_exists(element, *keys):
    '''
    Check if *keys (nested) exists in `element` (dict).
    '''
    if not isinstance(element, dict):
        raise AttributeError('keys_exists() expects dict as first argument.')
    if len(keys) == 0:
        raise AttributeError('keys_exists() expects at least two arguments, one given.')

    _element = element
    for key in keys:
        try:
            _element = _element[key]
        except KeyError:
            return False
    return True
def exists(obj, chain):
    _key = chain.pop(0)
    if _key in obj:
        return exists(obj[_key], chain) if chain else obj[_key]
data = {
    "spam": {
        "egg": {
            "bacon": "Well..",
            "sausages": "Spam egg sausages and spam",
            "spam": "does not have much spam in it"
        }
    }
}
print(exists(data,['spam']))
# print (keys_exists(data, "spam"))
# print ('spam > bacon (do not exists): {}'.format(keys_exists(data, "spam", "bacon")))
# print ('spam > egg (exists): {}'.format(keys_exists(data, "spam", "egg")))
# print ('spam > egg > bacon (exists): {}'.format(keys_exists(data, "spam", "egg", "bacon")))