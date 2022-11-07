# import libraries
import sys
import pandas as pd
from sqlalchemy import create_engine

#load data from csv files and merge to single pandas dataframe
def load_data(messages_filepath, categories_filepath):
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df_data = pd.merge(messages,categories,on='id')
    return df_data 

#Data pre-processing
def clean_data(df_data):
    # split categories into separate category columns
    categories = df_data['categories'].str.split(pat=';', expand=True)

    # select the first row of the categories dataframe
    row = categories.iloc[0,:]
        
    # use this row to extract a list of new column names for categories
    category_colnames = row.apply(lambda x: x[:-2])
    
    # rename the columns of `categories`      
    categories.columns = category_colnames

    # Convert category values to just numbers 0 or 1
    for column in categories:
         # set each value to be the last character of the string
         categories[column] = categories[column].str[-1] 
        
         # convert column from string to numeric
         categories[column] = categories[column].astype(int) 
        
         # "related" column has value 0,1,2 and we need only 0 & 1 hence replacing 2 with 1
         categories.related.replace(2,1,inplace=True) 
    
    # Replace categories column in df with new category columns
    # drop the original categories column from `df_data`
    df_data.drop('categories' , axis = 1 , inplace = True) 
    
    # concatenate the original dataframe with the new `categories` dataframe
    df_data = pd.concat([df_data,categories], join='inner', axis=1) 
    
    # drop duplicates
    df_data.drop_duplicates(inplace = True) 
    
    return df_data


#save data to SQLite database function
def save_data(df_data, database_filename):
    engine = create_engine('sqlite:///' + database_filename)
    df_data.to_sql('DisasterResponse', engine, index=False, if_exists='replace')

    
def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df_data = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df_data = clean_data(df_data)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df_data, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()