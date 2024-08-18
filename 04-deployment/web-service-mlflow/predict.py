import pickle
import mlflow

import os
os.environ["AWS_ACCESS_KEY_ID"] = "AKIA6ODU2FARFDCJJW5W"
os.environ["AWS_SECRET_ACCESS_KEY"] = "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"
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"


from flask import Flask, request, jsonify

import mlflow

RUN_ID = '0f06d2686fe64fda9f835fcd7639d773'
#logged_model = f'runs:/{RUN_ID}/model'
logged_model = f's3://mlflow-model/1/{RUN_ID}/artifacts/model'

# Load model as a PyFuncModel.
model = mlflow.pyfunc.load_model(logged_model)


def prepare_features(ride): 

    features = {}
    features['PU_DO'] = '%s_%s' % (ride['PULocationID'], ride['DOLocationID'])
    features['trip_distance'] = ride['trip_distance']
    return features



def predict(features): 

    preds = model.predict(features)
    return float(preds[0])

app = Flask('duration-prediction')

@app.route('/predict', methods = ['POST'])

def predict_endpoint(): 

    ride = request.get_json()
    features = prepare_features(ride)

    pred = predict(features)

    result = {
        'duration': pred,
        'model_version': RUN_ID
    }

    return jsonify(result)

if __name__ == "__main__": 
    app.run(debug=True, host='0.0.0.0', port = 9696)

