from PIL import Image
import requests
import json
import bs4 as bs
import urllib.request
import urllib.error
import time
import random
import imdb




def getNetflixData(genre_code):
    """ get {movie name: id} from genre id """
    # uses: json, bs4, urllib.request, urllib.error, time, random

    # returnable dictionary:
    id_to_show = {}

    try:
        source = urllib.request.urlopen('https://www.netflix.com/bd/browse/genre/'+genre_code).read()
    except urllib.error.HTTPError as e:
        print(e)
        print("skipping..")
        return id_to_show
    except urllib.error.URLError as e:
        print(e)
        print("bro you connected?")
        return id_to_show

    # the whole page
    soup = bs.BeautifulSoup(source,'lxml')

    all_shows = soup.find_all("img", class_="nm-collections-title-img")
    for m in all_shows:
        show_id = m['data-title-id']
        # poster_url = m['src']
        show_name = m['alt']

        id_to_show[show_id] = show_name

        ### if you wanna save the posters
        # path = "C:/Users/Partha/Documents/somethingsomethingnetflix/posters"
        # try
        # try:
        #     img = Image.open(requests.get(poster_url, stream=True).raw)
        #     img.save(path+'/'+movie_id+'.jpg')
        # except requests.exceptions.InvalidSchema as e:
        #     print(e)
        #     print("skipping...")

    return id_to_show






# from id_to_movie, get names and write


def saveImg(url, imdb_id):
    """ download image and save to file """
    # uses: PIL, req

    # url = "https://occ-0-2484-2186.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABQgQmh6BDX9OYZs9URfjj1ZjPmOtFLN4oW6HsaWq7RtmYMSoYJitx-QujjAQnUCqvhrBxFhUsCNXLBLidqX1jL6qOcLvOmn8NR3Q7WeTutpYrY8gi47fY9hdzhIW.jpg?r=80c"
    # folder path
    # path = "C:/Users/Partha/Documents/somethingsomethingnetflix/res"
    img_path = "C:/Users/Partha/Documents/somethingsomethingnetflix/posters"
    img = Image.open(requests.get(url, stream=True).raw)
    img.save(img_path + '/' + imdb_id + '.jpg')





# generate markdown posts
colors = [
    'E76F51', 'F4A261', '2A9D8F', '264653', '495867', '472d30', '8d99ae',
    '1b263b', '533747', '513b56', '432818', '5e503f', 'c44536', '2c6e49',
    '774936', '114b5f', '7c616c', 'ee6c4d', '004643', '4ecdc4'
]
# curr_color = 0


def createMarkdownPost(details):
    """ takes details of a show, creates a markdown doc with it """
    # imdb_id
    # netflix_id
    # title
    # genres
    # tags
    # rating
    # votes
    # plot_outline
    # kind
    # year
    # directors
    # cast
    # plot
    # cover_url

    md_text = "---\n"
    md_text += "layout: post\n"
    md_text += "title: \"" + details['title'] + "\"\n"
    plot_outline = details['plot_outline'].replace("\"", "")
    md_text += "description: \"" + plot_outline + "\"\n"
    if details['cover_url']!='':
        md_text += "img: " + details['imdb_id'] + ".jpg\n"
    md_text += "kind: " + details['kind'] + "\n"
    md_text += "genres: ["
    g_count = 0
    for g in details['genres']:
        if g_count>0:
            md_text += ","
        md_text += g
        g_count +=1
    md_text += "]\n"
    md_text += "tags: "
    for g in details['genres']:
        md_text += g + " "
    md_text += "\n"
    md_text += "language: " + details['language'] + "\n"
    md_text += "year: " + details['year'] + "\n"
    md_text += "imdb_rating: " + details['rating'] + "\n"
    md_text += "votes: "  + details['votes'] + "\n"
    md_text += "imdb_id: " + details['imdb_id'] + "\n"
    md_text += "netflix_id: " + details['netflix_id'] + "\n"

    md_text += "color: " + colors[random.randint(0, 19)] + "\n"
    # curr_color += 1
    md_text += "---"

    md_text += "\nDirector: " + "`" + details['directors'][0] + "`"
    if len(details['directors'])>1:
        md_text += " `" + details['directors'][1] + "`"

    md_text += "  \n\n"

    md_text += "Cast: "
    c_count = 0
    for c in details['cast']:
        md_text += "`" + c + "` "

    md_text += "\n\n" + details['plot']

    md_text = md_text.encode('utf-8', errors='ignore').decode()

    posts_path = "C:/Users/Partha/Documents/jekyll/BongNetflix/_posts"

    with open(posts_path + "/2020-01-01-" + details['imdb_id'] + ".md",
              "w",
              encoding="utf-8") as zing:
        zing.write(md_text)

