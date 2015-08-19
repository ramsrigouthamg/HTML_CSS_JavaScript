import urllib

def read_text():
    filepath = "/Users/avengers/Desktop/Github_Ramsri/HTML_CSS_JavaScript/ProgrammingFoundationsWithPython/movie_quotes.txt"
    quotes = open(filepath)
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection=urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print ("Profanity Alert!!")
    elif "false" in output:
        print ("This document has no curse words")
    else:
        print ("Couldn't scan the document properly or No internet Connection")
    
read_text()
