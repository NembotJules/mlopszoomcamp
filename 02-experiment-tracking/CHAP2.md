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

pip : pip install mlflow
conda : conda install -c conda-forge mlflow

## Basic Mlflow Commands 

import mlflow --- To import mlflow
mlflow.set_tracking_uri("sqlite:///mlflow.db") ---- Use sqlite as the backend store for tracking experiments
mlflow.set_experiment("nyc-taxi-experiment") ----- Creating a new environment if one doesn't already exist

