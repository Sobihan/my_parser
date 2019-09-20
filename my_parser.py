#!/usr/local/bin/python3

from urllib.request import urlopen
from os import path
import time

def parse_leclerc(url):
    product_url = []
    page = urlopen(url)
    if page.code != 200:
        print(page.code, ":", url)
    split = page.read().decode('utf-8').split("\"")
    for i  in range(len(split)):
        if split[i] == 'sUrlPageProduit':
              product_url.append(split[i + 2])
    return product_url

def write_in_file(product):   
    file = open("product.txt", "a")
    for i in range(len(product)):
        file.write(product[i])
        file.write('\n')

def read_file(category_url):
    file = open(category_url, "r").read()
    return file.split("\n")

def main():
    if not(path.exists("category.txt")):
        print("Need category.txt")
        exit()
    category_url = read_file("category.txt")
    for i in range(len(category_url)):
        if 'https://fd11-courses.leclercdrive.fr/' in category_url[i]:
                print("Category URL:", category_url[i])
                product = parse_leclerc(category_url[i])
                write_in_file(product)
                time.sleep(3)
        else:
                print("Not a leclerc url:", category_url[i])

if __name__ == "__main__":
    main()