
# <h4> What is Jboss or JBoss EAP (Enterprise application platform)?


JBoss is an application server platform used for hosting highly transactional Java applications.


Both JBoss and Tomcat are Java servlet application servers, but JBoss is a whole lot more. 
Tomcat is much more limited. 

One way to think of it is that JBoss is a JEE stack that includes a servlet container and web server, whereas Tomcat, for the most part, is a servlet container and web server.



JBoss EAP provides two operating modes for JBoss EAP instances: standalone server or managed domain. 
The standalone server operating mode represents running JBoss EAP as a single server instance. 
The managed domain operating mode allows for the management of multiple JBoss EAP instances from a single control point.

The management console and management command-line interface (CLI) make editing XML configuration files unnecessary and add the ability to script and automate tasks. 
While you can still edit the XML files manually it’s not suggested to do so.


# <h4> What is artifactory?

Artifactory is a product by JFrog that serves as a binary repository manager. 

(That said very often one will use a 'artifactory' as a synonym of the more general binary repository, much like many people use Frigidaire or fridge to denote the refrigerator regardless if it is a Frigidaire brand or not)


The binary repository is a natural extension to the source code repository, in that it will store the outcome of your build process, often denoted as artifacts. Most of the times one would not use the binary repository directly but through a package manager that comes with the chosen technology.


