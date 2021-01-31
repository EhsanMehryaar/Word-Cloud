import pandas as pd
import sqlite3
import regex as re
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def df_maker(name):
    ''' 
        Utility function that imports the data and creates dataframe and deletes duplicate entries. 
    '''
    # Read the CSV file
    df = pd.read_csv(name)
    df['spam'] = df['spam'].astype(int)

    # Remove duplicates
    df = df.drop_duplicates()

    df = df.reset_index(inplace = False)[['text','spam']]
    return df

def clean (df):
    ''' 
        Utility function changes all the letter to lower case, removes punctuation, tags, digits and 
        special characters. 
    '''
    cleaned = []
    for w in range(len(df.text)):
        #Lower case
        temp = df['text'][w].lower()
    
        #Delete punctuation
        temp = re.sub('[^a-zA-Z]', ' ', temp)
    
        #Delete tags
        temp = re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",temp)
    
        #Delete digits and special charachters
        temp = re.sub("(\\d|\\W)+"," ",temp)
    
        cleaned.append(temp)

    df['text'] = cleaned
    return df

def plot_cloud(df):
    ''' 
        Utility function that plots the word cloud. 
    '''

    #list of proposed stop words
    stop_words = ['wa','is','you','your','and', 'the', 'to', 'from', 'or', 'I', 'for', 'do', 'get', 'not', 'here', 'in', 'im', 'have', 'on', 're', 'new', 'subject']

    #plot the word cloud
    wordcloud = WordCloud(width = 800, height = 800, background_color = 'black', stopwords = stop_words, max_words = 1000, min_font_size = 20).generate(str(df['text']))
    plt.figure(figsize = (10,10), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()



def main(): 
    # Creating dataframe
    df = df_maker('emails.csv')

    #Cleaning data
    df = clean(df)

    #plotting the word cloud
    plot_cloud(df)



if __name__ == "__main__": 
    # calling main function 
    main()