
# <h1> Puppet Topics



# <h2> What is Puppet?

The Puppet is a configuration management tool that is extensively used for automating the administration tasks. Puppet tool helps you deploy, manage and configure your servers.


# <h2> What is Manifests?

The Manifests are just files in Puppet wherein the client configuration is specified.
The manifest is the closest thing to what one might consider a Puppet program.

# <h2> What is the difference between a Module and a Manifest?
The manifests that we define in modules can be included in the manifests. This makes it easier to manage the manifests. It is possible to push the chosen manifest on to the specific agent or node.

A module is a structure used for creating portable code. While modules usually contain manifests, they also typically contain files, templates, metadata, and test cases
 
# <h2> What is Facter?
The Facter is a system profiling library which is used to gather system information during a Puppet run. The Facter offers your information regarding the IP address, version of kernel, CPU and others.


# <h2> What is MCollective?
The MCollective is a tool that is developed by the Puppet labs for server orchestration. MCollective helps to run thousands of jobs in parallel using your own or existing plugins.


# <h2> What is Puppet architecture?



# <h2> What is the difference between puppet and ansible?

Puppet has master slave arch. It has agent running on slaves
Ansible has just the server and no agents


Mode of communication
Puppet communicates with the agent
Ansible communicates with the node via SSH


Puppet CM has pull based approach (clients poll a centralized master periodically for updates)
Ansible has push based approach

Ansible supports exception handling
Puppet does not have exception handling support


Both servers can only be installed on a LINUX machine


Puppet has a DSL syntax and 
Ansible uses YAML files with relatively simple syntax 


Puppet config files are called manifests with extension .pp
Ansible config files are called Playbook






# <h2> Puppet uses push or pull method?


# <h2> What is heira files in puppet?


# <h2> Which is the first file the puppet file looks for?

	site.pp


# <h2> Which is revision in puppet?


# <h2> 