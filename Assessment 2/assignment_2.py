
from cProfile import label
from cgitb import text
from datetime import datetime
from email import message
from faulthandler import disable
from multiprocessing.sharedctypes import Value
from os import P_DETACH, scandir
from sre_parse import State
from sys import exit as abort, maxsize
from tkinter import font
from tkinter.font import BOLD
from turtle import bgcolor, down, width
from urllib.error import URLError

# A function for opening a web document given its URL.
# [You WILL need to use this function in your solution,
# either directly or via the "download" function below.]
from urllib.request import urlopen

# Some standard Tkinter functions.  [You WILL need to use
# SOME of these functions in your solution.]  You may also
# import other widgets from the "tkinter" module, provided they
# are standard ones and don't need to be downloaded and installed
# separately.  (NB: Although you can import individual widgets
# from the "tkinter.tkk" module, DON'T import ALL of them
# using a "*" wildcard because the "tkinter.tkk" module
# includes alternative versions of standard widgets
# like "Label" which leads to confusion.  If you want to use
# a widget from the tkinter.ttk module name it explicitly,
# as is done below for the progress bar widget.)
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar



# Functions for finding occurrences of a pattern defined
# via a regular expression.  [You do not necessarily need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.]
from re import *


# A function for displaying a web document in the host
# operating system's default web browser (renamed to
# distinguish it from the built-in "open" function for
# opening local files).  [You WILL need to use this function
# in your solution.]
from webbrowser import open as urldisplay

# All the standard SQLite database functions.
from sqlite3 import *





