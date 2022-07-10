# Quick script to scrape Ryan Day's coaching performances (by game)
# https://www.sports-reference.com/cfb/schools/ohio-state/2018-schedule.html
# Want to dump to a csv file to ingest later

import pandas as pd
# import numpy as np
import os

def main():

    dfs = []
    years_coaching = range(2019, 2022)

    # Scraping football-reference schedules for each 
    for y in years_coaching:
        url = f"https://www.sports-reference.com/cfb/schools/ohio-state/{y}-schedule.html"

        dat = pd.read_html(url, displayed_only=False)[-1]
        print(dat.head(), len(dat))


        dfs.append(dat)
        print('---------------------------------------')

    df = pd.concat(dfs)

    print(df)
    data_path = os.path.join("..", "data", "results-tOSU.csv")

    df.to_csv(data_path, index=False)

    return df




if __name__ == "__main__":
    main()