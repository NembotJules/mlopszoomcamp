# 5 Model Monitoring

Traditional Software Application vs Machine Learning Application after deployment

Based on the Software developement lifecycle, if you have rigorously tested, and deployed your code, it should work as expected. In terms of monitoring your application, you might be worried about system metrics, error rates, traffic volume, app loading times, infrastructure. 

But in Machine Learning things are different...

Machine Learning models degrade over time. They’re dynamic and sensitive to real changes in the real world. 

From the moment you deploy your model to production, it begins to degrade in terms of performance. A model is at its best just before being deployed to production. This is why deployment should not be your final step.


So we need to monitor our Machine Learning system. Ml monitoring is mostly about four aspects : 

- **Service Health** : The general health of our service 
- **Model performance** : Based on the metrics we fixed
- **Data Quality and Integrity**
- **Data Drift and Concept Drift**

Now let's talk a little bit more about Data Drift and Concept Drift as they are the more popular : 

**Data Drift** : When you deploy a machine learning model in production, it will face real world data. This data might be different from what the model has seen during training. As a result the performance of the model will decline. The reason is that when a machine learning model "learns" what it actually learn is the distribution of the data, so you can expect the model to perform well on data similar to that distribution. But when the model is already train(have learned) a certain distribution, it fails to predict correctly new data point too different from that data distribution and that is what cause Data drift/


**Concept Drift:** In a supervised machine learning setup, we build a model based on historical data, and then we used the train model to predict on unseen data.  In the process, the model learns a relationship between the target variable and input features. For instance, an email spam classifier, that predicts whether an email is spam or not based on the textual body of the email. The machine learning model learns a relationship between the target variable (spam or not spam) and the set of keywords that appears in a spam email. These sets of keywords might not be constant, their pattern changes over time. Hence the model build on the old set of emails doesn’t work anymore on a new pattern of keywords. The relationship between the text in the email and whether is spam or not has changed and that is what we call Concept Drift. 

Don't get confuse Data drift and Concept drift are not the same, here is the difference : 

Data drift refers to a change in the features distribution where Concept drift refer to a change in the relationship between the features and the target variable.

Now a question emerge, how can you avoid all this problem??

By monitoring your Ml system. How specifically it's exactly what i will learn in the following days

See you!


## 5.2 Environment Setup

Here we used Docker compose to set up our different services, i checked everything work as expected. Here is the docker compose file for reference: 


```bash
version: '3.7'

volumes: 
  grafana_data: {}

networks:
  front-tier:
  back-tier:

services:
  db:
    image: postgres
    restart: always
    environment:
      POSTGRES_PASSWORD: example
    ports:
      - "5432:5432"
    networks:
      - back-tier

  adminer:
    image: adminer
    restart: always
    ports:
      - "8080:8080"
    networks:
      - back-tier
      - front-tier  

  grafana:
    image: grafana/grafana-enterprise
    user: "472"
    ports:
      - "3000:3000"
    volumes:
      - ./config/grafana_datasources.yaml:/etc/grafana/provisioning/datasources/datasource.yaml:ro
     # - ./config/grafana_dashboards.yaml:/etc/grafana/provisioning/dashboards/dashboards.yaml:ro
     # - ./dashboards:/opt/grafana/dashboards
    networks:
      - back-tier
      - front-tier
    restart: always
```

Here is the grafana_datasources.yaml for reference : 

```bash
# config file version
apiVersion: 1

# list of datasources to insert/update
# available in the database
datasources:
  - name: PostgreSQL
    type: postgres
    access: proxy
    url: db:5432
    database: test
    user: postgres
    secureJsonData:
      password: 'example'
    jsonData:
      sslmode: 'disable'
      database: test
```

In order to set up all the services you just need to run : 

```bash
docker-compose up --build
```


In my LinkedIn post i need to talk about : 

- What is Evidently
- Evidently Report
- Evidently Dashboard

Why is Evidently a good choice for Batch mode : In batch mode, data comes in batch and therefore we can compare the distributions of that data to the distribution of our reference data. This is how we mesure Drift.


Learn How to calculate some dummy metrics and load the information in the Grafana database, access data and visualize it using Grafana Dashboard.

dummy_metrics_calculation.py we want to create a database, create a table, write a function which add metric row by row, we are going to create a cycle
    
