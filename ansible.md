
  
# <h3> INVENTORY FILE
  
# <h5> linux


    WEB1 ansible_host= ansible_connection=ssh ansible_user= ansible_ssh_pass= ansible_ssh_private_key_file=

# <h5> windows


    WEB2 ansible_host= ansible_connection=winrm ansible_user= ansible_password= ansible_ssh_private_key_file=

------------------

# <h3> PLAYBOOK  
# <h5>    
    
play  
task    
actions    


    name:
    hosts:
    tasks:
        name:
        command:
      
------------------
# <h3> MODULES  


SYSTEM,SERVICE  
COMMAND,SCRIPT  
CLOUD   
DATABASE  
FILES,LINEINFILE  


# <h5> Freeform  
# <h5> Parameters  
# <h5> Idempotency - The result of executing an action is same as executing it multiple times without any intervening actions.  


------------------

# <h3> VARIABLES  

Defined in   
- Inventory file  
- playbook  
- variable file  

------------------

# <h3> CONDITIONALS  

    when: result == 0

------------------

# <h3> ANSIBLE LOOPS    
  
lookup plugins

    loop:
    with_items:

------------------

# <h3> ANSIBLE RULES  

------------------

# <h3> ANSIBLE GALAXY  

------------------

# <h3> PATTERNS  

------------------

# <h3> DYNAMIC INVENTORY  

------------------

# <h3> ANSIBLE COMMANDS  

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
    
------------------

# <h3> Facts  
  
Facts internally uses "Setup" Module

In ansible.cfg use "gathering" filed to enable or disable facts gathering

To get info from ansible facts

    ansible -m setup localhost | grep -i version


------------------

# <h3> Configuration Files

Order of precedence of config files, least at the top

- default config file at /etc/ansible/ansible.cfg
- at user home directory
- same directory as playbook exists
- defined in a variable as below

      $ANSIBLE_CONFIG=/opt/ansible-web.cfg


Optionally configs can also be set as an environment variable

Below commands used to debug configuration file issues

    ansible-config list
    
    ansible-config view
    
    ansible-config dump | grep -i gathering
    
  
------------------


# <h3> Ansible Installation commands


YUM or apt or pip can be used based on the available package manager on the OS

    sudo pip3 install ansible
    
    sudo pip3 install ansible=2.5
    
    sudo pip3 install ansible --upgrade
  
------------------

# <h3> Ansible SSH 
  
 Generate SSH keys on Ansible controller
 
     ssh-keygen -f ~/.ssh/ansible 
 
 Add key from controller to managed node
 
 
     ssh-copy-id -i dest-path user@host


------------------

# <h3> Adhoc Commands
  
Usually used as a short form of a playbook, used to test a command or a module

    ansible -m module -i inventory
    
    ansible -m ping -i inventory 
    
    ansible -m ping localhost
    
    ansible -m setup localhost    # to gather facts on localhost
    
Note: ansible ping is not same as ICMP ping on normal terminals. Ansible ping on tests ssh connectivity

Replace -m with -a to just run a command

    ansible -a 'cat /etc/hosts' localhost
    
------------------    

