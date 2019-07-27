# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 00:27:58 2019

@author: crich
"""
import os
import pandas as pd
import re

os.getcwd()
# In[]

df = pd.read_csv(r'C:\Users\crich\Desktop\gDrive\BootCamp\DataViz-Lesson-Plans\01-Lesson-Plans\09-SQL\3\Activities\02-Stu_Data_Normalization\Resources\pets.csv')


# In[]

df.iloc[2,2] = 'Spinkles, Yoyo, Chocalte, Koojo, Chicken'

# In[]

df.iloc[:,2].str.split(', ', expand =True).shape[1]

# In[]



# In[ Beta ]

class standardized_df:
    
    def __init__(self, df = None):
        self.df = df
        self.df_copy = df.copy()
        
    def splitter(self, primary_key = None):
        
        for column in self.df.columns:
            # attempt to split column based on 
            
            column_str_split = 0                 
            split_df_column_count = 0
            try:
                column_str_split = df[column].str.split(', ',expand=True)
                
                split_df_column_count = column_str_split.shape[1]

            except:
                pass
            
            if split_df_column_count:
                # loops over old and new columns, insuring there is nothing longer than len 2               
                split_column_names = []
                for num in range(split_df_column_count):
                    split_column_names.append((column + ' ' + str(num)))

#                column_str_split.column =

#                column_str_split[primary_key] = df[primary_key].copy()

                # Attempting to merge split df back to og_df
#                self.df_copy[split_column_names] = self.column_str_split
                
#                self.df_copy[split_column_names]

        return column_str_split
# In[ Dev ]

class standardized_df:
    
    def __init__(self, df = None):
        self.df = df
        self.df_copy = df.copy()
        
    def splitter(self, primary_key = None):
        
        dfs = []
        for column in self.df.columns:
            # attempt to split column based on 
            dfs.append(column)

            column_str_split = 0                 
            split_df_column_count = 0
            try:
                column_str_split = df[column].str.split(', ',expand=True)
                
                split_df_column_count = column_str_split.shape[1]

            except:
                pass
            
            
            if split_df_column_count > 1:
                # loops over old and new columns, insuring there is nothing longer than len 2               
                split_column_names = []
                for num in range(split_df_column_count):
                    split_column_names.append((column + '_' + str(num)))

                column_str_split.columns = split_column_names
#            else:
#                column_str_split.columns = column
#                dfs.append(column)
            
#            column_str_split[['ID','Owner']] = df[['ID','Owner']].copy()

            dfs.append(column_str_split)
            
# after building df of columns
#            column_str_split[primary_key] = df[primary_key].copy()
                
            # Attempting to merge split df back to og_df
#                self.df_copy[split_column_names] = self.column_str_split
            
#                self.df_copy[split_column_names]

        return column_str_split

test = standardized_df(df)
dfs_build = test.splitter(['ID','Owner'])

# In[ Dev ]

class standardized_df:
    
    def __init__(self, df = None):
        self.df = df
        self.df_copy = df.copy()
        
    def splitter(self, primary_key = None):
        
        dfs = []
        for column in self.df.columns:
            # attempt to split column based on 
            dfs.append(column)

            column_str_split = 0                 
            split_df_column_count = 0
            try:
                column_str_split = df[column].str.split(', ',expand=True)
                
                split_df_column_count = column_str_split.shape[1]

            except:
                pass
            
            
            if split_df_column_count > 1:
                # loops over old and new columns, insuring there is nothing longer than len 2               
                split_column_names = []
                for num in range(split_df_column_count):
                    split_column_names.append((column + '_' + str(num)))

                column_str_split.columns = split_column_names
#            else:
#                column_str_split.columns = column
#                dfs.append(column)


            
            
#            column_str_split[['ID','Owner']] = df[['ID','Owner']].copy()

            dfs.append(column_str_split)
            

# after building df of columns
#            column_str_split[primary_key] = df[primary_key].copy()
                

            # Attempting to merge split df back to og_df
#                self.df_copy[split_column_names] = self.column_str_split
            
#                self.df_copy[split_column_names]


        return column_str_split

    def test(self, primary_key = None):
        
        dfs = []
        for column in self.df.columns:
            # attempt to split column based on 
            dfs.append(column)

            column_str_split = 0                 
            split_df_column_count = 0
            try:
                column_str_split = df[column].str.split(', ',expand=True)
                
                split_df_column_count = column_str_split.shape[1]

            except:
                pass
            
            
            if split_df_column_count > 1:
                # loops over old and new columns, insuring there is nothing longer than len 2               
                split_column_names = []
                for num in range(split_df_column_count):
                    split_column_names.append((column + '_' + str(num)))

                column_str_split.columns = split_column_names
#            else:
#                column_str_split.columns = column
#                dfs.append(column)

#            column_str_split[['ID','Owner']] = df[['ID','Owner']].copy()

            dfs.append(column_str_split)
            
# after building df of columns
#            column_str_split[primary_key] = df[primary_key].copy()
                

            # Attempting to merge split df back to og_df
#                self.df_copy[split_column_names] = self.column_str_split
            
#                self.df_copy[split_column_names]


        return column_str_split


test = standardized_df(df)
dfs_splitter = test.splitter(['ID','Owner'])
dfs_test = test.test(['ID','Owner'])


# In[ NOTES ]

1) column appears to get mutated after the first line of the for loop

# In[]

test = standardized_df(df)
test.splitter()


# In[]

for column in df.columns:
    print(column)
# In[]

#df = pd.read_csv(r'C:\Users\crich\Desktop\gDrive\BootCamp\DataViz-Lesson-Plans\01-Lesson-Plans\09-SQL\3\Activities\02-Stu_Data_Normalization\Resources\pets.csv')

# duplciate original df for mutation
normy_df = df.copy()

# Remove comma and space from columns with multiple entries
normy_df[['Pet One', 'Pet Two']] = df['Pet'].str.split(', ',expand=True)
normy_df[['Type One', 'Type Two']] = df['Type'].str.split(', ',expand=True)
normy_df[['Service One', 'Service Two']] = df['Service'].str.split(', ',expand=True)

# ------ append split columns into lists that will be appended to original df ------
id_ = []
owner = []
pet = []
type_ = []
service = []
for index, row in normy_df.iterrows():
    if row['Pet Two'] != None:
        # append owner twice to pair with pet
        i = 0
        while i != 2:
            i += 1
            id_.append(row['ID'])
            owner.append(row['Owner'])
        
        type_.append(row['Type One'])
        type_.append(row['Type One'])

        pet.append(row['Pet One'])
        pet.append(row['Pet Two'])
        
        service.append(row['Service One'])
        service.append(row['Service Two'])

df_2nd = pd.DataFrame({'ID': id_,
          'Owner':owner,
          'Pet':pet,
          'Type':type_,
          'Service':service
          })

keys = df_2nd.iloc[:,0].unique()

# Remove rows that are standardized via 
for key in keys:
    df = df[df['ID'] != key]

df = df.append(df_2nd)
df.sort_values(by = ['ID'], inplace = True)

del(normy_df, id_, owner, pet, type_, service, i , index, key, keys, df_2nd, row)


# In[]





# In[]





# In[]




# In[]




# In[]








# In[]





# In[]




# In[]




# In[]


