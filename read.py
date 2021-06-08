import csv
genere=[]
def load_csv():
    with open('netflixoriginals.csv', 'r') as file:

        reader = csv.reader(file)

    
        for i in reader:
            genere.append(i[1])
            print(genere)
            

            

           

def filter_genre_year(genere):
    load_csv()
    genere_count=
    
	#return genre_count
filter_genre_year(genere)

