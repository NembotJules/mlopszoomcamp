import pickle
import mlflow



from flask import Flask, request, jsonify

import mlflow

RUN_ID = '0f06d2686fe64fda9f835fcd7639d773'

#loggin the model directly from S3

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

