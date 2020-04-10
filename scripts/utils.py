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


def __recur_fields(data, fields):
    for element in data_fields:
        if isinstance(element, dict):
            working_keys = list(element.keys())
            cur_keys = list(fields.keys())
            for key in working_keys:
                if key in cur_keys:
                    __recur_fields(data[key], fields[key])
                else:
                    __recur_fields(data[key], fields)
        else:
             

            

        

