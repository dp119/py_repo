
# <h1> Jenkins Topics






# <h4> What is Jenkins? 
Jenkins is an open source automation tool used for continous inetration and delivery and monitor them.

With Jenkins we can build pipelines to build project, run tests and then deploy


# <h4> How to turn off Jenkins Security if the administrative users have locked out of the admin console? 

We can disable the security in config.xml file and security will be disabled when jenkins is started the next time.



# <h4> Difference between webhook and polling? 
    
There are two ways your apps can communicate with each other to share information: polling and webhooks. As one of our customer champion's friends has explained it: Polling is like knocking on your friend’s door and asking if they have any sugar. Webhooks are like someone tossing a bag of sugar at your house whenever they buy some.

Webhooks are automated messages sent from apps when something happens. They have a message—or payload—and are sent to a unique URL—essentially the app's phone number or address.

Poll SCM periodically polls the SCM to check whether changes were made (i.e. new commits) and builds the project if new commits where pushed since the last build.

# <h4> What are some of the useful plugins in Jenkins?
Git repository
Amazon EC2
HTML Publisher


# <h4> How to setup a Jenkins job?
go to the Jenkins top page and then select a ‘New Job’ and build a freestyle software project.


# <h4> What is the process for creating a backup and copy files in Jenkins?
regularly backup our Jenkins_Home directory



# <h4> What are Declarative Pipelines in Jenkins?

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



# <h4> What is Agent Directive in Jenkins?

Answer: The Agent is the section that specifies the execution point for the entire pipeline or any
specific stage in the pipeline. This section is being specified at the top-level inside the
pipeline block.


# <h4> How can you define a Continuous Delivery Workflow?

Git Clone
Compile
Unit test
Packaging
Deploy

# <h4> What are the various ways in which the build can be scheduled in Jenkins?

After the completion of other builds.  
By source code management (modifications) commit. (webhook)  
At a specific time. (scheduled)  
By requesting manual builds. (polling)  



# <h4> Types of jobs in Jenkins?

Freestyle project  
Maven project  
Pipeline  
Multi Config project  
Folder  
Github Org  
Multibranch pipeline  


# <h4> How to trigger jenkins build based on status changes on a jira ticket?


# <h4> Jenkins or Maven lifecycle?

	Build Test Deploy Monitor


# <h4> How to perform user access job wise?



# <h4> What are slaves and executors in jenkins?


# <h4> How to establish communication between master and slave in jenkins?


# <h4> A local repo has 10 commits performed. After which there is a push done to master. How to run test jobs for each of the commits in this push?


# <h4> Difference between Declarative and Scripted Pipeline in jenkins?


# <h5> Pipeline Code Validation at startup

	Eg: Build Step runs 5 mins  
	Test step runs 3 mins

Scripted pipeline does not fail immediately. It runs each step before failing at a specific stage (in this example it runs for 5 mins for build and fails at test stage)

Declarative pipeline fails immediately. Though the error is induced in test stage, the pipeline job fails immediately which saves time and computer resources.

# <h5> Restart only the stages

In Declarative pipeline only a particular stage can be run seperately. For example we can only run test stage.

In Scripted pipeline, this feature is missing.

# <h5> Skip stage option using WHEN block

A stage can be skipped based on a condition in Scripted pipeline using the WHEN block.


# <h5> Declarative pipeline options

Unlike scripted pipeline, there are options block in declarative pipeline. This acts as global settings.
So the implementation block is clutter free.


# <h5> Jenkins File in GIT vs Jenkins UI

Declarative script is relatively new concept that supports pipeline as code concept in jenkins.
It is easier to read and write.  
This code is written in a JenkinsFile and checked into the SCM such as Git.

The Scripted pipeline is a traditional way of writing the code. In this pipeline, the Jenkinsfile is written on the Jenkins UI instance. 


# <h5> Simple vs complex requirements

Declarative type would be ideal for simpler continuous delivery pipelines.

Scripted type  ideal for users with more complex requirements.


# <h5> Syntax 

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


# <h4> In Jenkins groovy how to copy files from one slave to another without using ssh or scp or sftp.

Using groovy map

# <h4> In Jenkins groovy how to pass parameters at one shot (like 30 parameters)?

Using stash and unstash


# <h4> Jenkins Libraries Used

Job DSL - For creating new jobs from pipeline

# <h4> After a pipeline job executes, Is it possible to automate trigger of jenkins freestyle job? Or is it possible to call freestyle from pipeline job?


# <h2>#####Jenkins V2

# <h4>  What are the ways to integrate Jenkins with GIT ?
What are the ways to integrate Jenkins with Jira ?  
	
# <h4>  How would you copy files from one server to another in jenkins?  
	
# <h4>  Jenkins Shared Library folder structure?
How to copy files in resources to Workspace?
Is it possible to have shared library in local instead of git repo? If yes how do you configure?  
	
# <h4>  How do you automate job creation in jenkins?  
Job DSL plugins
	
# <h4>  After a pipeline job executes, Is it possible to automate trigger of jenkins freestyle job? Or is it possible to call freestyle from pipeline job?
(Trigger parameterized build on other projects)  
	
# <h4>  For a new project implementaion how would you choose which pipeline to go with - Declarative and Scripted Pipeline?


# <h4>  Is it possible to run shell script within jenkins plugins?  If yes, a variable declared within groovy script is not available within the shell script. Why?
Because it's not declared with env.Variable_name=
	Eg: env.x=10
