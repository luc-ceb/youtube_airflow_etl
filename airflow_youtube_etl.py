import pandas as pd
import json
from datetime import datetime
import s3fs
from googleapiclient .discovery import build

def run_youtube_etl():
    example1 = "api_credentials.txt" #api_key
    file1 = open(example1, "r")
    api_key = file1.read() #save as a variable


    youtube_resource= build('youtube','v3',developerKey=api_key)  
                                                                
    
    request2=youtube_resource.channels().list(
        part='statistics',
        forUsername= 'ElonMuskZone'
    )
    response2=request2.execute()

    dictionary = response2['items'][0]['statistics']

    df = pd.DataFrame(dictionary , index=['1'])

    df .to_csv("s3://name-bucket/elon_musk_data.csv")

