import score
from prefect import flow
from datetime import datetime
from dateutil.relativedelta import relativedelta


@flow
def ride_duration_prediction_backfill(): 

    start_date = datetime(year=2023, month=8, day=1)
    end_date = datetime(year = 2024, month=7, day = 1)

    d = start_date

    while d <= end_date: 
        score.ride_duration_prediction(
            run_id = '0f06d2686fe64fda9f835fcd7639d773', 
            run_date=d
        )

        d = d + relativedelta(months=1)



if __name__=="__main__": 
    ride_duration_prediction_backfill()