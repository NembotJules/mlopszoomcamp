# Introduction to Docker

I thought it will be a good thing to learn a little bit more about Docker before going into Ml Pipelines Orchestration.

For that i will use the Docker lesson in the Data Engineering Zoomcamp and Youtube videos.

## What is Docker

Docker is a platform that help us build, run and share software.

Docker uses something call **containers** to create isolated environments where programs run. Even though containers use the same hardware as our operating system, they are separated entities that operate in a sandbox.

Therefore all software requirements are pre-installed inside containers.

With containers, we can work on the same environment from different computers.

## Docker images

Docker images are similar to Github repositories. But instead of software -they store environments where software is installed.

Docker images have a read only format. We can build new images, but we can't change existing ones. We can think of images as a static set of instructions.

Images are instructions for containers. **If image is a blueprint for a house then the Docker container is the house itself.** In technical term, a docker container is a running instance of an image. Unlike images, we can change and interact with them.

- Images: Read, Build
- Containers : Run, Modify

## Docker compose

An alternative way of defining Docker compose