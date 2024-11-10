'''Extracts a dataset'''
import requests

URL = 'https://raw.githubusercontent.com/fivethirtyeight/election-results/refs/heads/main/races.csv'
FILE_PATH = 'data/election-results.csv'

def extract(url = URL, path = FILE_PATH):
    '''Extracts a dataset based on URL and saves it to the path'''
    with requests.get(url) as r:
        with open(path, 'wb') as f:
            f.write(r.content)
    return path

if __name__ == '__main__':
    extract()