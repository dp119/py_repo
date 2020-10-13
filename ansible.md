
  
<h2> Inventory File
  
<h4> linux

  WEB1 ansible_host= ansible_connection=ssh ansible_user= ansible_ssh_pass= ansible_ssh_private_key_file=

<h4> windows
  
  WEB2 ansible_host= ansible_connection=winrm ansible_user= ansible_password= ansible_ssh_private_key_file=


<h2> playbook
play
task
actions


    name:
    hosts:
    tasks:
        name:
        command:
      


<h5> Freeform
<h5> Parameters
<h5> Idempotency - The result of executing an action is same as executing it multiple times without any intervening actions.


<h2> Modules  

SYSTEM,SERVICE
COMMAND,SCRIPT
CLOUD
DATABASE
FILES,LINEINFILE


<h2> VARIABLES

Defined in 
- Inventory file
- playbook
- variable file

<h2> CONDITIONALS

  when: result == 0


<h2> ANSIBLE LOOPS  
  
lookup plugins

  loop:
  with_items:
  
<h2> ANSIBLE RULES

<h2> ANSIBLE GALAXY

<h2> PATTERNS

<h2> DYNAMIC INVENTORY

<h2> ANSIBLE COMMANDS

ansible-playbook -i inventory playbook.yml


#ansible dryrun
ansible-playbook -i inventory playbook.yml --check
ansible-playbook 
