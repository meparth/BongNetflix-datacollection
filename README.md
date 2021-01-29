# BongNetflix - Data collection
***
The codes that I used to collect relevent data (posters, rating, plot, cast etc.) from [netflix](netflix.com) and [imdb](imdb.com) and presented them in jekyll compatible _.md_ files. 

## The process
***
1. At first I had to get hold of the names of the shows available in Bangladesh. I browsed netflix and searched with the parsed genre codes that I got from [here](https://www.netflix-codes.com/) with python's beautiful soup package.
2. After I got the names of the shows, using imdb package, I got the necessary informations and the posters. 
3. To make all the information work on jekyll site, I created markdown files with them and saved them.

## The result
>The static jekyll site can be viewed here: https://meparth.github.io/BongNetflix/

