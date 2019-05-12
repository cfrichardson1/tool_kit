#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24

@author: chrisrichardson

PUPROSE:
    To  further streamline scrape techniques and improve overall skill,  logic, and  more!
    
    
FUTURE:
    1) Convert  all FN to OOP FNs
    2) Segment  Dependencies based on FN & Comment  Out
    3) 
    
"""
# In[ Dependencies ]
from bs4 import BeautifulSoup as bs
import codecs
from difflib import SequenceMatcher
import json
import pandas as pd
from pprint import pprint
import random
import re
from splinter import Browser
import time

# In[ FNS ]
 
# ******* MEAT N POTATOES *******
def html_parser(url = '', min_time = 5, max_time = 10):
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
    sleep_timer(min_time,max_time)
    
    browser.quit()
    
    return bs(html, 'html.parser')


def html_file_reader(file):
    '''
    '''

    return codecs.open(file, 'r')

def html_file_writer( var, file_name):
    '''
    Writes Beautiful Soup as file    
    '''
    with open(str(file_name), 'w') as file:
        file.write(str(var))


def match_ratio(string_a, string_b):
    return SequenceMatcher(None, string_a, string_b).ratio()


def sleep_timer(minimum, maximim):
    '''
    Random sleep timer within range of min max time args
    '''
    
    return time.sleep(random.randint( minimum, maximim))
    
    
def test():
    '''    
    Quick test to see if import of module is successfull!
    '''
    print('**'*20,'\nScrape Module up and running!\n','**'*20)
        

#def var_zipper( list1, list2, args*) for consequent lists

#def var_zipper( variable_list, content_list):
#    '''
#    Zips a list of variables with a list of contents.
#    
#    EX.
#    variable_list = [link1, link2]
#    content_list = ['link1.com', 'link2.com']
#    
#    var_zipper( variable_list, content_list)
#    '''
#    
#    for num, item in enumerate(content_list):
#        variable_list[num] = item

    
    
    
    
    
    
    
    

###########################
#
# SIMPLE SCRIPTS
#
###########################

#
## In[]
#
#list_ = []
#
#for num, item in enumerate(list_):
#    print(num)
#    print(item)
#    print( '*'*40, 'Item 1', '*'*40)
#    
## In[]
#
#list_ = [one_dollar_main, two_bills_main, three_bills_main, five_bills_main, ten_bills_main, twenty_bills_main, thirty_bills_main]
#
#for num, item in enumerate(list_):
#    scrape.website_catcher( var = item, file_name =  'scratcher', i = num)
    
