fake_details = {
    "imdb_id" : "00000000000000",
    "netflix_id" : "33123123",
    "title" : "hum nikalte hain",
    "genres" : ['some','thing', 'fun'],
    "rating" : "5.5",
    "votes" : "234423",
    "plot_outline" : "Dom Cobb is a skilled thief, the absolute best in the dangerous art of extraction, stealing valuable secrets from deep within the subconscious during the dream state, when the mind is at its most vulnerable. Cobb's rare ability has made him a coveted player in this treacherous new world of corporate espionage, but it has also made him an international fugitive and cost him everything he has ever loved...",
    "kind" : "mubi",
    "year" : "2019",
    "language" : "unagi",
    "directors" : ["a", "b"],
    "cast" : ["d", "k", "ddk"],
    "plot" : "Dominic Cobb is the foremost practitioner of the artistic science of extraction, inserting oneself into a subject's dreams to obtain hidden information without the subject knowing, a concept taught to him by his professor father-in-law, Dr. Stephen Miles. Dom's associates are Miles' former students, who Dom requires as he has given up being the dream architect for reasons he won't disclose. Dom's primary associate, Arthur, believes it has something to do with Dom's deceased wife, Mal, who often figures prominently and violently in those dreams, or Dom's want to \"go home\" (get back to his own reality, which includes two young children). Dom's work is generally in corporate espionage. As the subjects don't want the information to get into the wrong hands, the clients have zero tolerance for failure. Dom is also a wanted man, as many of his past subjects have learned what Dom has done to them. One of those subjects, Mr. Saito, offers Dom a job he can't refuse: to take the concept one step further into inception, namely planting thoughts into the subject's dreams without them knowing. Inception can fundamentally alter that person as a being. Saito's target is Robert Michael Fischer, the heir to an energy business empire, which has the potential to rule the world if continued on the current trajectory. Beyond the complex logistics of the dream architecture of the case and some unknowns concerning Fischer, the biggest obstacles in success for the team become worrying about one aspect of inception which Cobb fails to disclose to the other team members prior to the job, and Cobb's newest associate Ariadne's belief that Cobb's own subconscious, especially as it relates to Mal, may be taking over what happens in the dreams.::Huggo",
    "cover_url" : "gruu"
}
# createMarkdownPost(fake_details)

def getShowDetails(show_name, netflix_id):
    """ given a show's name, a dictionary of 
    - imdb_id,
    - netflix_id,
    - title,
    - genres
    - language
    - rating
    - votes
    - plot_outline
    - year
    - kind
    - directors
    - writers //
    - cast
    - plot
    - full-size cover url
    will be returned """

    # uses imdb

    # show = sdb.get_movie(sdb.search_movie("3 idiots")[0].getID())
    found = True
    details = {}

    showDB = imdb.IMDb()
    show_from_search = showDB.search_movie(show_name)
    if len(show_from_search)==0:
        return (False, details)


    imdb_id = show_from_search[0].getID()
    show = showDB.get_movie(imdb_id)



    if 'title' in show:
        title = show['title']
    else:
        title = show_name

    if 'genres' in show:
        genres = show['genres'][:5]
    else:
        genres = ['N/A']

    if 'languages' in show:
        language = show['languages'][0]
    else:
        language = 'N/A'

    if 'rating' in show:
        rating = str(show['rating'])
    else:
        rating = 'N/A'

    if 'votes' in show:
        votes = str(show['votes'])
    else:
        votes = 'N/A'


    if 'year' in show:
        year = str(show['year'])
    else:
        year = 'N/A'

    if 'kind' in show:
        kind = show['kind']
    else:
        kind = 'N/A'

    if 'directors' in show:
        directors = [d['name'] for d in show['directors']][:2]
    else:
        directors = ['N/A']

    # if 'writers' in show:
    #     writers = [w['name'] for w in show['writers']][:2]
    # else:
    #     writers = ['N/A']

    if 'cast' in show:
        cast = [c['name'] for c in show['cast']][:5]
    else:
        cast = ['N/A']

    if 'plot' in show:
        plots = show['plot']
        plots_len = [len(p) for p in plots]
        plot = plots[plots_len.index(max(plots_len))]
    else:
        plot = 'N/A'

    if 'plot outline' in show:
        plot_outline = show['plot outline']
    else:
        plot_outline = plot

    r = random.randint(400, 600)
    plot_outline = plot_outline[:r] + ".."

    cover_url = show.get('full-size cover url')
    if not cover_url:
        cover_url = ''


    details['imdb_id'] = imdb_id
    details['netflix_id'] = netflix_id
    details['title'] = title
    details['genres'] = genres
    details['language'] = language
    details['rating'] = rating
    details['votes'] = votes
    details['plot_outline'] = plot_outline
    details['kind'] = kind
    details['year'] = year
    details['directors'] = directors
    # details['writers'] = writers
    details['cast'] = cast
    details['plot'] = plot
    details['cover_url'] = cover_url


    # make markdowns with the details
    createMarkdownPost(details)
    # save the image
    if cover_url!='':
        saveImg(cover_url, imdb_id)

    return (found, details)

# ['cast', 'genres', 'runtimes', 'countries', 'country codes', 'language codes', 'color info', 'aspect ratio', 'sound mix'
# , 'box office', 'certificates', 'original air date', 'rating', 'votes', 'cover url', 'plot outline', 'languages', 'title
# ', 'year', 'kind', 'directors', 'writers', 'producers', 'composers', 'cinematographers', 'editors', 'editorial departmen
# t', 'casting directors', 'production designers', 'art directors', 'set decorators', 'costume designers', 'make up depart
# ment', 'production managers', 'assistant directors', 'art department', 'sound department', 'special effects', 'visual ef
# fects', 'stunts', 'camera department', 'animation department', 'casting department', 'costume departmen', 'location mana
# gement', 'music department', 'script department', 'transportation department', 'miscellaneous', 'thanks', 'akas', 'write
# r', 'director', 'production companies', 'distributors', 'special effects companies', 'other companies', 'plot', 'synopsi
# s', 'canonical title', 'long imdb title', 'long imdb canonical title', 'smart canonical title', 'smart long imdb canonic
# al title', 'full-size cover url']



# getShowDetails("The Woods", "81108061")