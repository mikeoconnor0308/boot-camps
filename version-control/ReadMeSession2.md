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
