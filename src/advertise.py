import tweepy
from twibot.colors import *

def advertise(api, data):
    data_size = len(data)

    #  Check for data
    if data_size < 1:
        print(ERROR + "No data to send.")
        return -1

    debug_0 = INFO + "Received {0} bytes of data.".format(data_size)
    print(debug_0)

    #  Post the tweet.
    api.update_status(data)
    return 0

