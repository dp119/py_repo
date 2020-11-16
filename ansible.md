
  
# <h3> INVENTORY FILE
  
# <h5> linux


    WEB1 ansible_host= ansible_connection=ssh ansible_user= ansible_ssh_pass= ansible_ssh_private_key_file=
	ansible_become=yes
	ansible_become_user=nginx

# <h5> windows


    WEB2 ansible_host= ansible_connection=winrm ansible_user= ansible_password= ansible_ssh_private_key_file=

------------------

# <h3> PLAYBOOK  

    
play  
task    
actions    

Eg1:

    - 
      name:
      hosts:
      tasks:
      -
        name:
        command:
      
Eg2:      

	-
  		name: create a new VG called vg_sql
  		hosts: node00
  		tasks: 
  		-
    		name: create a new VG called vg_sql
    		mount:
      			src: /dev/vg_sql/lv_data 
      			name: /mnt/data 
      			fstype: ext4 
      			state: mounted      
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
	
	register: result

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
	

Below command to print hostname of all managed nodes

	ansible -a "hostname" -i playbooks/inventory all
	
Below command to copy from source to dest on node00 using copy module

	ansible -m copy -a "src=/etc/resolv.conf dest=/tmp/resolv.conf" -i playbooks/inventory node00
    
Below command to Run an ad-hoc command to print the uptime of all managed nodes in the inventory file	
	
	ansible all -m shell -a uptime -i inventory
	
Below command to run playbook to read /etc/redhat-release file on all nodes in verbose mode	
	
	ansible-playbook -i playbooks/inventory playbooks/playbook.yml -vv
	

------------------

# <h3> Privilege Escalations

Privilege Escalations can be done in as a 

- command parameter as below

		ansible_playbook --become --become_method=doas --become_user=nginx --ask-become_pass
	
	note: --ask-become_pass => to prompt for password
	
	--become => to change the login shell for a remote user

- defined in playbook file
	
		become: true
		become_user: admin
		become_method: doas
	
- defined in inventory file

		dev1 ansible_host=172.20.1.100 ansible_user=admin ansible_become=yes ansible_become_user=nginx
	
- defined in default config
	
		become	= true
		become_method = doas
		become_user = nginx
	
Default value of become_user directive is root


------------------

# <h3> Examples - File Handling

To create a blank file 

		-
		  name: create a blank file
		  hosts: web1
		  tasks:
		  -
			name: create a blank file
			lineinfile:
			  path: '/var/www/html/index.html'
			  state: present
			  create: yes
			  line: "This line was added using Ansible lineinfile module!"
	  
	  
To create a file content with specified content in it

		-
		  name: create a blank file with content
		  hosts: web1
		  tasks:
		  -
			name: create a blank file with content
			lineinfile:
			  path: '/var/www/html/index.html'
			  state: present
			  create: yes
			  line: "This line was added using Ansible lineinfile module!"
	  
To find files in /opt/data directory older than 2 minutes and equal or greater than 1 megabyte in size and also copy that files under /opt directory


		---
		- hosts: web1
		  tasks:
			- name: Find files
			  find:
				paths: /opt/data
				recurse: yes
				age: 120
				size: 1m
			  register: file

			- name: Copy files
			  command: "cp {{ item.path }} /opt"
			  with_items: "{{ file.files }}"


In /var/www/html/index.html file on web1 node add some additional content using blockinfile module. Make sure user owner and group owner of the file is apache also make sure the block is added at beginning of the file. Create new playbook for this ~/playbooks/index2.yml

		-
		  name: create a blank file
		  hosts: web1
		  tasks:
		  -
			name: create a blank file
			blockinfile:
			  path: '/var/www/html/index.html'
			  owner: apache
			  group: apache
			  insertbefore: BOF
			  block:
				Welcome to KodeKloud!
				This is Ansible Lab.

On web1 node we want to run our httpd server on port 8080. Create a playbook ~/playbooks/httpd.yml to change port 80 to 8080 in /etc/httpd/conf/httpd.conf file using replace module. Also make sure Ansible restarts httpd service after making the change.
Listen 80 is the parameter that need to be changes in /etc/httpd/conf/httpd.conf

Solution 1:
 
		-
		  name: create a blank file
		  hosts: web1
		  tasks:
		  -
			name: create a blank file
			replace:
			  path: '/etc/httpd/conf/httpd.conf'
			  regexp: 'Listen 80'
			  replace: 'Listen 8080'
			  
		  -
			name: restart httpd service
			service:
				name: httpd
				state: restarted
		
Solution 2 (different syntax):		

		---
		- name: replace port 80 to 8080
		  hosts: web1
		  tasks:
		  - replace:
			  path: /etc/httpd/conf/httpd.conf
			  regexp: 'Listen 80'
			  replace: 'Listen 8080'
		  - service: name=httpd state=restarted

------------------
# <h3> Examples - Archiving



		---
		- name: to make a zip archive opt.zip of /opt directory on web1 node and save it under /root on web1 node itself
		  hosts: web1
		  tasks:
			- archive:
				path: /opt
				dest: /root/opt.zip
				format: zip      


		---
		- name: to extract its contents on web1 under /tmp directory
		  hosts: web1
		  tasks:
			- unarchive:
				src: /home/thor/playbooks/local.zip
				dest: /tmp
				
		---
		- name: an archive data.tar.gz under /root directory, extract it under /srv directory and make sure data.tar.gz archive is removed
		  hosts: web1
		  tasks:
		  - name: unzipping
			unarchive:
			  src: /root/data.tar.gz
			  dest: /srv
			  remote_src: yes

		  - name: remove the source
			file: path=/root/data.tar.gz state=absent

		---
		- name: Download  from URL and extract under /root directory
		  hosts: web1
		  tasks:
		  -   unarchive:
			   src: https://github.com/kodekloudhub/Hello-World/archive/master.zip
			   dest: /root
			   remote_src: yes
			  
			
		---
		- name: three files on web1 node /root/file1.txt, /usr/local/share/file2.txt and /var/log/lastlog. Create a bz2 archive of all these files and save it under /root, name the archive as files.tar.bz2
		  hosts: web1
		  tasks:
		  -   archive:
			   path: 
				 - /root/file1.txt
				 - /usr/local/share/file2.txt
				 - /var/log/lastlog
			   dest: /root/files.tar.bz2

Setup nginx on web1 node with some sample html code. Create a playbook ~/playbooks/nginx.yml to do so. Below are the details about the task:
a. Install nginx package and start/enable its service.
b. Extract /root/nginx.zip archive under /usr/share/nginx/html directory.
c. Inside /usr/share/nginx/html/index.html replace line This is sample html code with line This is KodeKloud Ansible lab.

		---
		- name: ngnix
		  hosts:web1
		  tasks:
		  - yum:
			 name: nginx
			 state: present
		  - service: name=httpd state=restarted	 
		  - name: nginx
			unarchive:
			 src: /root/nginx.zip
			 dest: /usr/share/nginx/html
		  - replace:
			  path: /etc/httpd/conf/httpd.conf
			  regexp: 'This is sample html code'
			  replace: 'This is KodeKloud Ansible lab'