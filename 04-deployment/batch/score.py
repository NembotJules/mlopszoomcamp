
#import pickle
#import os
import mlflow
import uuid
import sys
from prefect import task, flow, get_run_logger
from prefect.context import get_run_context
from datetime import datetime
from dateutil.relativedelta import relativedelta



import pandas as pd


def generate_uuids(n): 
    ride_ids = []
    for i in range(n): 
        ride_ids.append(str(uuid.uuid4()))
        
    return ride_ids


def read_dataframe(filename: str): 

    df = pd.read_parquet(filename)
    df['duration'] = df.lpep_dropoff_datetime - df.lpep_pickup_datetime
    df.duration = df.duration.dt.total_seconds() / 60
    df = df[(df.duration >= 1) & (df.duration <= 60)]

    df['ride_id'] = generate_uuids(len(df))
    return df


def prepare_dictionaries(df: pd.DataFrame): 

    categorical = ['PULocationID', 'DOLocationID']
    df[categorical] = df[categorical].astype(str)
    df['PU_DO'] = df['PULocationID'] + '_' + df['DOLocationID']
    categorical = ['PU_DO']
    numerical = ['trip_distance']
    dicts = df[categorical + numerical].to_dict(orient='records')
    return dicts



def load_model(run_id): 
    logged_model = f's3://mlflow-model/1/{run_id}/artifacts/model'
    model = mlflow.pyfunc.load_model(logged_model)
    return model


def save_result(df, output_file, y_pred, run_id): 

    print(f"Saving the result to {output_file}...")

    df_result = pd.DataFrame()
    df_result['ride_id'] = df['ride_id']
    df_result['lpep_pickup_datetime'] = df['lpep_pickup_datetime']
    df_result['PULocationID'] = df['PULocationID']
    df_result['DOLocationID'] = df['DOLocationID']
    df_result['actual_duration'] = df['duration']
    df_result['predicted_duration'] = y_pred
    df_result['diff'] = df_result['actual_duration'] - df_result['predicted_duration']
    df_result['model_version'] = run_id

    df_result.to_parquet(output_file, index=False)
    

    
@task
def apply_model(input_file, run_id, output_file): 

    logger = get_run_logger()

    logger.info(f"Reading the data from the {input_file}...")

    df = read_dataframe(input_file)
    dicts = prepare_dictionaries(df)

    logger.info(f"Loading the model with RUN_ID={run_id}...")

    model = load_model(run_id)

    logger.info("Applying the model...")
    y_pred = model.predict(dicts)

    logger.info("Saving the result to output file")
    save_result(df, output_file, y_pred, run_id)
    return output_file



def get_paths(run_date): 
    
    prev_month = run_date - relativedelta(months=1)
    year = prev_month.year
    month = prev_month.month
    input_file = f'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_{year:04d}-{month:02d}.parquet'
    output_file = f's3://zoomcamp-mlops-2024/chap5-score-result/green_tripdata_pred_{year:04d}-{month:02d}.parquet'
   # RUN_ID = '0f06d2686fe64fda9f835fcd7639d773'

    return input_file, output_file




@flow
def ride_duration_prediction(run_id: str, run_date: datetime = None): 

    if run_date is None: 
        ctx = get_run_context()
        run_date = ctx.flow_run.expected_start_time # The time for which the flow is scheduled

    input_file, output_file = get_paths(run_date)

    apply_model(input_file=input_file, output_file=output_file, run_id= run_id)



def run(year = 2024, month = 2, run_id = '0f06d2686fe64fda9f835fcd7639d773'): 

  #  year =  int(sys.argv[1])
   # month = int(sys.argv[2])
   # run_id = sys.argv[3]     #'0f06d2686fe64fda9f835fcd7639d773'
    
    ride_duration_prediction(run_id=run_id, run_date=datetime(year = year, month = month, day = 1))


if __name__=="__main__": 
    run()


