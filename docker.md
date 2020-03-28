

# <h1> Docker Topics


# <h2> What is Docker?

Docker is an open-source lightweight containerization tool.

It helps to easily create, deploy and run application using containers.



Containerisation is bundling an application together with all it's related configuration files, libraries and dependencies.

# <h2> What is Docker image?



The Docker image is a (immutable) file used to create Docker containers.  

A docker image is made up of multiple layers. An image is composed system libraries, tools, other files and dependencies for executable code.

Every docker images are stored in the Docker registry.




# <h2> What is Docker Engine?

Docker daemon or Docker engine represents the server. 

The docker daemon and the clients can be run on the same or remote host, which can communicate through command-line client binary and full RESTful API.



# <h2> What is registry in Docker?

Docker's public registry is called Docker hub.
Docker can also have private registry.



# <h2> Commands

	docker -version 						# to check docker version

	docker pull	imagename					# Download an image from docker repository

	docker run -i -t alpine /bin/bash 		# to run the image as a container

	docker ps 								# to see all running container

	docker ps -a							# to see all running and exited container 

	docker exec -it <container id> bash		# to access running container

	docker stop <container id>				# to stop a running container

	docker kill <container id>				# to kill the container

	# ‘docker stop’ gives the container time to shutdown gracefully, 
	# in situations when it is taking too much time for getting the container to stop, one can opt to kill it

	docker rm  <container id>				# to delete a stopped container

	docker rmi <image-id>					# delete image from local storage

	docker commit <conatainer id> <username/imagename>

	docker push username/imagename			# to push the new image to Docker registry

	docker images							# List of images downloaded

	docker build <path to docker file>

	docker info								# Information Command

	docker login							# to login to docker hub repository

	docker stats							# Container information

	docker-compose -f docker-compose.json up	# to use JSON instead of YAML compose file





# <h2> What are the steps for the Docker container life cycle?

Build  
Pull  
Run  



# <h2> Difference between virtualization and containerization?

	Virutalization 
	- represents hardware level virtualization
	- Heavy weight
	- Slow provisioning
	- Fully isolated and more secure

	Containerization
	- represents OS level virtualization
	- Light weight
	- real time provisioning and scalability
	- Process level isolation and less secure



# <h2> What are the different ways to build a docker image?

Interactively building Images  
Using Dockerfile  
Importing from a tarball  


# <h4> Interactive mode

	1. pull a base image and run it in interactive mode

	docker run -it --name py-flask /bin/bash

	docker exec -it py-flask /bin/bash

	2. Now make changes to the base container (add files/directories) and build layers

	docker commit py-flask my-flask

	3. Now run the newly created image

	docker run -it --name my-flask /bin/bash


# <h4> Using Dockerfile

A dockerfile is a script which contains a collection of dockerfile commands and operating system commands


	FROM

	The base image for building a new image. This command must be on top of the dockerfile.

	MAINTAINER

	Optional, it contains the name of the maintainer of the image.

	RUN

	Used to execute a command during the build process of the docker image.

	ADD

	Copy a file from the host machine to the new docker image. There is an option to use a URL for the file, docker will then download that file to the destination directory.

	ENV

	Define an environment variable.

	CMD

	Used for executing commands when we build a new container from the docker image.

	ENTRYPOINT

	Define the default command that will be executed when the container is running.

	WORKDIR

	This is directive for CMD command to be executed.

	USER

	Set the user or UID for the container created with the image.

	VOLUME

	Enable access/linked directory between the container and the host machine.

	Now let's start to create our first dockerfile.


Once the dockerfile is built, run the below command

	docker build -t my-flask .					# PS: last character is the path of the dockerfile


# <h4> Importing from a tarball

If we have an image, we can save it into a tarball with *docker save* command. 
We can import the same image from the tarball wherever we need with *docker load* command.


	docker save flask-py > myflask.tar

	docker load < myflask.tar

	docker image ls 					# it will list all images including the new one


# <h2> Difference between RUN and CMD in dockerfile

RUN lets you execute commands inside of your Docker image. These commands get executed once at build time and get written into your Docker image as a new layer.

CMD lets you define a default command to run when your container starts.



# <h2> Command to run jenkins from docker

	docker pull jenkins 									#pulls image from hub.docker.com

	docker run --name myjenkins -p 8080:8080 -p 50000:50000 -v /d/jenkins:/var/jenkins_home jenkins



# <h2> When attaching a local path as volume to a jenkins container it fails. What could be the reasons?

	1. The given windows path does not directly work on docker. Eg: D:/Jenkins
		Instead use the below format /d/jenkins

	2. The drive should be shared. If not the command fails. 
		Share the drive from docker on right had bottom corner or directly on the drive properties


# <h2> What is the use of volume in docker?

	Volumes are preferred mechanism for preserving data generated and required by docker containers.

 Usage 

 	Decoupling container from storage. On deleting containers, volumes does not delete.

 	Share and attach same volume among different containers.

# <h2> Can same volume be attached to different containers at the same time? If yes how is file read/write lock is achieved?




