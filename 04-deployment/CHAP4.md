# 4 Model Deployment

## 4.1 Three ways of deploying a model

- Batch mode (offline deployment) : Here the model is not up and running all the time, we apply our model to new data on a regular base (hourly, daily, etc)
- Online deployment : We need the model to be up and running all the time, we need predictions as soon as possible. It online deployment we have two variances: web services and streaming.

In web service, the mode is available via a web service we can send http request and get predictions from the service. Streaming is when there is a stream of events, models services is listening to the stream of events and provide predictions in real time.



## 4.2 Web services : Deploying a model with Flask and Docker

How to deploy a model as a webservices : 

* Creating a virtual environment with Pipenv
* Creating a script for prediction 
* Putting the script into a Flask app
* Packaging the app to Docker


```bash
docker build -t ride-duration-prediction-service:v1 .
```

```bash
docker run -it --rm -p 9696:9696  ride-duration-prediction-service:v1
```

## 4.3 Deployment to the cloud: AWS Elastic Beanstalk

In the previous step we built a Docker image, build the container, put our ride duration prediction service there and also the model. Then we build this image and learn how to run it locally. Now we want to take this image and deploy it to the cloud.


**[Amazon Elastic Beanstalk](https://aws.amazon.com/de/elasticbeanstalk/)** is one of the services in Amazon AWS. It’s an easy way to deploy your services, also including dockerized containers.

### Introduction to AWS Elastic Beanstalk

In the world of cloud computing, deploying and managing web applications can be a complex and time-consuming task. Enter AWS Elastic Beanstalk, a service provided by Amazon Web Services (AWS) that simplifies the process of deploying and scaling web applications.

### What is AWS Elastic Beanstalk?

**[Amazon Elastic Beanstalk](https://aws.amazon.com/de/elasticbeanstalk/)** is a Platform as a Service (PaaS) offering that abstracts away the underlying infrastructure and streamlines the deployment, scaling, and management of web applications. With Elastic Beanstalk, developers can focus on writing code, while AWS takes care of provisioning resources, load balancing, auto-scaling, and monitoring.

Key Features of AWS Elastic Beanstalk:

- **Easy Deployment:** Elastic Beanstalk supports multiple programming languages and web frameworks, making it suitable for a wide range of applications. You can deploy your code with a few simple commands or use integrated development environments (IDEs) to seamlessly deploy from your development environment.


- **Automatic Scaling:** Elastic Beanstalk can automatically adjust the number of application instances based on traffic load. This ensures that your application remains responsive even during traffic spikes, without manual intervention.


- **Managed Infrastructure:** AWS handles all the infrastructure management tasks, including server provisioning, operating system updates, and security patches. This allows developers to focus on writing code and delivering features.


- **Monitoring and Analytics:** Elastic Beanstalk provides built-in integration with AWS CloudWatch, enabling real-time monitoring of application performance and resource utilization. You can set up alarms and triggers to respond to issues proactively.


- **Easy Environment Management:** Developers can create multiple environments for different stages of the development lifecycle, such as development, testing, and production. Each environment is isolated, making it easy to test changes before deploying them to production.

### Who Should Use AWS Elastic Beanstalk?

AWS Elastic Beanstalk is an excellent choice for startups, small businesses, and development teams looking to streamline the deployment and management of web applications. It’s also suitable for experienced AWS users who want to reduce the operational overhead of managing infrastructure.

### How AWS Elastic Beanstalk Enhances the Ride Duration Prediction Service

Here’s how it works: AWS Elastic Beanstalk (EB) serves as the orchestrator in the cloud. Our ride-duration service is running inside a container within EB. To enable external communication, we’ve already exposed the port within this container.

Now, when the marketing service sends a request to EB, Elastic Beanstalk acts as a bridge. It forwards the incoming request to the container hosting our ride-duration service. The container processes the request and sends back the prediction. This way, the marketing service obtains the necessary prediction data.

One of the remarkable features of Elastic Beanstalk is its ability to dynamically adjust to varying traffic loads. When a surge of requests arrives, EB can automatically scale up, utilizing load balancing to distribute traffic efficiently. This scaling process involves adding more containers and instances of our service to meet the increased demand.

Conversely, when traffic subsides, Elastic Beanstalk can scale down gracefully, reducing the number of containers and instances. This automatic scaling ensures that resources are optimized according to the actual workload, helping us achieve cost-efficiency and responsiveness in our application deployment.

In essence, AWS Elastic Beanstalk acts as a flexible and responsive manager for our containerized churn service, allowing it to seamlessly adapt to changing traffic patterns while maintaining performance and reliability.

### Installing the EB CLI

To install the command line interface for AWS Elastic Beanstalk (awsebcli) as a development dependency, you can use the following commands:

```bash
pipenv install awsebcli --dev
```

After installing, you can activate the virtual environment with:

```bash
pipenv shell
```

Then, initialize an Elastic Beanstalk application with the specified options using:

```bash
eb init -p docker -r eu-west-1 ride-prediction-service
```

This command will create an Elastic Beanstalk application named ‘ride-prediction-service’ and generate a ‘.elasticbeanstalk’ folder containing a ‘config.yml’ file, which contains configuration settings for your Elastic Beanstalk environment.

### Running eb locally

Before deploying your application to the cloud, you can use AWS Elastic Beanstalk to test it locally. Elastic Beanstalk provides a convenient way to replicate the deployment environment on your local machine.

To run your application locally with Elastic Beanstalk, you can use the following command:

```bash
eb local run --port 9696
```

This command sets up a local environment that mimics the configuration of your Elastic Beanstalk environment, including port mappings.

Now, to test our locally running application, we open another terminal window and use the following command:

```bash
python test.py
```

This command will send a request to our locally hosted service, allowing us to validate that everything is working as expected before deploying to the cloud. It’s a crucial step in ensuring a smooth deployment process.

### EB best pratices

When installing and using AWS Elastic Beanstalk (EB), there are a few additional considerations and best practices to keep in mind:

- **AWS Credentials:** Ensure that you have configured AWS credentials properly. You can use the AWS Command Line Interface (CLI) or IAM roles if you’re running EB on an AWS resource like an EC2 instance. Make sure the credentials have the necessary permissions for creating and managing Elastic Beanstalk resources.


- **Region Selection:** Specify the AWS region where you want to deploy your Elastic Beanstalk application. The ‘-r’ flag in the ‘eb init’ command specifies the region. Choose a region that is geographically close to your target audience for lower latency.


- **Platform:** Select the appropriate platform for your application. In your example, you’re using the Docker platform. Elastic Beanstalk supports various platforms, including Node.js, Python, Ruby, Java, and more. Choose the one that matches your application’s technology stack.


- **Environment Configuration:** After initializing your application, you’ll typically create one or more environments within that application. Environments are isolated instances of your application with their own settings. You can define environment-specific configuration, such as environment variables and scaling options.


- **Deployment:** Use the ‘eb deploy’ command to package and deploy your application code to Elastic Beanstalk environments. This command uploads your code and dependencies to the environment, making it available for execution.


- **Logs and Monitoring:** AWS Elastic Beanstalk integrates with AWS CloudWatch for monitoring and logging. You can access logs and performance metrics to monitor the health and performance of your environments. Set up alarms and triggers to be notified of any issues.


- **Scaling:** Elastic Beanstalk provides auto-scaling options to automatically adjust the number of instances based on traffic. You can configure scaling policies to ensure that your application can handle fluctuations in demand.


- **Security:** Implement security best practices by configuring security groups, using AWS Identity and Access Management (IAM) for access control, and applying encryption where necessary.


- **Cost Management:** Keep an eye on the cost of running Elastic Beanstalk environments, especially when using auto-scaling. Use AWS Budgets and Cost Explorer to manage and optimize your AWS expenses.


- **Documentation and Support:** AWS Elastic Beanstalk has extensive documentation and a support community. If you encounter issues or need assistance, consult the official documentation and consider leveraging AWS support options.

By following these considerations and best practices, you can effectively install, configure, and manage AWS Elastic Beanstalk for your applications while ensuring reliability and cost-efficiency.

### Deploying the model to the cloud

To create an Elastic Beanstalk environment for your application, you can use the following command:

```bash
eb create ride-duration-prediction-env
```

This command initiates the creation of an Elastic Beanstalk environment named ‘churn-serving-env.’ Please note that the environment creation is not instantaneous, so it may take a moment to complete. Once the process finishes, you’ll receive information indicating the specific address where your application is available.

An essential point to highlight here is that creating an Elastic Beanstalk environment this way makes it accessible from the internet by default. Therefore, it’s crucial to implement proper security measures and ensure that only authorized services and users have access.

Now, to test our running application, open another terminal window and execute the following command:


```bash
python test.py
```
While using EB we must do a few changes in test.py.

```bash
import requests

ride = {
    "PULocationID": 1,
    "DOLocationID": 30,
    "trip_distance": 2
    }

host = 'ride-prediction-env.......elasticbeanstalk.com'

url = f'http://{host}/predict'
response = requests.post(url, json=ride)
print(response.json())

```

we have changed the url, by replacing localhost with the address of our eb service.

To terminate the Elastic Beanstalk environment when you’re done with it, you can use the following command:

```bash
eb terminate ride-duration-prediction-env
```

This command will gracefully shut down and remove the Elastic Beanstalk environment, helping you manage your resources efficiently.


## 4.3 Web-services: Getting the models from the model registry (MLflow)

1) Pre-requisite : Create an EC2 instance, create an S3 bucket, see if you can find the list of bucket using your EC2 instance with the command: 


```bash
 aws s3 ls
```


If you have the CredentialError: Unable to locate credentials,  use : **aws configure**, put your access id, your access secret key id, set your region.

If after that your are still unable to connect it means what of the previous information is wrong.


2) Start the mlflow tracking server: 

