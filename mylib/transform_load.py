'''Takes a csv and loads it as a db'''

import csv
import os
import sqlite3

PATH = 'data/bad-drivers.csv'

def trans_load(path = PATH):
    '''Takes the csv file and transforms it into a d in SQLite3'''
    print(os.getcwd()) 
    payload = csv.reader(open(path, newline=''), delimiter = ',')
    connection = sqlite3.connect('badDrivers.db')
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS badDrivers')
    cursor.execute('CREATE TABLE badDrivers (state, drivers_count, speeding_percent, alc_percent, no_distraction_percent, no_prev_percent, car_insurance, insurance_losses)')

    cursor.executemany("INSERT INTO badDrivers VALUES (?, ?, ?, ?, ?, ?, ?, ?)", payload)
    connection.commit()
    connection.close()
    return 'badDrivers.db'
