import os
config_dir = os.environ["HOME"] + os.sep + ".twibot"
secret_file = config_dir + os.sep + "secrets"


def parse_data(data):
    """
    Split stored data
    """
    try:
        key, value = data.split("=")
        return key, value
    except Exception as err:
        print("[!] Error: {0}".format(err))
        return -1

def load_keys():
    """
    Load the API and SECRET key for the bot operations.
    """
    keys = dict()
    try:
        with open(secret_file, "r") as f:
            for line in f.readlines():
                k, v = parse_data(line.replace("\n", ""))
                keys[k] = v
    except Exception as err:
        print("[!] Error: {0}".format(err))
        return -1
    return keys
