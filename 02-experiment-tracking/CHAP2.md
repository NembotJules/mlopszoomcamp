# Chapter 2 : Experiment Tracking with Mlflow 

## Important concepts

 - Ml experiment : The process of building an ML model
 - Experiment run: Each trial in an ML experiment
 - Run artifact: Any file that is associated with an ML run
 - Experiment metadata

## What's experiment tracking ?

Experiment tracking is the process of keeping track of all the **relevant information** from an **ML experiment**, which includes: 

- Source code
- Environment
- Data
- Model
- Hyperparameters
- Metrics
- ...

## Why is experiment tracking so important?

In general, because of these 03 main reasons: 

- Reproducibility
- Organization
- Optimization

## Mlflow

**Definition: "An open source platform for the machine learning lifecycle"**

In practice, it's just a python package that can be installed with pip, and it contains four main modules: 

- Tracking
- Models
- Model Registry
- Projects

## Tracking experiments with Mlflow

The Mlflow tracking module allows you to organize your experiments into runs, and to keep track of: 

- Parameters
- Metrics
- Metadata
- Artifacts
- Models

Along with this information, Mlflow automatically logs extra information about the run: 

- Source code
- Version of the code (git commit)
- Start and end time
- Author

## Installing Mlflow 

`pip` : pip install mlflow <br>
`conda` : conda install -c conda-forge mlflow

## Basic Mlflow Commands 

`import mlflow` --- To import mlflow <br>
`mlflow.set_tracking_uri("sqlite:///mlflow.db")` ---- Use sqlite as the backend store for tracking experiments <br>
`mlflow.set_experiment("nyc-taxi-experiment")` ----- Creating a new environment if one doesn't already exist  

`mlflow.log_artifact(local_path = "The local of the element you want to save, artifact_path = "Where you want to save the model in Mlflow")` <br>
`mlflow.xgboost.log_model(the model, artifact_path = "Where the model will be save in Mlflow")`

## Model Management

### Machine Learning LifeCycle

The machine learning lifecycle refers to the multiple steps that are needed in order to build and maintain a Machine Learning Model/System.

<img src = "homework/solution/imgs/Experiment-tracking.webp">

You should not use a folder system to manage your models. Why? : 

 - **Error prone:** It is possible that accidentally you end up overwriting an old model


 - **There is no versioning:**  Sometimes the name of the folder can indicate the version of the model, but this system become inefficient when you have a lot of versions


 - **No model lineage:** It is not easy to understand how all these models were created

