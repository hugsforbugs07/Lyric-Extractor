# Import modules
from tkinter import *
from lyrics_extractor import SongLyrics

# User-defined function to get lyrics
def get_lyrics():
    extract_lyrics = SongLyrics("AIzaSyCOsPyLDMvOQW2mxBU8bqxYlGCimmjVUzY", "https://cse..google.com/cse.js?cx=85950c12085d64270")
    song_name = str(e.get())
    temp = extract_lyrics.get_lyrics(song_name)
    res = temp['lyrics']
    result.set(res)

# Create the Tkinter window
master = Tk()
master.configure(bg='light grey')
master.title("Song Lyrics Extractor")

# Variable to store the result
result = StringVar()

# Labels and entry field
Label(master, text="Enter Song Name:", bg="light grey").grid(row=0, sticky=W)
Label(master, text="Result:", bg="light grey").grid(row=3, sticky=W)

e = Entry(master, width=50)
e.grid(row=0, column=1)

Label(master, textvariable=result, bg="light grey").grid(row=3, column=1, sticky=W)

# Button to fetch lyrics
b = Button(master, text="Show Lyrics", command=get_lyrics, bg="Blue")
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

# Run the GUI application
mainloop()