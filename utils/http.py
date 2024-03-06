
def json_response(data):
    if data is None:
        return data
    if isinstance(data , list) :
      return [ dt.__json__() for dt in data] 
    else :
        return data.__json__()
        