def download(url = 'http://www.wikipedia.org/',
             target_filename = 'downloaded_document',
             filename_extension = 'html',
             save_file = True,
             char_set = 'UTF-8',
             incognito = False):

    # Import the function for opening online documents and
    # the class for creating requests
    from urllib.request import urlopen, Request

    # Import an exception sometimes raised when a web server
    # denies access to a document
    from urllib.error import HTTPError

    # Import an exception raised when a web document cannot
    # be downloaded due to some communication error
    from urllib.error import URLError

    # Open the web document for reading (and make a "best
    # guess" about why if the attempt fails, which may or
    # may not be the correct explanation depending on how
    # well behaved the web server is!)
    try:
        if incognito:
            # Pretend to be a web browser instead of
            # a Python script (NOT RELIABLE OR RECOMMENDED!)
            request = Request(url)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                               'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                               'Chrome/42.0.2311.135 Safari/537.36 Edge/12.246')
            print("Warning - Request does not reveal client's true identity.")
            print("          This is both unreliable and unethical!")
            print("          Proceed at your own risk!\n")
        else:
            # Behave ethically
            request = url
        web_page = urlopen(request)
    except ValueError as message: # probably a syntax error
        print("\nCannot find requested document '" + url + "'")
        print("Error message was:", message, "\n")
        return None
    except HTTPError as message: # possibly an authorisation problem
        print("\nAccess denied to document at URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None
    except URLError as message: # probably the wrong server address
        print("\nCannot access web server at URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None
    except Exception as message: # something unexpected
        print("\nSomething went wrong when trying to download " + \
              "the document at URL '" + str(url) + "'")
        print("Error message was:", message, "\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
    except UnicodeDecodeError as message:
        print("\nUnable to decode document from URL '" + \
              url + "' as '" + char_set + "' characters")
        print("Error message was:", message, "\n")
        return None
    except Exception as message:
        print("\nSomething went wrong when trying to decode " + \
              "the document from URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Optionally write the contents to a local text file
    # (overwriting the file if it already exists!)
    if save_file:
        try:
            text_file = open(target_filename + '.' + filename_extension,
                             'w', encoding = char_set)
            text_file.write(web_page_contents)
            text_file.close()
        except Exception as message:
            print("\nUnable to write to file '" + \
                  target_filename + "'")
            print("Error message was:", message, "\n")

    # Return the downloaded document to the caller
    return web_page_contents

# Your code goes here
my_window = Tk()
#TITLE
my_window.title('NEWS OUTLET')

#sizing of window
my_window.minsize(880,880)
my_window.maxsize(880,880)

#background
bg ='peach'

#size of the window screen
my_window.geometry('880x880')

#intvar
var=IntVar()

#Pictures to be used
main_image = PhotoImage(file='newspaper2.png')

#frame label for the image
label1= Label(my_window, image= main_image, bg= 'white',)
label1.grid(row=1,column=0)
title1 = Label(my_window, text='THE WORLD NEWS', font=('Times Roman',20,BOLD), border=3,relief='solid',highlightbackground= 'black',highlightthickness= 2)
title1.grid(row=0, column=0)

#downloading the source when radiobuttons are choosen
def downloading_sources():
    if var.get()== 1:
        
        #Enables the buttons again so it can be used
        show_sources['state'] = NORMAL
        show_headlines['state'] = NORMAL
        print_stories['state'] = NORMAL
        save_stories['state'] = NORMAL
        website = download('https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')

        #check if internet connection is availabile or not
        if(website==None):
            Message_box.delete('1.0',END)
            Message_box.insert(END,'ERORR! There is no internet connection')
            return

        #inserts the message that the sources have been downloaded
        Message_box.delete('1.0',END)
        Message_box.insert(END,'The news sources from NewYork Times has been downloaded.')
    elif var.get()==2:

        #Enables the buttons again so it can be used
        show_sources['state'] = NORMAL
        show_headlines['state'] = NORMAL
        print_stories['state'] = NORMAL
        save_stories['state'] = NORMAL
        website = download('https://moxie.foxnews.com/google-publisher/latest.xml')

        #check if internet connection is availabile or not
        if(website==None):
            Message_box.delete('1.0',END)
            Message_box.insert(END,'ERORR! There is no internet connection')
            return

        #inserts the message that the sources have been downloaded
        Message_box.delete('1.0',END)
        Message_box.insert(END,'The news sources from Fox News has been downloaded.')
    else:

        #Enables the buttons again so it can be used
        show_sources['state'] = NORMAL
        show_headlines['state'] = NORMAL
        print_stories['state'] = NORMAL
        save_stories['state'] = NORMAL
        website = download('https://www.9news.com/feeds/syndication/rss/news')

         #check if internet connection is availabile or not
        if(website==None):
            Message_box.delete('1.0',END)
            Message_box.insert(END,'ERORR! There is no internet connection')
            return

        #inserts the message that the sources have been downloaded
        Message_box.delete('1.0',END)
        Message_box.insert(END,'The news sources from Nine News has been downloaded.')

#The functionality of the first button which shows the sources to the user
def sources():
    if var.get() == 1:
        urldisplay('https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')
    elif var.get() == 2:
        urldisplay('https://moxie.foxnews.com/google-publisher/latest.xml')
    else:
        urldisplay('https://www.9news.com/feeds/syndication/rss/news')



#functioanlity of the second button
def radio_functionality():
    Message_box['state'] = NORMAL
    Message_box.delete('1.0',END)

    #displays the headlines for NEWYORK TIMES
    if var.get() == 1:
        website = download('https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')
        if website == '':
            raise Exception('Sorry no string to be found')
        
        #finds the headlines and dates 
        list_headlines = findall('<title>(.*?)</title>',website)
        list_dates = findall('<pubDate>(.*?)</pubDate>',website)
       
        #inserts the top 3 headlines with its dates
        Message_box.insert(END,'1-' +str(list_headlines[2])+"\n" + str(list_dates[1]+"\n"))
        Message_box.insert(END,"\n"'2-' +str(list_headlines[3])+"\n" + str(list_dates[2]+"\n"))
        Message_box.insert(END,"\n"'3-' +str(list_headlines[4])+"\n" + str(list_dates[3]))

    #displays the headlines for Fox News
    elif var.get()== 2:
        website = download('https://moxie.foxnews.com/google-publisher/latest.xml')

        ##finds the headlines and dates 
        Main_headline = findall('<title>(.*?)</title>', website)
        timeline = findall('<pubDate>(.*?)</pubDate>',website)

        #inserts the top 3 headlines with its dates
        Message_box.insert(END,'1-' +str(Main_headline[2])+"\n" + str(timeline[1])+"\n")
        Message_box.insert(END,"\n"'2-' +str(Main_headline[3])+"\n" + str(timeline[2])+"\n")
        Message_box.insert(END,"\n"'3-' +str(Main_headline[4])+"\n" + str(timeline[3]))

    #displays the headlines for Nine News    
    else:
        website = download('https://www.9news.com/feeds/syndication/rss/news')

         #finds the headlines and dates  
        Headline = findall('<title>(.*?)</title>', website)
        pubdate = findall('<pubDate>(.*?)</pubDate>', website)

        #Inserts the top 3 headlines with its dates to the GUI
        Message_box.insert(END,'1-' +str(Headline[1])+"\n"+ str(pubdate[0])+"\n")
        Message_box.insert(END,"\n"'2-' +str(Headline[2])+"\n"+ str(pubdate[1])+"\n")
        Message_box.insert(END,"\n"'3-' +str(Headline[3])+"\n"+ str(pubdate[2]))


#HTML template that is used for the third button to output the html page
Html_template ="""
<html>
<head>
    <title>INTERNATIONAL BREAKING NEWS</title>
</head>
<h1> QUT NEWS(FAYAAZ)</h1>
<hr>
<h2> ***HEADLINE***</h2>
<img src="***IMAGE***" width="500" height="333">
<p>***DESCRIPTION***<p/>
<h3>***WEBSITENAME***</h3>
<p> ***DATE***<p/>
<hr>
<h2> ***HEADLINE2***</h2>
<img src="***IMAGE2***" width="500" height="333">
<p>***DESCRIPTION2***<p/>
<h3>***WEBSITENAME***</h3>
<p> ***DATE2***<p/>
<hr>
<h2> ***HEADLINE3***</h2>
<img src="***IMAGE3***" width="500" height="333">
<p>***DESCRIPTION3***<p/>
<h3>***WEBSITENAME***</h3>
<p> ***DATE3***<p/>


  
</body>
</html>
"""

#third button functionality
def printing():

    #printing the stories for NEWYORK TIMES
    if var.get() == 1: 
        website_name1 = 'THE NEWYORK TIMES (US News)'
        website = download('https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')

        #finds the headlines,dates,image and the descriptions of the headline news
        list_headlines = findall('<title>(.*?)</title>',website)
        list_dates = findall('<pubDate>(.*?)</pubDate>',website)
        list_image = findall('url="(.*?)"',website)
        list_description = findall('<description>(.*?)</description>',website)

        #finding the top 3 headline with its imagages and descriptions and dates
        headline_1 = str(list_headlines[2])
        headline_2 = str(list_headlines[3])
        headline_3 = str(list_headlines[4])
        date_1 = str(list_dates[1])
        date_2 = str(list_dates[2])
        date_3 = str(list_dates[3])
        image_1 = str(list_image[0])
        image_2 = str(list_image[1])
        image_3 = str(list_image[2])
        d_1 = str(list_description[1])
        d_2 = str(list_description[2])
        d_3 = str(list_description[3])

        #replace html code with details, so it can be viewed in an html page
        html_code = Html_template.replace('***HEADLINE***',headline_1)
        html_code = html_code.replace('***HEADLINE2***',headline_2)
        html_code = html_code.replace('***HEADLINE3***',headline_3)
        html_code = html_code.replace('***DATE***',date_1)
        html_code = html_code.replace('***DATE2***',date_2)
        html_code = html_code.replace('***DATE3***',date_3)
        html_code = html_code.replace('***IMAGE***',image_1)
        html_code = html_code.replace('***IMAGE2***',image_2)
        html_code = html_code.replace('***IMAGE3***',image_3)
        html_code = html_code.replace('***DESCRIPTION***',d_1)
        html_code = html_code.replace('***DESCRIPTION2***',d_2)
        html_code = html_code.replace('***DESCRIPTION3***',d_3)
        html_code = html_code.replace('***WEBSITENAME***',website_name1)

        #write html code to a unicode file
        html_file = open('newyorktimes.html','w',encoding='UTF-8')
        html_file.write(html_code)
        html_file.close()

        #printing the stories for FOX NEWS
    elif var.get() == 2: 
        website_name2 = 'FOX NEWS (EUROPE BREAKING NEWS)'
        website = download('https://moxie.foxnews.com/google-publisher/latest.xml')

        #finds the headlines,dates,image and the descriptions of the headline news
        list_headlines = findall('<title>(.*?)</title>',website)
        list_dates = findall('<pubDate>(.*?)</pubDate>',website)
        list_image = findall('url="(.*?)"',website)
        list_description = findall('<description>(.*?)</description>',website)

        #finding the top 3 headline with its imagages and descriptions and dates
        headline_1 = str(list_headlines[2])
        headline_2 = str(list_headlines[3])
        headline_3 = str(list_headlines[4])
        date_1 = str(list_dates[1])
        date_2 = str(list_dates[2])
        date_3 = str(list_dates[3])
        image_1 = str(list_image[0])
        image_2 = str(list_image[1])
        image_3 = str(list_image[2])
        d_1 = str(list_description[1])
        d_2 = str(list_description[2])
        d_3 = str(list_description[3])

        #replace html code with details
        html_code = Html_template.replace('***HEADLINE***',headline_1)
        html_code = html_code.replace('***HEADLINE2***',headline_2)
        html_code = html_code.replace('***HEADLINE3***',headline_3)
        html_code = html_code.replace('***DATE***',date_1)
        html_code = html_code.replace('***DATE2***',date_2)
        html_code = html_code.replace('***DATE3***',date_3)
        html_code = html_code.replace('***IMAGE***',image_1)
        html_code = html_code.replace('***IMAGE2***',image_2)
        html_code = html_code.replace('***IMAGE3***',image_3)
        html_code = html_code.replace('***DESCRIPTION***',d_1)
        html_code = html_code.replace('***DESCRIPTION2***',d_2)
        html_code = html_code.replace('***DESCRIPTION3***',d_3)
        html_code = html_code.replace('***WEBSITENAME***',website_name2)

        #write html code to a unicode file
        html_file = open('foxnews.html','w',encoding='UTF-8')
        html_file.write(html_code)
        html_file.close()

        #Printing the story for NINE NEWS
    else: 
        website_name2 = '9 NEWS (AUSTRALIAN BREAKING NEWS)'
        website = download('https://www.9news.com/feeds/syndication/rss/news')

        #finds the headlines,dates,image and the descriptions of the headline news
        list_headlines = findall('<title>(.*?)</title>',website)
        list_dates = findall('<pubDate>(.*?)</pubDate>',website)
        list_image = findall('url="(.*?)"',website)
        list_description = findall('<description>(.*?)</description>',website)

        #finding the top 3 headline with its imagages and descriptions and dates
        headline_1 = str(list_headlines[1])
        headline_2 = str(list_headlines[2])
        headline_3 = str(list_headlines[3])
        date_1 = str(list_dates[0])
        date_2 = str(list_dates[1])
        date_3 = str(list_dates[2])
        image_1 = str(list_image[0])
        image_2 = str(list_image[1])
        image_3 = str(list_image[2])
        d_1 = str(list_description[1])
        d_2 = str(list_description[2])
        d_3 = str(list_description[3])

        #replace html code with details
        html_code = Html_template.replace('***HEADLINE***',headline_1)
        html_code = html_code.replace('***HEADLINE2***',headline_2)
        html_code = html_code.replace('***HEADLINE3***',headline_3)
        html_code = html_code.replace('***DATE***',date_1)
        html_code = html_code.replace('***DATE2***',date_2)
        html_code = html_code.replace('***DATE3***',date_3)
        html_code = html_code.replace('***IMAGE***',image_1)
        html_code = html_code.replace('***IMAGE2***',image_2)
        html_code = html_code.replace('***IMAGE3***',image_3)
        html_code = html_code.replace('***DESCRIPTION***',d_1)
        html_code = html_code.replace('***DESCRIPTION2***',d_2)
        html_code = html_code.replace('***DESCRIPTION3***',d_3)
        html_code = html_code.replace('***WEBSITENAME***',website_name2)

        #write html code to a unicode file
        html_file = open('9NEWS.html','w',encoding='UTF-8')
        html_file.write(html_code)
        html_file.close()

#button 4 for saving the stories
def saving_data():

    #NEWS FOR NEWYORK TIMES
    if var.get() == 1: 
        
        #connecting to the database
        connection = connect(database='world_news.db')

        #creating a cursor
        world_db = connection.cursor()
        newsource = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
        website = download(newsource)

        #seperates the code from rss using regex
        list_headlines = findall('<title>(.*?)</title>',website)
        list_dates = findall('<pubDate>(.*?)</pubDate>',website)
        list_description = findall('<description>(.*?)</description>',website)

        #assigns headlines
        headline_1 =list_headlines[2]
        headline_2 = list_headlines[3]
        headline_3 = list_headlines[4]
        headlinelist =[list_headlines[2],list_headlines[3],list_headlines[4]]

        #assigns the date the news was published at
        date_1 = list_dates[1]
        date_2 = list_dates[2]
        date_3 = list_dates[3]
        datelist =[list_dates[1],list_dates[2],list_dates[3]]
        #description for the stories
        d_1 = list_description[1]
        d_2 = list_description[2]
        d_3 = list_description[3]
        descriptionlist=[list_description[1],list_description[2],list_description[3]]

        #sql query to insert the data into the database
        sql = ''' INSERT INTO interesting_stories(news_source,headline,dateline,story)
              VALUES(?,?,?,?) '''
        world_db.execute('DELETE FROM interesting_stories')

        #for loop used to loop through headlines,date, and description that will be saved in database
        for i in range(3):
            world_db.execute(sql,(newsource,headlinelist[i],datelist[i],descriptionlist[i]))
    
        
        connection.commit()

        world_db.close()
        connection.close()

    #fox news being saved in database
    elif var.get()==2:

        #connecting to the database
        connection = connect(database='world_news.db')

        #creating a cursor
        world_db = connection.cursor()
        newsource = 'https://moxie.foxnews.com/google-publisher/latest.xml'
        website = download(newsource)

        #seperates the code from rss using regex
        list_headlines = findall('<title>(.*?)</title>',website)
        list_dates = findall('<pubDate>(.*?)</pubDate>',website)
        list_description = findall('<description>(.*?)</description>',website)

        #assigns headlines
        headline_1 =list_headlines[2]
        headline_2 = list_headlines[3]
        headline_3 = list_headlines[4]
        headlinelist =[list_headlines[2],list_headlines[3],list_headlines[4]]

        #assigns the date the news was published at
        date_1 = list_dates[1]
        date_2 = list_dates[2]
        date_3 = list_dates[3]
        datelist =[list_dates[1],list_dates[2],list_dates[3]]

        #description for the stories
        d_1 = list_description[1]
        d_2 = list_description[2]
        d_3 = list_description[3]
        descriptionlist=[list_description[1],list_description[2],list_description[3]]

        #sql query to insert the data into the database
        sql = ''' INSERT INTO interesting_stories(news_source,headline,dateline,story)
              VALUES(?,?,?,?) '''
        world_db.execute('DELETE FROM interesting_stories')

         #for loop used to loop through headlines,date, and description that will be saved in database
        for i in range(3):
            world_db.execute(sql,(newsource,headlinelist[i],datelist[i],descriptionlist[i]))

        #saving the changes to the database
        connection.commit()
        
        #closing of the the database
        world_db.close()
        connection.close()

    #saving data of nine news to the the database
    else:
        #connecting to the database
        connection = connect(database='world_news.db')

        #creating a cursor
        world_db = connection.cursor()
        newsource = 'https://www.9news.com/feeds/syndication/rss/news'
        website = download(newsource)

        #seperates the code from rss using regex
        list_headlines = findall('<title>(.*?)</title>',website)
        list_dates = findall('<pubDate>(.*?)</pubDate>',website)
        list_description = findall('<description>(.*?)</description>',website)

        #assigns headlines
        headline_1 =list_headlines[1]
        headline_2 = list_headlines[2]
        headline_3 = list_headlines[3]
        headlinelist =[list_headlines[1],list_headlines[2],list_headlines[3]]

        #assigns the date the news was published at
        date_1 = list_dates[0]
        date_2 = list_dates[1]
        date_3 = list_dates[2]
        datelist =[list_dates[0],list_dates[1],list_dates[2]]

        #description for the stories
        d_1 = list_description[1]
        d_2 = list_description[2]
        d_3 = list_description[3]
        descriptionlist=[list_description[1],list_description[2],list_description[3]]

        #sql query to insert the data into the database
        sql = ''' INSERT INTO interesting_stories(news_source,headline,dateline,story)
              VALUES(?,?,?,?) '''
        world_db.execute('DELETE FROM interesting_stories')

         #for loop used to loop through headlines,date, and description that will be saved in database
        for i in range(3):
            world_db.execute(sql,(newsource,headlinelist[i],datelist[i],descriptionlist[i]))

        #saving the changes to the database
        connection.commit()
        
        #closing of the the database
        world_db.close()
        connection.close()

        

#Frame for the radio buttons that will be used
radiobuttons = Frame(my_window)
Find_stories = LabelFrame(radiobuttons, text='Find Stories', font=('Aharoni',24 ),fg='Green',)
Find_stories.grid(row=2, column=1,)
NY_times = Radiobutton(Find_stories, text = 'NEWYORK TIMES', font=('Aharoni', 18),variable =var,value=1, bd=1, relief= "solid",command=downloading_sources)
Fox_news = Radiobutton(Find_stories, text = 'Fox News',font=('Aharoni', 18),variable = var ,value=2, bd=1, relief= "solid" ,command=downloading_sources)
nine_News = Radiobutton(Find_stories, text='9 NEWS',font=('Aharoni', 18),variable = var,value=3, bd=1, relief= "solid",command=downloading_sources )
NY_times.grid (row=1, column=0,pady=18)
Fox_news.grid(row=2,column=0,pady=18,sticky= 'w')
nine_News.grid(row=3,column=0,pady=18,sticky= 'w')
radiobuttons.grid(row=2, column=0,padx=10,sticky='w',)

#Frame for the normal buttons that will be used to view the sources
Buttons = Frame(my_window)
view_stories = LabelFrame(Buttons, text='View The Stories', font=('Aharoni', 24 ),fg='Red',padx=10)
view_stories.grid(row=0, column=0,)
show_sources = Button(view_stories, text = 'Show Sources', activeforeground= 'red',font=('Aharoni', 18), bd=1, relief= "solid",state= DISABLED, command= sources)
show_sources.grid(row=1, column=0, pady=5,sticky= 'w')
show_headlines = Button(view_stories, text='Show Headlines',activeforeground= 'blue',font=('Aharoni', 18), bd=1, relief= "solid",state= DISABLED, command= radio_functionality)
show_headlines.grid(row=2, column=0,pady=5,sticky= 'w')
print_stories = Button(view_stories, text='Print Stories',activeforeground= 'green',font=('Aharoni', 18), bd=1, relief= "solid",state= DISABLED,command=printing)
print_stories.grid(row=3, column=0,pady=5,sticky= 'w')
save_stories = Button(view_stories, text='Save Stories',activeforeground= 'purple',font=('Aharoni', 18), bd=1, relief= "solid",state= DISABLED,command=saving_data)
save_stories.grid(row=4, column=0,pady=5,sticky= 'w')
Buttons.grid(row=2,column=0)

#Message box
Label_frame = LabelFrame(my_window,text='Messages', font=('Aharoni',24),fg='blue',)
Message_box = Text(Label_frame, width=35, height=14,bg='white')
Message_box.insert(END,'Please select a news source')
Label_frame.grid(row=2,column=0,sticky='e',)
Message_box.grid(row=0,column=0,)


my_window.mainloop()

