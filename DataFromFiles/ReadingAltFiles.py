#!/usr/bin/env python3
import pandas

df1 = pandas.read_csv("supermarket_data/supermarkets.csv")
# to read a csv file use the read_csv method

df2 = pandas.read_json('supermarket_data/supermarkets.json')
# to read a json file use the read_json method

df3 = pandas.read_excel('supermarket_data/supermarkets.xlsx')
# to read excel files use the read_excel method

df4 = pandas.read_csv('supermarket_data/supermarkets-commas.txt')
# for text files you can use the read_csv method as well

df5 = pandas.read_csv('supermarket_data/supermarkets-semi-colons.txt', sep=';')
# for text files that have columns seperated by anything other
# than a comma you must specify that in the method call using the parameter sep
