# Version Control and Git - crib sheet

Git is officially available for download here → [git-scm.com](http://git-scm.com/)

[![](version_control.png)](http://karthik.github.io/git_intro/#/slide-title)

## Initial setup

 If you are one a computer account that has not used git before
 then you should probably introduce yourself to git. This information
 will be associated with the changes that you make to files later:

    $ git config --global user.name "Count Dracula"
    $ git config --global user.email "count@sesame-street.edu"

Because working with git will involve making notes about your changes
you should probably go ahead and register your text editor with git.
The following lines tell git how to call your text editor in a way that  will pause git until you close your editing session. The commands differ a bit from editor to editor. 

You can use `nano`, `vim`, whatever you [prefer](http://www.sublimetext.com/)! 

    $ git config --global core.editor "vim" 

All of these options are stored in a file called `.gitconfig`. I've included a sample [here](sample.gitconfig).

**Add some aliases **

```
git config --global alias.st status 
git config --global alias.ci commit 
git config --global alias.co checkout
git config --global alias.ls 'log --pretty=format:"%C(yellow)%h%Cred%d\\ %Creset%s%Cblue\\ [%cn]" --decorate'
git config --global alias.ll `'log --pretty=format:"%C(yellow)%h%Cred%d\\ %Creset%s%Cblue\\ [%cn]" --decorate --numstat'
# I can share more shortcuts here
```



---

## Working with a local repository

Let's create a local repository for this week's workshop:

    $ mkdir hackathon
    $ cd hackathon
    $ git init

Let's take a look at what files `git` has made:

    $ ls -A

### Git configuration

Let's look at our Global configuration from the options we just added.

    $ cat ~/.gitconfig
    [user]
	name = Your Name
	email = yourname@yourplace.org
    [core]
	editor = nano
    $ git config -l

### Working with files in the repository

Now let's add something to the repository! For simplicity, we're going to start with a [Markdown](http://daringfireball.net/projects/markdown/syntax) file, but it can be anything!

    $ nano rfc-template.md

Next, write some text. 

```markdown    
    # Title

    by Authors

    ## Overview

    ## Key points

    * One
    * Two
    * Three...

    ## References
    
    * Reference
    * ...
```

Now we'll look at our Git status to see the current state of our repository 


    $ git status

You should see something like this: 
```
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	rfc-template.md

nothing added to commit but untracked files present (use "git add" to track)
```

Git is telling us that there are some untracked files, which we need to tell it to track. 

    $ git add rfc-template.md
    $ git status rfc-template.md

Now we've added the file, and you should see:

```
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   rfc-template.md
```

The file is now in the staging area, ready to be committed 

    $ git commit

Commit message - provide the "why" about a change.

Top tip: Write useful commit messages, not "made a change".

Commit shows number of files changed and the number of lines inserted or deleted. 

    $ git status rfc-template.md

`nothing to commit` means file is in the repository, working directory up-to-date, no uncommitted changes in staging area.

    $ git log

Commit identifier (AKA revision number) uniquely identifies the changes made in this commit, author, date, and message.
Now let's just do another quick commit on another new file:

    $ git log --relative-date
    $ cp rfc-template.md data-rfc.md
    $ git add data-rfc.md

Instead of opening up the editor, you can just quickly commit via command-line.

    $ git commit -m "Create data RFC from rfc-template.md."

Now let's make some changes to `data-rfc.md`:

```markdown
# Hackathon Notes

by Mike O'Connor, David Glowacki and Fred Manby

## Overview
```
    

    $ git status data-rfc.md

Modified - changed but not staged or commited. Git shows us that the file has been changed, but it has not been staged or commited yet. Let's do that now: 

    $ git add data-rfc.md
    $ git commit -m "Added title, authors, overview, points, references" 


### Discarding changes

Make a few more changes to `data-rfc.md`, which we're not going to keep:

```markdown
# Hackathon Notes

This workshop is terrible.... 

by Mike O'Connor, David Glowacki and Fred Manby

## Overview
```

Use `diff` to see what's changed: 

    $ git diff data-rfc.md

`-` line removed, `+` line added, `-` and `+` line edited.

I've changed my mind, let's throw away changes (revert).

    $ git checkout -- data-rfc.md
    $ git status data-rfc.md

### History

    $ git log
    $ git ls
    $ git ll
    $ git log data-rfc.md

Globally-unique commit identifier can be used to compare or go back to previous commits:

    $ git diff COMMITID
    $ git diff OLDER_COMMITID NEWER_COMMITID
    $ git log
    $ git checkout COMMITID
    $ ls
    $ git checkout master
    $ ls

Top tip: There's the notion of 'atomic commits'. If you commit often with every change you make, you can precisely undo any mistakes you make, and track progress. Very useful for hunting down bugs! 

DropBox and GoogleDrive also preserve every version, they delete old versions after 30 days, or, for GoogleDrive, 100 revisions. 

DropBox allows for old versions to be stored for longer but you have to pay for this. 

Using revision control the only bound is space available!

Commit changes to sets of files and rollback to exact state.

### Branches

    $ git status 

`master` is a branch name.

Branches are multiple sets of changes to files and directories - parallel instances.

Useful for bug-fixing releases while working on product or trying out a new feature. 

Create branch for release.

    -o---o---o                               master
              \
               o                             release

Continue developing on default, master, branch.

    -o---o---o---o---o---o                   master
              \
               o                             release

Fix bug in release branch and release bug-fixed version.

    -o---o---o---o---o                       master
              \
               o---o---o                     release

Merge changes into master.

    -o---o---o---o---o---M                   master
              \         /
               o---o---o                     release

Continue developing.

    -o---o---o---o---o---M---o---o           master
              \         /
               o---o---o                     release

Popular model of release branch, master (up-to-date stable) branch, feature-specific and/or developer specific branches.

             0.1      0.2        0.3
              o---------o------o------    release
             /         /      /
     o---o---o--o--o--o--o---o---o---    master
     |            /     /
     o---o---o---o     /                 fred
     |                /
     o---o---o---o---o                   kate

Let's create a branch.
```
 git branch some-notes
 git checkout some-notes
```
Note we could do this with one command:

```
 git checkout -b some-notes
```
Make some changes to `data-rfc.md`.

```
git add data-rfc.md
git commit -m "new features"
```
Now imagine we needed to go back to the master branch and make a change to `rfc-template.md`

```
git checkout master 
```

Make some changes to `rfc-template.md`. Let's commit with a one-liner 

```
git commit -am "Quick fix" 
```

Ok now we're happy with the changes, and we want to bring the changes on the `some-notes` branch back into `master`. For that we use the merge command. 

```
git merge some-notes
```

What if we had made conflicting changes to the same file? We'll look into that below. 

## Working from multiple locations with a remote repository

We're now keeping track of our code on this machine, but what if we lose the laptop, or accidentally delete the folder? What if we want to work from other machines, or with other people? 

### GitHub and BitBucket

* [GitHub](http://github.com) 
* [BitBucket](http://bitbucket.com)
* [Launchpad](https://launchpad.net)
* [GoogleCode](http://code.google.com)
* [SourceForge](http://sourceforge.net)

These services provide cloud based repositories and project infrastructure e.g. wiki, issue (ticket) and bug trackers, release management, commit-triggered e-mails etc.

All rights are reserved on unlicensed repositories - you should licence it to let people know what they can and cannot do with it.

BitBucket offers free, private repositories to researchers. 

GitHub and others offer pricing plans to host private repositories.

Git =/= GitHub

Let's create a repository on both. 

[Sign-up for free GitHub account](https://github.com/signup/free)

[Sign-up for free BitBucket account](https://bitbucket.org/account/signup/)

### Create new repository

GitHub:
* [Log in](https://github.com).
* Click on Create a new repo icon on top right, next to user name.
* Enter Repository name: `hackathon`.
* Check Public option is selected.
* Check Initialize this repository with a README is unselected.
* Click Create Repository.

BitBucket:
* [Log in](https://bitbucket.com).
* Click on Create  icon on top left, next to Bitbucket logo.
* Enter Repository name: `hackthon`.
* Check private repository option is ticked.
* Check repository type is `Git`.
* Check Initialize this repository with a README is unselected.
* Click Create Repository.

Push `master` branch to GitHub:

    $ git remote add origin https://github.com/USERNAME/bootcamp.git
    $ git push -u origin master

Push `master` branch to BitBucket:

    $ git remote add origin https://USERNAME@bitbucket.org/USERNAME/bootcamp.git
    $ git push -u origin --all

`origin` is an alias for repository URL. `-u` sets local repository to track remote repository.

GitHub, click Code tab and click Network tab.

BitBucket, click Source tab and click Commits tab.

### Cloning a remote repository

Let's delete our local copy of the repository (!) and clone it from one of the remote repositories

    $ cd ..
    $ rm -rf hackathon
    $ git clone https://github.com/USERNAME/hackathon.git
    $ git clone https://USERNAME@bitbucket.org/USERNAME/hackathon.git
    $ cd hackathon
    $ git log
    $ ls -A

### Push changes to a remote repository

    # Make changes, add, commit.
    $ git push

GitHub, click Code tab and click Network tab.

BitBucket, click Source tab and click Commits tab.

Always pull before push. This way you make sure your commits match the remote repository

### Pull changes from a remote repository

    $ cd ..
    $ ls
    $ git clone https://github.com/USERNAME/bootcamp.git anotherbootcamp
    $ git clone https://USERNAME@bitbucket.org/USERNAME/bootcamp.git anotherbootcamp
    $ ls

Pretend clones are on separate machines. 3 repositories - one remote, 2 local on our 'separate machines'.

    $ cd bootcamp
    $ nano data-rfc.md

Make changes, add, commit.

    $ git push
    $ cd ../anotherbootcamp
    $ git fetch
    $ git diff origin/master

Compare `master` branch with `origin/master` branch, alias for branch on remote repository.

    $ git merge origin/master
    $ cat data-rfc.md
    $ git log

pull = fetch + merge

    $ nano data-rfc.md

Make changes, add, commit.

    $ git push
    $ cd ../bootcamp
    $ git pull
    $ cat data-rfc.md
    $ git log

### Conflicts and resolution

    $ nano data-rfc.md

Make changes, add, commit.

    $ git push
    $ cd ../anotherbootcamp

Make changes to same lines, add, commit.

    $ git push

Push fails because it cannot merge the conflicting changes. Fetch changes made to remote repository.

    $ git fetch
    $ git diff origin/master
    $ git merge origin/master

Merge done file-by-file, line-by-line. Conflict - file has two changes affecting the same line.

    $ git status

Unmerged.

    $ cat data-rfc.md

`<<<<<<< HEAD` lines from local version.

`=======` delimiter

`>>>>>>> 71d34decd32124ea809e50cfbb7da8e3e354ac26` lines from remote version.

Keep local, or keep remote, or combine both. Remove all the mark-up.

    $ git add data-rfc.md
    $ git commit -m "Resolved conflict in data-rfc.md by ...."
    $ git push

GitHub, click Code tab and click Network tab.

BitBucket, click Source tab and click Commits tab.

DropBox and GoogleDrive don't do this. No work is lost.

## Collaborating with colleagues

Form into pairs and swap GitHub / BitBucket user names.

One of you (Owner) share your repository with your partner.

Owner, on GitHub, click on the Settings tab, click on Collaborators, add partner's GitHub name.

Owner, on BitBucket, click Share link, add partner's BitBucket name.
Both,

    $ git clone https://github.com/OWNERUSERNAME/bootcamp.git
    $ git clone https://USERNAME@bitbucket.org/USERNAME/bootcamp.git 

Now:

* Both edit same file, add and commit.
* Owner push.
* Partner push, fetch, merge, resolve conflicts (if any), add, commit, push.
* Owner pull.
* Both edit same file, add and commit.
* Owner push, fetch, merge, resolve conflicts (if any), add, commit, push.
* Partner pull.
* Repeat! Try adding and editing new files too.

## More on branching

    $ git branch

`*` signifies current branch.

    $ git branch new_template
    $ git branch
    $ git checkout new_template
    $ git branch
    $ nano template-rfc.md

Change, add, commit.

    $ git checkout master
    $ ls
    $ git checkout new_template
    $ ls
    $ git checkout master
    $ ls
    $ git merge new_template
    $ git branch -D new_template

## Summary

* Keep track of changes, a lab notebook for code and documents.
* Roll back changes to any point in the history of changes, "undo" and "redo" for files.
* Back up entire history of changes in various locations.
* Work on files from multiple locations.
* Identify and resolve conflicts when the same file is edited within two repositories without losing any work.
* Collaboratively work on code or documents or any other files.

## Links

* K. Ram  (2013) "git can facilitate greater reproducibility and increased transparency in science", Source Code for Biology and Medicine 2013, 8:7 doi:[10.1186/1751-0473-8-7](http://dx.doi.org/10.1186/1751-0473-8-7) - survey of the range of ways in which version control can help research.
* [Visual Git Reference](http://marklodato.github.com/visual-git-guide/index-en.html) - pictorial representations of what Git commands do.
* [Pro Git](http://git-scm.com/book) - the "official" online Git book.
* [Version control by example](http://www.ericsink.com/vcbe/) - an acclaimed online book on version control by Eric Sink.
* [Git commit policies](http://osteele.com/posts/2008/05/commit-policies) - images on what Git commands to with reference to the working directory, staging area, local and remote repositories.
* [Gitolite](https://github.com/sitaramc/gitolite) - a way for you to host
your own multi-user Git repositories. Your collaborators send you their public SSH keys then they can pull and push from/to the repositories.
* [A successful Git branching model](http://nvie.com/posts/a-successful-git-branching-model/)
* G. Wilson, D. A. Aruliah, C. T. Brown, N. P. Chue Hong, M. Davis, R. T. Guy, S. H. D. Haddock, K. Huff, I. M. Mitchell, M. Plumbley, B. Waugh, E. P. White, P. Wilson (2012) "[Best Practices for Scientific Computing](http://arxiv.org/abs/1210.0530)", arXiv:1210.0530 [cs.MS].

## Git hints and tips

### `man` page

Like many Unix/Linux commands, `git` has a `man` page,

    $ man git

You can scroll the manual page up and down using the up and down arrows.

You can search for keywords by typing `/` followed by the search term e.g. if interested in help, type `/help` and then hit enter.

To exit the manual page, type `q`.

### Add a repository description

You can edit the file `.git/description` and give your repository a name e.g. "My first repository".

### Ignore scratch, temporary and binary files

You can create a `.gitignore` file which lists the patterns of files you want Git to ignore. It's common practice to not add to a repository any file you can automatically create in some way e.g. C object files (`.o`), Java class (`.class`) files or temporary files e.g. XEmacs scratch files (`~`). Adding these to `.gitignore` means Git won't complain about them being untracked.

Create or edit `gitignore`,

    $ nano .gitignore

Then add patterns for the files you want to ignore, where `*` is a wildcard,

    *~
    *.o
    *.so
    *.dll
    *.exe
    *.class
    *.jar

Then, add `.gitignore` to your repository,

    $ git add .gitignore
    $ git commit -m "Added rules to ignore XEmacs scratch files and binary files"

### Add colour to `diff`

    $ git config --global color.diff auto
