# Auto-Push
Just a simple Python script to push code automatically after a specified period of time.
Consider it like auto-save but for git😁

You're welcome😎


# Installation
To install auto-push, refer to the included INSTALL.md

# Usage
```auto-push [--dir] [--branch] [--commit] [--interval]```

**--dir**   is the path to the directory you want to push. Defaults to CURRENT DIRECTORY

**--branch**        is the branch to which you want to push. Default is the result of the 'git branch' command.

**--commit* *       is a template for the commit message. Default is 'auto-commit-[uuid]
        For example: if --commit='auto-commit' then all the commit message will be 'auto-commit-[uuid]'.
        Note: You can also put the uuid anywhere else in the string like so: --commit='commit-#num#-automatic'
The --commit above will be turned into 'custom-[uuid]-automatic'

**--interval**      is the interval between pushes in minutes. Default is 5 minutes

Note: - You can press q anytime to quit
      - p is for pausing or resuming
      - cb [newbranch] is for changing to a new branch while it's running
