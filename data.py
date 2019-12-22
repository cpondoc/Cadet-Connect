import csv
import requests
import os.path
from club import *

def get_data():
    clubs = []
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "data/AugmentedClubs20192020.csv")
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                club = Club()
                club.id = str(line_count)
                club.name = row[1]
                club.purpose = row[2]
                club.join = row[3]
                club.adviser = row[4]
                club.meet = row[5]
                club.frequently = row[6]
                club.where = row[7]
                club.how = row[8]
                club.email = row[9]
                clubs.append(club)
                line_count += 1
        print(f'Processed ' + str(len(clubs)) + ' lines.')
    return clubs