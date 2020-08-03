
def safe_int(data, default=0) -> int:
    '''safely cast variable value to integer'''
    try:
        data = int(data)
    except (ValueError, TypeError):
        data = default

    return data
