
# <h2>  What is Jboss or JBoss EAP (Enterprise application platform)?


JBoss is an application server platform used for hosting highly transactional Java applications.


Both JBoss and Tomcat are Java servlet application servers, but JBoss is a whole lot more. 
Tomcat is much more limited. 

One way to think of it is that JBoss is a JEE stack that includes a servlet container and web server, whereas Tomcat, for the most part, is a servlet container and web server.



JBoss EAP provides two operating modes for JBoss EAP instances: standalone server or managed domain. 
The standalone server operating mode represents running JBoss EAP as a single server instance. 
The managed domain operating mode allows for the management of multiple JBoss EAP instances from a single control point.

The management console and management command-line interface (CLI) make editing XML configuration files unnecessary and add the ability to script and automate tasks. 
While you can still edit the XML files manually it’s not suggested to do so.



# <h2> Difference between web server and app server?



# <h2> What is artifactory?

Artifactory is a product by JFrog that serves as a binary repository manager. 

(That said very often one will use a 'artifactory' as a synonym of the more general binary repository, much like many people use Frigidaire or fridge to denote the refrigerator regardless if it is a Frigidaire brand or not)


The binary repository is a natural extension to the source code repository, in that it will store the outcome of your build process, often denoted as artifacts. Most of the times one would not use the binary repository directly but through a package manager that comes with the chosen technology.


# <h2> What is Elasticsearch?

Fully distributed enterprise search and analytics engine.
Used to create own search engine or to analyze the data and extract useful information.

It's a document database 
we can query documents and run analysis and aggregations on search results.


Backend repository for logging and monitoring infrastructure.


Apache lucene is used as core search library to provide search functionality.

Popular enterprise search engine.



# <h3> ElasticSearch Features

Distributed and Scalable Horizontally

High Availability because of multiple copies of data

RESTful API to perform operations creating retrieving updating and deleting via simple JSON based HTTP calls

Powerful Query DSL - Express complex queries simply with JSON

Schemaless - (Index data without an explicit schema). Need not follow specific schema or datatypes or specific field names beforing indexing and parsing documents.


Examples - 
Ecommerce site to index product catalog, inventory, provide autocomplete for users

Video hosting site to index video clips, tags etc

E learning site to index courses, authors, topics covered




# <h3> Elastic components
Kibana is a data visualization.

Logstash is a data processing pipeline
which can analyze data from multiple sources.



Document is the smallest unit of data stored in elasticsearch.

Index is the collection of similar documents.

Shards is logically dividing the Index (helps easily searchable)

Node is a machine where the shard is hosted

Cluster is the collection of shards

Replica are backup of shards and contain exact same information as shard


With added node the shards are rebalanced automatically by ES





# <h2> What is REST api?

REST - or Representational State Transfer 
(can be used over nearly any protocol, when used for web APIs it typically takes advantage of HTTP)

A RESTful API is an application program interface (API) that uses HTTP requests to GET, PUT, POST and DELETE data. 
REST leverages less bandwidth, making it more suitable for internet usage


(which is why REST technology is generally preferred to the more robust Simple Object Access Protocol (SOAP) technology)




# <h2> What is Maven?

Maven is Project management tool.  
It is a framework which simplifies and standardizes the project build process for the team.


# <h4> Default directory structure for Maven - 

	source code			${basedir}/src/main/java
	Resources			${basedir}/src/main/resources
	Tests				${basedir}/src/test
	Compiled byte code	${basedir}/target
	distributable JAR	${basedir}/target/classes


POM - Project Object Model

It is fundamental unit of work in Maven. It is an XML file that resides in the base directory of the project as pom.xml

It should be noted that there should be a single POM file for each project.

	All POM files require the project element and three mandatory fields: groupId, artifactId, version.

	Projects notation in repository is groupId:artifactId:version.




The Super POM is Maven’s default POM. All POMs inherit from a parent or default (despite explicitly defined or not). This base POM is known as the Super POM, and contains values inherited by default.

Command to check Super POM default configurations

	mvn help:effective-pom



# <h2> Explain different stages of maven life cycle.

Prepare resources  
Validate  
Compile  
Test  
Package  
Install  
Deploy  

Also there will be additional pre and post phases to register goals.

When a phase is called via Maven command, for example mvn compile, only phases up to and including that phase will execute.

# <h2> What is Build Profile in Maven?

A Build profile is a set of configuration values, which can be used to set or override default values of Maven build.  
Using a build profile, you can customize build for different environments such as Production v/s Development environments.

A Maven Build Profile can be activated in various ways.

	Explicitly using command console input.
	Through maven settings.
	Based on environment variables (User/System variables).
	OS Settings (for example, Windows family).
	Present/missing files.



# <h2> Can we have multiple pom.xml in a project. What are the benefits?



