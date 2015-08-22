# 3a Movie Website

import webbrowser
import fresh_tomatoes

class Movie():
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
    


toy_story = Movie("Toy Story",
                  " Story Line",
                  "http://4.bp.blogspot.com/-hH0sGT1XR_8/VUmCiadeGlI/AAAAAAAAVvQ/MPzKEmrT45A/s1600/Baahubali%2BShivudu.jpg",
                  "https://www.youtube.com/watch?v=ZZv1vki4ou4"
                  )

avatar = Movie("Avatar",
                  " Story Line",
                  "http://4.bp.blogspot.com/-hH0sGT1XR_8/VUmCiadeGlI/AAAAAAAAVvQ/MPzKEmrT45A/s1600/Baahubali%2BShivudu.jpg",
                  "https://www.youtube.com/watch?v=cRdxXPV9GNQ"
                  )
baahubali = Movie("Baahubali",
                  " Story Line",
                  "http://4.bp.blogspot.com/-hH0sGT1XR_8/VUmCiadeGlI/AAAAAAAAVvQ/MPzKEmrT45A/s1600/Baahubali%2BShivudu.jpg",
                  "https://www.youtube.com/watch?v=sOEg_YZQsTI"
                  )
movies= [toy_story,avatar,baahubali]

fresh_tomatoes.open_movies_page(movies)

