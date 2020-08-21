from blix_utils import *
import json
import random
import logging
import time
import imdb
import urllib3
import requests

logging.basicConfig(
    filename='app.log',
    filemode='a',
    format=
    '%(asctime)s.%(msecs)03d - %(funcName)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)



# print(getShowDetails("inception", netflix_id))

with open("id_to_show.json", "r") as inFile:
    id_to_show = json.load(inFile)
netflix_id_list = list(id_to_show.keys())

# there are total 4104 shows
start = 4104
end = 4106

for i in range(start, end):
    netflix_id = netflix_id_list[i]
    try:
        print("trying " + id_to_show[netflix_id])
        found, details = getShowDetails(id_to_show[netflix_id], netflix_id)
    except requests.exceptions.ConnectionError as e:
        print(e)
        print("retry this later, lets sleep for now..")
        with open("retries.txt", "a") as f:
            f.write(netflix_id+"\n")
        time.sleep(100)
        continue

    except imdb._exceptions.IMDbDataAccessError as e:
        print(e)
        print("retry this later, lets sleep for now..")
        with open("retries.txt", "a") as f:
            f.write(netflix_id + "\n")
        time.sleep(100)
        continue
    except urllib3.exceptions.ProtocolError as e:
        print(e)
        print("retry this later, lets sleep for now..")
        with open("retries.txt", "a") as f:
            f.write(netflix_id + "\n")
        time.sleep(100)
        continue

    if found == False:
        print("well, " + id_to_show[netflix_id] + " coundnt be found :|")
        continue

    # print("we got " + id_to_show[netflix_id])
    # logging.info("all done with " + id_to_show[netflix_id] + " (" + str(i) + ")")

    print("\n\n")

    with open("show_details.json", "r+") as show_details:
        data = json.load(show_details)
        data.update({netflix_id : details})
        show_details.seek(0)
        json.dump(data, show_details)
        show_details.write('\n')

    print("we got " + id_to_show[netflix_id])
    logging.info("all done with " + id_to_show[netflix_id] + " (" + str(i) + ")")

    hault = random.randint(5, 20)
    time.sleep(hault)
