#from dateutil.parser import parse
import datetime
import csv
from typing import Counter

def load_csv():
    with open('netflixoriginals.csv', 'r') as file:
        reader = csv.reader(file)
        year_list=[]
        genre_list=[]       
        for i in reader:

            premier_data=i[2]            
            year_p=premier_data[-4:] 
            genre_data=i[1]           

            genre_list.append(genre_data)
            year_list.append(year_p)
            
    return year_list,genre_list
          
year,genre=load_csv()  
#print(year,genre)


def filter_genre_year(year,genre):
    #load_csv()
    for i in year:
        #print(i)
        if i=='2020': 
            genre_count=[ [l, genre.count(l)] for l in set(genre)] 
        
            #print ([ [l, genre.count(l)] for l in set(genre)]) 
    return genre_count

    
        
       
filter_genre_year(year,genre)
print(filter_genre_year(year,genre))

       
        

    

