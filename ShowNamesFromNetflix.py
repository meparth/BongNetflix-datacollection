import json
import bs4 as bs
import urllib.request
import urllib.error
import time
import random

from blix_utils import *


import logging

logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s.%(msecs)03d - %(funcName)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)




# loading the codes:name dictionary
with open("all_codes.json", "r") as inFile:
    code_map = json.load(inFile)
all_codes = list(code_map.keys())



# do this in multiple parts
# there are 215 genres
start = 205
end = 216
# n_per_genre = 10
# n_curr_genre = 0

# for every genre codes
for i in range(start, end):
    code = all_codes[i]
    print("*** getting all " + code_map[code]+"...")

    id_to_show = {}
    id_to_show = getNetflixData(code)


    with open("id_to_show.json", "r+") as all_show_names:
        data = json.load(all_show_names)
        data.update(id_to_show)
        all_show_names.seek(0)
        json.dump(data, all_show_names)




    hault = random.randint(5, 20)
    time.sleep(hault)
    print("... and done, found " + str(len(id_to_show)) + " titles")

    logging.info('got ' + code_map[code] + " (" + str(i) + "), total titles: " + str(len(id_to_show)))


# write to file
# list_movie_names = list(movie_names)


# # save list in txt
# with open("all_movie_names.txt", "a+") as zing:
#     for name in list_movie_names:
#         zing.write('%s\n' % name)



# json way
# names_obj = json.dumps(list_movie_names)
# with open("all_movie_names.json", "r+") as all_movie_names:
#     data = json.load(all_movie_names)
#     data.update(list_movie_names)
#     file.seek(0)
#     json.dump(data, all_movie_names)
# with open("all_movie_names.json", "w") as outFile:
#     outFile.write(names_obj)



# to read

# places = []
### open file and read the content in a list
# with open('listfile.txt', 'r') as filehandle:
#     for line in filehandle:
#         # remove linebreak which is the last character of the string
#         currentPlace = line[:-1]

#         # add item to the list
#         places.append(currentPlace)



# try:
#     source = urllib.request.urlopen('https://www.netflix.com/bd/browse/genre/'+code).read()
# except urllib.error.HTTPError as e:
#     print(e)
#     print("skipping..")
#     continue
# except urllib.error.URLError as e:
#     print(e)
#     print("bro you connected?")
#     continue

# soup = bs.BeautifulSoup(source,'lxml')
# all_movies = soup.find_all("span", class_="nm-collections-title-name")

# # get the ID, NAME, and store the poster
# for m in all_movies:
#     name = m.string.encode(encoding='ascii', errors='ignore').decode()
#     movie_names.add(name)
#     print("found "+name)
