# Utils

def __recur_fields(desired_fields, api_call):
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
            
            


            

        

