# Machine Learning Orchestration using Prefect

I switch back to an old version of the course when they were using prefect(Mage is too confusing to me!).

## 3.1 Introduction to workflow orchestration

Prefect allow to Orchestrate & observe your python workflows at scale. 

Goal for module 3 : Learn how to use prefect to orchestrate and observe your Ml workflows.

## 3.2 Introduction to Prefect

You can install Prefect simply by running the command : `pip install -U prefect`. 

When you are self hosting a prefect server, you are basicall hosting : 

- *Orchestration API* : used by the server to work with workflow metadata

- *Database* : stores workflow metadata

- *UI* : visualizes  workflows

### Some prefect terminology 

**Task** : A discret unit of work in a Prefect workflow, similar to a python function, takes input, perform work and then produce output.
**Flow** : Container for workflow logic, it is also similar to a python function in which they are calls to other python functions (task). Flows can be viewed as parent function define to call tasks.

**Subflow**: A flow call by another flow.

A **task** has the `@task` decorator and the a **Flow** has the `@flow` decorator.

## 3.3 Prefect Workflow

In this chapter i learn how to run some basic workflow with prefect, moving code from experimental stage (Notebooks) to production stage (python script)  run workflows and visualize them in the UI.

## 3.4 Deploy your workflow

### Important concepts Definitions

**Deployments** : Are server-side representations of flows. They store the crucial metadata needed for remote orchestration including **when**, **where**, and **how** a workflow should run. Deployments elevate workflows from functions that you should run manually to API managed entities that can be triggered remotely.

Deployment requires a **name** and a **reference** to an underlying flow. Triggering a run of a deployment from the Prefect CLI can be done like this : 

`prefect deployment run my-first-flow/my-first-deployment`


**Worker Pool** : Work pools organize work for execution. Work pools have types corresponding to the infrastructure that will execute the flow code, as well as the delivery method of work to that environment. A simple and easy way to understand Worker Pool is to think of them as distribution center where tasks are organized before being executed. Their responsability is to decide how and where tasks or flows must be executed. There are two types of Work pool : 

- **Pull Work Pool** : In this type of work pool a ""worker"" we look for work to do in the worker pool.

- **Push Work Pool** : Here the worker pool sends directly the work to a cloud service like Google cloud run, or AWS ECS. Nobody needs to look for them.

- **Managed Work Pool** : This worker pool are automatically managed by Prefect. You don't have to worry about the way the work is distributed or run. Everything is done for you.

**Worker** : You can think of a worker, as an entity or an agent that is responsible for asking the worker pool if there is anything to be executed. 

### Important piece of Code 

**Start a Prefect project** : `prefect init`

**Start a Prefect server** : `prefect server start`

**Start a worker that polls your work pool** : `prefect worker start -p **my-pool** -t process`

**Deploy your flow** : `prefect deploy my-flow.py:say_hello -n 'my-deployment' -p **my-pool**`

**Start a run of the deployed flow from the CLI** : `prefect deployment run Hello/my-deployment`

NB : *my-pool* : is the name of the pool. <br>   
     *my-flow.py* : is the python file in which the flow you want to deploy is located. <br>  
     *say_hello*:  is the name of the entrypoint aka the function representing the flow. <br>  
     *my-deployment*:  is the name you want to give your deployment.<br>  
     *Hello*:  is the name of the deployed flow (not the name of the deployment)



