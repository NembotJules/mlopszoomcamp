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
