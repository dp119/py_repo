
  
<h3Inventory File
  
<h5 linux


    WEB1 ansible_host= ansible_connection=ssh ansible_user= ansible_ssh_pass= ansible_ssh_private_key_file=

<h5 windows


    WEB2 ansible_host= ansible_connection=winrm ansible_user= ansible_password= ansible_ssh_private_key_file=


<h3> playbook  
    
play  
task    
actions    


    name:
    hosts:
    tasks:
        name:
        command:
      

<h3> Modules  

SYSTEM,SERVICE  
COMMAND,SCRIPT  
CLOUD   
DATABASE  
FILES,LINEINFILE  


<h5> Freeform  
<h5> Parameters  
<h5> Idempotency - The result of executing an action is same as executing it multiple times without any intervening actions.  



<h3> VARIABLES  

Defined in   
- Inventory file  
- playbook  
- variable file  

<h3> CONDITIONALS  

    when: result == 0


<h3> ANSIBLE LOOPS    
  
lookup plugins

    loop:
    with_items:
  
<h3> ANSIBLE RULES  

<h3> ANSIBLE GALAXY  

<h3> PATTERNS  

<h3> DYNAMIC INVENTORY  

<h3> ANSIBLE COMMANDS  

To execute a playbook

    ansible-playbook -i inventory playbook.yml


ansible dryrun

    ansible-playbook -i inventory playbook.yml --check
  
start at task  

    ansible-playbook -i inventory playbook.yml --start-at-task
    
tag  

    ansible-playbook -i inventory playbook.yml --tag "install"
    

skip tag

    ansible-playbook -i inventory playbook.yml --skip-tag "install"
    
    
<h3 Facts  
  
Facts internally uses "Setup" Module

In ansible.cfg use "gathering" filed to enable or disable facts gathering

To get info from ansible facts
  
    ansible -m setup localhost | grep -i version
    
    
<h3 Configuration Files
  
Order of precedence of config files
  
  
Below commands used to debug configuration file issues
  
    ansible-config list
    
    ansible-config view
    
    ansible-config dump | grep -i gathering