# <h2> What is a Maven Repository?

In Maven terminology, a repository is a directory where all the project jars, library jar, plugins or any other project specific artifacts are stored and can be used by Maven easily.

Maven repository are of three types. The following illustration will give an idea regarding these three types.

	local 	- %USER_HOME% is the default directory. Override default location with %M2_HOME%\conf\settings.xml 
	central - repository provided by Maven community
	remote	- developer's own custom repository containing required libraries or other project jars


# <h2>  What are Maven Plugins?
Maven is actually a plugin execution framework where every task is actually done by plugins. Maven Plugins are generally used to −

create jar file
create war file
compile code files
unit testing of code
create project documentation
create project reports


	mvn [plugin-name]:[goal-name]

	mvn compiler:compile


# <h2> Maven - External Dependencies?

If dependency is not available in any of remote repositories and central repository?
Maven provides answer for such scenario using concept of External Dependency.

	Add lib folder to the src folder.

	Copy any dependency/jar into the lib folder.

	add this external dependency to maven pom.xml



# <h2> What is SNAPSHOT in Maven?

SNAPSHOT is a special version that indicates a current development copy

Unlike regular versions, Maven checks for a new SNAPSHOT version in a remote repository for every build.

# <h4> Snapshot vs Version

In case of Version, if Maven once downloaded the mentioned version, say data-service:1.0, it will never try to download a newer 1.0 available in repository. To download the updated code, data-service version is be upgraded to 1.1.

In case of SNAPSHOT, Maven will automatically fetch the latest SNAPSHOT (data-service:1.0-SNAPSHOT) every time the project is built.


# <h2> What is Build Automation ?


Build Automation defines the scenario where dependent project(s) build process gets started once the project build is successfully completed, in order to ensure that dependent project(s) is/are stable


Example

Consider a team is developing a project bus-core-api on which two other projects app-web-ui and app-desktop-ui are dependent.

app-web-ui project is using 1.0-SNAPSHOT of bus-core-api project.
app-desktop-ui project is using 1.0-SNAPSHOT of bus-core-api project.


Now, teams of app-web-ui and app-desktop-ui projects require that their build process should kick off whenever bus-core-api project changes.

We can proceed with the following two ways −

	Add a post-build goal in bus-core-api pom to kick-off app-web-ui and app-desktop-ui builds.

	Use a Continuous Integration (CI) Server like Hudson to manage build automation automatically.


# <h2> What information does POM contain?
POM contains the some of the following configuration information −

	project dependencies
	plugins
	goals
	build profiles
	project version
	developers
	mailing list

# <h2> Ellucian

Ansible Interview questions

Load Balancers questions

Docker Questions

Testing tools 

Relational VS Document databases

# <h2> Optimum Solutions

Artifactory admin

Groovy interview questions

# <h2> JanBask (Trainer Role)
https://www.janbasktraining.com/devops-certification-training

What is DevOps culture, SDLC introduction and agile methodology.

Ansible AWS

Introduction about cloud, virtualization and physical infra.

Linus Administration command and file system.


Variables, looping, decision making in 
shell scripting

Introduction about POM and maven life cycle and goals
Maven plugins, dependency management and project templates


How to Setup Ansible and setup SSH connection and inventory?

Introduction to Log management tools?


Introduction about AWS cloud platform
How to setup an AWS account and secure it using AMI service.
Managing AWS users, groups, roles and policies.
Managing AWS instances using EC2, Security Group and Key pair.
Working with AWS services like ELB, EBS, S3, VPC, RDS and Route 53 etc.


Nagios and Q&A

System Monitoring tool using Nagios and Q&A
Why Monitoring in important for continuous monitoring in DevOps?
Introduction to Nagios for monitoring
Concepts behind Nagios
Installation and configuration Nagios.
Generating reports and configuring notifications and checks.
Analysing applications, network and server related issues.
Q&A session to discuss queries and doubts.
Overview on resume preparing and interview questions.
Demo on sample Jenkins pipeline



# <h2> Opentext
• 5+ yrs of experience in various log shippers for application, system, network devices like filebeat, metricbeat, fluentd, heka, logstash etc.
• Developing and managing pipeline rules for high volume multi-tenant log providers in logstash.
• Exposure in development of plugin to extend opensource features to suit enterprise needs on graylog/ELK technologies.
• Good exposure to efficient grok, stream rules, pipeline extractors in graylog.
• Manage and own Graylog infrastructure like capacity planning, upgrades and scaling.
• Managing elastic index by developing solutions around tools like curator.
• Exposure to automation technologies like Ansible and ability to develop playbook for automation.
• Working experience with hybrid cloud model (Private Cloud, Public cloud) preferably exposure to GCP.
• Exposure to containerization technologies (docker and Kubernetes).