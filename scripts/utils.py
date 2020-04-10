# Utils

def __recur_fields(api_call, desired_fields):
    """
    Reads through API data to make sure client desired data is present

    :param api_call: is the working API data in a dict
    :param desired_fields: is the client desired data in a dict
    """
    for element in desired_fields:
        if isinstance(element, dict):
            keys = list(element.keys())
            try:
                for k in keys:
                    cur1 = element[k]
                    cur2 = api_call[k]
                    __recur_fields(cur1, cur2)
            except:
                raise Exception('WARNING: Incorrect desired data')
        else:
            for l in desired_fields:
                if l not in api_call:
                    print(desired_fields)
                    print(api_call)
                    raise Exception('WARNING: desired data ' + l + ' not present in desired data')


def __scrap_fields(data, fields):
    """
    Removes data not necessary to the client
    
    :param data: dict of the working API data
    :param fields: are the data fields the client wants saved in a dict
    """
    for element in data:
        working_keys = list(element.keys())
        cur_keys = list(fields.keys())
        for key in working_keys:
            if not isinstance(data[key], dict):
                if key not in cur_keys:
                    del data[key]
            else:
                if key in cur_keys:
                    data = __recur_fields(data[key], fields[key])
                else:
                    data = __recur_fields(data[key], fields)
        return data
            
def __cleanup(data):
    """
    Remove null values from parsed API data

    :param data: parsed API data in a dict
    """
    if isinstance(data, dict):
        return_data = {}
        for key in data.keys():
            if data[key] is not None:
                return_data[key] = __cleanup(data[key])
        return return_data
    elif isinstance(data, list):
        l = []
        for item in data:
            l.append(__cleanup(item))
        return l
    else:
        return data


            

        

