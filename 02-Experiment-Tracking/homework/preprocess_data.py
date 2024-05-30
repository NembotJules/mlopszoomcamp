import os 
import pickle
import pandas as pd

from sklearn.feature_extraction import DictVectorizer


def dump_pickle(obj, filename: str):
    with open(filename, "wb") as f_out:
        return pickle.dump(obj, f_out)


def read_dataframe(filename: str):
    df = pd.read_parquet(filename)

    df['duration'] = df['lpep_dropoff_datetime'] - df['lpep_pickup_datetime']
    df['duration'] = df.duration.apply(lambda td: td.total_seconds() / 60)
    df = df[(df.duration >= 1) & (df.duration <= 60)]

    categorical = ['PULocationID', 'DOLocationID']
    df[categorical] = df[categorical].astype(str)

    return df 

def preprocess(df: pd.DataFrame, dv: DictVectorizer, fit_dv: bool = False):
    df['PU_DO'] = df['PULocationID'] + '_' + df['DOLocationID']
    categorical = ['PU_DO']
    numerical = ['trip_distance']
    dicts = df[categorical + numerical].to_dict(orient = 'records')
    if fit_dv:
        X = dv.fit_transform(dicts)
    else:
        X = dv.transform(dicts)
    return X,dv


df_train = read_dataframe("/home/maxtheking/mlopszoomcamp/02-Experiment-Tracking/homework/taxi_data/green_tripdata_2023-01.parquet")
df_val = read_dataframe("/home/maxtheking/mlopszoomcamp/02-Experiment-Tracking/homework/taxi_data/green_tripdata_2023-02.parquet")
df_test = read_dataframe("/home/maxtheking/mlopszoomcamp/02-Experiment-Tracking/homework/taxi_data/green_tripdata_2023-03.parquet") 

 # Extract the target
target = 'duration'
y_train = df_train[target].values
y_val =   df_val[target].values 
y_test =  df_test[target].values

    # Fit the DictVectorizer and preprocess data
dv = DictVectorizer()
X_train, dv = preprocess(df_train, dv, fit_dv = True)
X_val, _ = preprocess(df_val, dv, fit_dv = False)
X_test, _ = preprocess(df_test, dv, fit_dv = False)

 # Save DictVectorizer and datasets
dest_path = "/home/maxtheking/mlopszoomcamp/02-Experiment-Tracking/homework/taxi_data/output"
print(f"Saving DictVectorizer to {os.path.join(dest_path, 'dv.pkl')}")
dump_pickle(dv, os.path.join(dest_path, "dv.pkl"))
print(f"Saving training data to {os.path.join(dest_path, 'train.pkl')}")
dump_pickle((X_train, y_train), os.path.join(dest_path, "train.pkl"))
print(f"Saving validation data to {os.path.join(dest_path, 'val.pkl')}")
dump_pickle((X_val, y_val), os.path.join(dest_path, "val.pkl"))
print(f"Saving test data to {os.path.join(dest_path, 'test.pkl')}")
dump_pickle((X_test, y_test), os.path.join(dest_path, "test.pkl"))






