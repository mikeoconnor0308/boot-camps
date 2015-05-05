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
git config --global alias.ll 'log --pretty=format:"%C(yellow)%h%Cred%d\\ %Creset%s%Cblue\\ [%cn]" --decorate --numstat'
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

Globally-unique commit identifier can be used to compare or go back to previous commits. `COMMITID`, `OLDER_COMMITID` and `NEWER_COMMITID` refer to hashes (the long string of numbers outputted by `git log`:

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
