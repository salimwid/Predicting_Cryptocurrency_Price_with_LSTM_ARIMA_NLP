import numpy as np
import pandas as pd
import re
import requests
import concurrent.futures
import multiprocessing as mp
import pickle


from bs4 import BeautifulSoup

def get_date_newsbtc(url):
    date = re.search(r'([0-9]{4}\/[0-9]{2}\/[0-9]{2})', url).group(1).replace('/', '-')
    
    return date

def get_date_others(source, url):
    page = requests.get(url).text
    html_parser = BeautifulSoup(page, 'html.parser')
    
    if source == 'cointelegraph':
        #Cointelegraph
        date = html_parser.find(class_ = 'post-meta__publish-date')
        if date is not None:
            date = date.time['datetime']
        
        else:
            print(url)
    
    else:
        #Coindesk
        date = html_parser.find('meta', property = 'article:published_time')
        if date is not None:
            date = date['value'].split('T')[0]
        
        else:
            print(url)

    return date

def run_parallel(process_num, new_df):
    print('running process')
    count = 0
    all_date = {}
    for index, row in new_df.iterrows():
        try:
            if count % 500 == 0:
                print('ai ai ai 500', count, 'process num', process_num)
            count += 1
            if new_df['source'][index] == 'newsbtc':
                date = get_date_newsbtc(new_df['url'][index])
            
            else:
                date = get_date_others(new_df['source'][index], new_df['url'][index])

            all_date[index] = date
        except Exception as ex:
            print('error on', process_num, new_df['url'][index], ex)

    print('FINISHED process num', process_num)
    return all_date

def run():
    df = pd.read_csv('crypto_news_parsed_2013-2018_40k.csv')

    filler = ['www', 'com', 'net']
    clean_url = []

    for index, url in enumerate(df['url']):
        main_url = re.search(r'^.*:\/\/([\w.]+)/.*', url).group(1)
        main_url = main_url.split('.')
        
        for clean in main_url:
            
            if clean not in filler:
                clean_url.append(clean)

    df = df.rename(columns = {'source':'category'})
    #df.drop(['url', 'html'], inplace=True, axis=1)
    df['source'] = clean_url

    new_df = df.loc[~df['source'].isin(['ccn', 'forklog'])]
    new_df.reset_index(inplace = True)
    new_df.drop(columns='index', inplace = True)

    all_date = {}
    new_df_rows = new_df.shape[0]
    processes = 20
    chunk_size = int((new_df_rows)/processes)
    print('we are here')
    with concurrent.futures.ProcessPoolExecutor(max_workers=processes) as executor:
        futures = []
        row_start = 0
        process_count = 0
        while row_start < new_df_rows:
            row_end = min(row_start + chunk_size, new_df_rows)
            futures.append(
                executor.submit(run_parallel, process_count, new_df.iloc[row_start:row_end,:])
            )
            row_start += chunk_size
            process_count += 1

        for future in concurrent.futures.as_completed(futures):
            try:
                all_date.update(future.result())
            except Exception as ex:
                print('error', ex)

    print(all_date)
    with open('index-date.pickle', 'wb') as handle:
        pickle.dump(all_date, handle, protocol=pickle.HIGHEST_PROTOCOL)

if __name__ == "__main__":
    run()