#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 21:17:54 2019

@author: chrisrichardson
"""
# In[ Dependencies ]
from bs4 import BeautifulSoup as bs
from difflib import SequenceMatcher
import json
import pandas as pd
from pprint import pprint
import random
import re
from splinter import Browser
import time

# In[ FNS ]

def match_ratio(string_a, string_b):
    return SequenceMatcher(None, string_a, string_b).ratio()
 
# ******* MEAT N POTATOES *******
def html_parser(url):
    '''
    Returns html in beautiful soup format.
    
    The following will find all "meta" tags
    meta_data = soup_exp.find_all('meta')
    
    start = re.search(r'{"config', tag_script).start()
    end = re.search(r'};', tag_script).end() - 1 # minus 1 removes semicolon from JSON
    '''
    
    browser = Browser('chrome') # initialize browser
    
    browser.visit(url)     # visit link
    
    html = browser.html
    sleep_timer(5,10)
    
    browser.quit()
    
    return bs(html, 'html.parser') 


def sleep_timer(minimum, maximim):
    '''
    
    Random sleep timer within range of min max time args
    
    '''
    
    time.sleep(random.randint( minimum, maximim))
    
    
def test():
    '''    
    Quick test to see if import of module is successfull!
    '''
    print('**'*20,'\nScrape Module up and running!\n','**'*20)
    
def website_catcher( var, file_name, i):
    with open(str('html/' + file_name + str(i)+'.html'), 'w') as file:
        file.write(str(var))

# SIMPLE SCRIPTS

'''
# In[]

list_ = []

for num, item in enumerate(list_):
    print(num)
    print(item)
    print( '*'*40, 'Item 1', '*'*40)
    
# In[]

list_ = [one_dollar_main, two_bills_main, three_bills_main, five_bills_main, ten_bills_main, twenty_bills_main, thirty_bills_main]

for num, item in enumerate(list_):
    scrape.website_catcher( var = item, file_name =  'scratcher', i = num)
    

'''















