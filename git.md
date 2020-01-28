
# <h1> GIT Topics






# <h2> What is Git? 

GIT is an opensource distributed version control system and source code management system.



# <h2> What is the difference between Git and Github?
Git is the version control system that tracks changes in the source code.
It aides in co-ordinating work among programmers and can track in any set of files.

Github is repository hosting service. It provides more features like GUI, access control and several collaboration features.


# <h2> What is a repository in Git?
Repository in Git is a place where Git stores all the files. Git can store the files either on the local repository or on the remote repository.


# <h2> Frequently used git commands?

	git init 								# to initalyze a local git repo
	git clone <remote repo name>			# to clone a remote repo to local
	git status
	git add .
	git commit -m "message"
	git push
	git push origin master

	git pull
	git fetch
	git merge

	git branch 								# lists all branches
	git branch branchname					# creates new branch
	git checkout branchname					# to switch to a branch

	git stash 								# stashes (saves) with default name
	git stash name 							# stashes with given name
	git stash list 							# lists available stash lists
	git stash drop name 					# drops a particular stash
	git stash clear 						# drops all stash

	git revert 								# revert a commit that has already been pushed and made public

	git cherry-pick <commit-hash>

	git diff-tree -r {hash}


# <h2> What is ‘bare repository’ in Git?
A “bare” repository in Git contains information about the version control and no working files (no tree) and it doesn’t contain the special .git sub-directory.

 whereas the working directory consists of :
 
A .git subdirectory with all the Git related revision history of your repository.
A working tree, or checked out copies of your project files.



# <h2> What is a ‘conflict’ in git? How to resolve it?

Git can handle on its own most merges by using its automatic merging features. There arises a conflict when two separate branches have made edits to the same line in a file, or when a file has been deleted in one branch but edited in the other.

On UI - Conflict can be resolved manually by removing the marked lines in the file. Then click on "Resolve now" and then on "compare and pull" 

On CLI - Navigate to the file having the merge conflict and open it in an editor. Search for conflict marker in the file. So edit the file manually and keep the changes that is to be incorporated. Then run git add <filename>

Conflict markers look similar to below  
		<<<<<<< HEAD   
		=======   
		>>>>>>> BRANCH-NAME  

Conflict can also be resolved with git squash, git rebase and git merge methods


# <h2> In Git how do you revert a commit that has already been pushed and made public?

	git revert <name of bad commit>


# <h2> What is the difference between git pull and git fetch?
	Git pull = git fetch + git merge 


# <h2> What is ‘staging area’ or ‘index’ in Git?
before completing the commits, it can be formatted and reviewed in an intermediate area known as ‘Staging Area’ or ‘Index’.


# <h2>  What is the difference between the ‘git diff ’and ‘git status’?
 ‘git diff’ is similar to ‘git status’, the only difference is that it shows the differences between various commits and also between the working directory and index. 
 
 
# <h2>  What is git cherry-pick?
 The command git cherry-pick is normally used to introduce particular commits from one branch within a repository onto a different branch.

 Cherry picking is the act of picking a commit from a branch and applying it to another.

 	git cherry-pick <commit-hash>
 

# <h2>  How do you find a list of files that have changed in a particular commit?
 	git diff-tree -r {hash}
 
 
# <h2>  What do you mean by Git fork?
 A Git fork is nothing but a copy of a Git repository. In a Git ecosystem forking down a Repository enables you with liberal experimentation with different changes with little or no Effects on your original project.
 
 Then it can be merged with the original repo using Pull requests.
 

 
# <h2>  What is the HEAD in git?
 HEAD is a reference to the last commit in the currently checked-out branch.
cat .git/HEAD

# <h2>  what is .gitignore

Git sees every file in your working copy as one of three things:

tracked - a file which has been previously staged or committed;
untracked - a file which has not been staged or committed; or
ignored - a file which Git has been explicitly told to ignore.

Ignored files are tracked in a special file named .gitignore that is checked in at the root of your repository. 
There is no explicit git ignore command
Instead the .gitignore file must be edited and committed by hand when you have new files that you wish to ignore



# <h2>  What are different branching strategy in Git

Feature Branches

	Feature branches are the ones developers create to work on new features. 
	After the feature is complete, the developer should merge the feature back to master.

Release Branches

	These branches allow for preparation of a new release. And besides that, they enable the developer to perform minor bug fixes and to prepare metadata for the release. 
	
	Since this work is being done in a separate branch, the development branch is free to receive featuresintended for the next release.
	
Hotfix Branches

	Hotfix branches are for bug fixes.
	This release isn’t planned. 
	Instead, it’s due to necessity: a critical bug in production that must be dealt with swiftly


# <h2> How to save the work and switch between branches


	git stash 

"git stash" command temporarily stores (temporarily but safely) the uncommitted local changes.  
This way we can come back and re-apply them later on.

After stash we are free to make changes, create new commits, switch branches, and perform any other Git operations

NOTE: Stash is local to your Git repository. Stashes are not transferred to the server when you push


	git stash list 									# to list the list of stash
	stash@{0}: WIP on master: 5002d47 our new homepage
	stash@{1}: WIP on master: 5002d47 our new homepage
	stash@{2}: WIP on master: 5002d47 our new homepage

	git stash pop										# will re-apply the most recently created
														# "git stash pop" applies and deletes the stash

	git stash pop stash@{0}:


	git stash drop stash@{1}							# to delete a stash
	Dropped stash@{1} (17e2697fd8251df6163117cb3d58c1f62a5e7cdb) 

	git stash clear 									# to clean all stash


# <h2> How to link git with JIRA for comments, stage changes etc

Using Smart commit feature available in JIRA.


# <h2> How to enforce branch naming strategies in GIT.

Using branch rules in GIT repo settings.

# <h2> What are git branch controls/rules?


# <h2> How to trigger jenkins build job for each of the commits made in git?

	
# <h5> *Learn more about markdown [here](https://guides.github.com/features/mastering-markdown/)*