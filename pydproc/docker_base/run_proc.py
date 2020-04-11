# this is the python script that runs inside docker container

# import dependencies
import yaml
import requests, json
import time
from scripts.utils import __scrap_fields, __cleanup

def load_specs(filename="proc.yml"):
    """
    Load specs from yaml file
    :param filename: spec_file
    :return: dictionary
    """
    with open("proc.yml", "r+") as f:
        specs = yaml.safe_load(f)
    return specs


def get_data(url):
    """
    Returns JSON data from url or {} if 404 error
    :param url: string that has JSON data
    :return: dictionary
    """
    response = requests.get(url)
    x = response.json()
    if x["cod"] != 404:
        return x
    else:
        print("404 Error: url not found.")
        return {}


def filter_data(data, fields):
    """
    Removes keys in data that are not part of fields
    :param data: dict of data
    :param fields: dict representing the keys/indexes to be saved
    :return: a dict with the parsed data inside
    """
    
    def scrap_fields(data, fields):
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
    
    def cleanup(data):
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
    
    clean_data = cleanup(scrap_fields(data, fields))
    
    fin_data = {}
    for key in list(clean_data.keys()):
        if clean_data[key]:
            fin_data[key] = clean_data[key]

    return fin_data


def main():
    # Load specs from file
    specs = load_specs()
    print(f"Specs loaded from proc.yml: {specs}")

    # Convert time interval in hours to milliseconds
    h_interval = specs["time_interval"]
    s_interval = h_interval * 60 * 60
    print(f"Time interval in seconds computed to be {s_interval}")

    # Get url
    complete_url = specs["base_url"].format(**specs["url_params"])
    print(f"Complete url for requests: {complete_url}")

    # Main loop
    for i in range(specs["max_requests"]):
        # Get new data
        new_data = get_data(complete_url)

        # Save data to file
        with open(f"/saved_data/{time.time()}-data.yml", "w+") as f:
            f.write(yaml.dump(new_data))

        # Wait for next time interval
        time.sleep(s_interval)


if __name__ == "__main__":
    main()
