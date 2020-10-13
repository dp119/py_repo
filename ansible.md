
#Inventory File
#linux
WEB1 ansible_host= ansible_connection=ssh ansible_user= ansible_ssh_pass= ansible_ssh_private_key_file=

#windows
WEB2 ansible_host= ansible_connection=winrm ansible_user= ansible_password= ansible_ssh_private_key_file=


#playbook
play
task
actions

-
  name:
  hosts:
  tasks:
    -
      name:
      command:
      

Freeform
Parameters
Idempotency - The result of executing an action is same as executing it multiple times without any intervening actions.


#Modules
SYSTEM,SERVICE
COMMAND,SCRIPT
CLOUD
DATABASE
FILES,LINEINFILE


#VARIABLES
Defined in 
- Inventory file
- playbook
- variable file

#CONDITIONALS

  when: result == 0


#ANSIBLE LOOPS
lookup plugins

  loop:
  with_items:
  
#ANSIBLE RULES

#ANSIBLE GALAXY

#PATTERNS

#DYNAMIC INVENTORY

#ANSIBLE COMMANDS

ansible-playbook -i inventory playbook.yml


#ansible dryrun
ansible-playbook -i inventory playbook.yml --check
ansible-playbook 
