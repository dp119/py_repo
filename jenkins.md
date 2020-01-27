
# <h1> Jenkins Topics






# <h2> What is Jenkins? 
Jenkins is an open source automation tool used for continous inetration and delivery and monitor them.

With Jenkins we can build pipelines to build project, run tests and then deploy


# <h2> How to turn off Jenkins Security if the administrative users have locked out of the admin console? 

We can disable the security in config.xml file and security will be disabled when jenkins is started the next time.



# <h2> Difference between webhook and polling? 
    
There are two ways your apps can communicate with each other to share information: polling and webhooks. As one of our customer champion's friends has explained it: Polling is like knocking on your friend’s door and asking if they have any sugar. Webhooks are like someone tossing a bag of sugar at your house whenever they buy some.

Webhooks are automated messages sent from apps when something happens. They have a message—or payload—and are sent to a unique URL—essentially the app's phone number or address.

Poll SCM periodically polls the SCM to check whether changes were made (i.e. new commits) and builds the project if new commits where pushed since the last build.

# <h2> What are some of the useful plugins in Jenkins?
Git repository
Amazon EC2
HTML Publisher


# <h2> How to setup a Jenkins job?
go to the Jenkins top page and then select a ‘New Job’ and build a freestyle software project.


# <h2> What is the process for creating a backup and copy files in Jenkins?
regularly backup our Jenkins_Home directory



# <h2> What are Declarative Pipelines in Jenkins?

	pipeline {
	    agent any
	    stages { 
	        stage('Example') {
	            steps {
	                echo 'Hello World'
	            }
	        }
	    }
	}

The above code has 3 major elements

Pipeline: The block of script contents.  
Agent: Defines where the pipeline will start running from.  
Stage: The pipelines contain several steps enclosed in the block called Stage.  



# <h2> What is Agent Directive in Jenkins?

Answer: The Agent is the section that specifies the execution point for the entire pipeline or any
specific stage in the pipeline. This section is being specified at the top-level inside the
pipeline block.


# <h2> How can you define a Continuous Delivery Workflow?

Git Clone
Compile
Unit test
Packaging
Deploy

# <h2> What are the various ways in which the build can be scheduled in Jenkins?

After the completion of other builds.  
By source code management (modifications) commit. (webhook)  
At a specific time. (scheduled)  
By requesting manual builds. (polling)  



# <h2> Types of jobs in Jenkins?

Freestyle project  
Maven project  
Pipeline  
Multi Config project  
Folder  
Github Org  
Multibranch pipeline  


# <h2> How to trigger jenkins build based on status changes on a jira ticket?


# <h2> Jenkins or Maven lifecycle?

	Build Test Deploy Monitor


# <h2> How to perform user access job wise?



# <h2> What are slaves and executors in jenkins?


# <h2> How to establish communication between master and slave in jenkins?


# <h2> A local repo has 10 commits performed. After which there is a push done to master. How to run test jobs for each of the commits in this push?


# <h2> Difference between Declarative and Scripted Pipeline in jenkins?


# <h4> Pipeline Code Validation at startup

	Eg: Build Step runs 5 mins  
	Test step runs 3 mins

Scripted pipeline does not fail immediately. It runs each step before failing at a specific stage (in this example it runs for 5 mins for build and fails at test stage)

Declarative pipeline fails immediately. Though the error is induced in test stage, the pipeline job fails immediately which saves time and computer resources.

# <h4> Restart only the stages

In Declarative pipeline only a particular stage can be run seperately. For example we can only run test stage.

In Scripted pipeline, this feature is missing.

# <h4> Skip stage option using WHEN block

A stage can be skipped based on a condition in Scripted pipeline using the WHEN block.


# <h4> Declarative pipeline options

Unlike scripted pipeline, there are options block in declarative pipeline. This acts as global settings.
So the implementation block is clutter free.


# <h4> Jenkins File in GIT vs Jenkins UI

Declarative script is relatively new concept that supports pipeline as code concept in jenkins.
It is easier to read and write.  
This code is written in a JenkinsFile and checked into the SCM such as Git.

The Scripted pipeline is a traditional way of writing the code. In this pipeline, the Jenkinsfile is written on the Jenkins UI instance. 


# <h4> Simple vs complex requirements

Declarative type would be ideal for simpler continuous delivery pipelines.

Scripted type  ideal for users with more complex requirements.


# <h4> Syntax 

Declarative pipeline is defined within a block labellded "pipeline"

	pipeline {
	  agent { label 'node-1' }
	  stages {
	    stage('Source') {
	      steps {
	        git 'https://github.com/digitalvarys/jenkins-tutorials.git''
	      }
	    }
	    stage('Compile') {
	      tools {
	        gradle 'gradle4'
	      }
	      steps {
	        sh 'gradle clean compileJava test'
	      }
	    }
	  }
	}



Scripted pipeline is defined within a ‘node’

	node ('node-1') {
	  stage('Source') {
	    git 'https://github.com/digitalvarys/jenkins-tutorials.git''
	  }
	  stage('Compile') {
	    def gradle_home = tool 'gradle4'
	    sh "'${gradle_home}/bin/gradle' clean compileJava test"
	  }
	}


# <h2> In Jenkins groovy how to copy files from one slave to another without using ssh or scp or sftp.

Using groovy map

# <h2> In Jenkins groovy how to pass parameters at one shot (like 30 parameters)?

Using stash and unstash