```bash
mlflow server --backend-store-uri=sqlite:///mlflow.db --default-artifact-root=s3://the-name-of-your-s3-bucket/
```

Now open the Mlflow UI at http://127.0.0.1:5000

3) Create a Jupyter Notebook to train the Random Forest Model, tracked and saved the model in Mlflow.

We can check the experiment detail in the Mlflow UI. [Include an Image of the Mlflow UI]

At this step if you have the NoCredentialsError it means Mlflow cannot access your S3 bucket. How can you fix it??

MLflow and Boto3 (the AWS SDK for Python) look for AWS credentials in the environment variables by default. You can set these variables in your terminal session:

```bash
export AWS_ACCESS_KEY_ID=your_access_key_id
export AWS_SECRET_ACCESS_KEY=your_secret_access_key
export AWS_DEFAULT_REGION=your_default_region
```

If the previous don't work you can set the variables using os: 

```bash
import os
os.environ["AWS_ACCESS_KEY_ID"] = "your_access_key_id"
os.environ["AWS_SECRET_ACCESS_KEY"] = "your_secret_access_key"
os.environ["AWS_DEFAULT_REGION"] = "your_default_region"
```

After that you can start using the logged model.  There are multiple ways to use the logged model. If we are using runs/RUN_ID/model then we run with risk of availability lest the tracking server should go down. However, if fetch the artifact directly from S3 then we are not dependent on the artifact server. Please check the predict.py script to see the changes made.





















