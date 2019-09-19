#!/usr/local/bin/python3

from urllib.request import urlopen
from os import path

def parse_leclerc(url):
    product_url = []
    page = urlopen(url).read().decode('utf-8')
    split = page.split("\"")
    for i  in range(len(split)):
        if split[i] == 'sUrlPageProduit':
              product_url.append(split[i + 2])
    return product_url

def write_in_file(product):   
    Product_Exist = path.exists("product.txt")
    file = open("product.txt", "a")
    for i in range(len(product)):
        file.write(product[i])
        file.write('\n')

def read_file(category_url):
    split = []
    file = open(category_url, "r").read()
    return file.split("\n")

def main():
    if not(path.exists("category.txt")):
        print("Need category.txt")
        exit()
    category_url = read_file("category.txt")
    for i in range(len(category_url)):
        product = parse_leclerc(category_url[i])
        write_in_file(product)

if __name__ == "__main__":
    main()