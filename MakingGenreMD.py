genres = ["Drama", "Romance", "Action", "Adventure", "Horror", "Documentary", "War", "History", "Crime", "Sci-Fi", "Comedy", "Musical", "Western", "Mystery", "Thriller", "Fantasy", "Music", "Animation", "Family", "Biography", "Sport", "Short", "Reality-TV", "News", "Talk-Show", "Game-Show", "Film-Noir"]

for g in genres:
    md_text = "---\n"
    md_text += "title: "
    md_text += g + "\n"
    md_text += "layout: "
    md_text += "single-genre\n"
    md_text += "permalink: "
    md_text += "/g/" + g + "\n"
    md_text += "genre: " + g + "\n"
    md_text += "---"




    with open("md_pages/g-" + g + ".md", "w",
            encoding="utf-8") as zing:
        zing.write(md_text)


"""

---
title: Action
layout: single-genre
permalink: /g/action/
genre: Action
---

"""