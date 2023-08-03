from statistics import mean, mode, median
from collections import Counter
import psycopg2

# List of unique colours
colours = ["GREEN", "YELLOW", "BROWN", "BLUE", "BLEW", "PINK", "ORANGE", "CREAM", "RED", "WHITE", "ARSH", "BLACK"]

monday = ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE",\
     "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"]
     
tuesday = ["ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE",\
     "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"]

wednesday = ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED",\
     "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"]

thursday = ["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM",\
     "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"]

friday = ["GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED",\
     "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"]

# The days and corresponding colours list
days_dict = {"monday": monday, "tuesday": tuesday, "wednesday": wednesday, "thurday": thursday, "friday": friday}

# A list to hold all colours throughout the week
all_colours = list()

# Combine the daily colour lists
for lst in days_dict.values():
    all_colours.extend(lst)

def get_mean(colour_list):
    """
    Convert list of colours to indexes and find the mean,
    then return the colour that corresponds to the mean.
    """
    colour_num_list = list(map(lambda colour: colours.index(colour), colour_list)) # convert the colours to numbers
    index = round(mean(colour_num_list)) # round the mean to the nearest integer
    return colours[index] # return the mean colour

mean_colour = get_mean(all_colours)
most_worn_colour = mode(all_colours)
median_colour = median(all_colours)
frequencies = Counter(all_colours)

red_probability = frequencies["RED"] / len(all_colours)

print("Mean: ", mean_colour)
print("Mode: ", most_worn_colour)
print("median: ", median_colour)
print("Probability of red: ", red_probability)

def save_to_database():

    DB_NAME = "dbname"
    DB_USER = "dbuname"
    DB_PASS = "dbpass"
    DB_HOST = "<dburi>"
    DB_PORT = "<dbport"

    try:
        conn = psycopg2.connect(database=DB_NAME,
                                user=DB_USER,
                                password=DB_PASS,
                                host=DB_HOST,
                                port=DB_PORT)
        print("Database connected successfully")
    except:
        print("Database not connected successfully")

    cur = conn.cursor()  # Create a cursor
    
    # Create table
    cur.execute("""
        CREATE TABLE Colours
        (
            ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            Colour TEXT NOT NULL,
            Frequency INT NOT NULL
        )
        """)
    
    for colour, freq in frequencies.items():
        cur.execute("""
            INSERT INTO Colours (Colour, Frequency) VALUES (%s, %s)
            """, (colour, freq))

    # commit the changes
    conn.commit()
    conn.close()


save_to_database()