#!/usr/bin/env python3
import sys
import os

'''
    git pull origin master --allow-unrelated-histories
    git push --set-upstream origin master
'''

#Execute git add, git commit, git push commands
def add_commit_push(*args):
    print(f'{args}')
    message = args[1]
    if message == "":
        message = input("Enter a git commit message: ")
    stream = os.popen("git --no-pager branch")
    output = stream.read()
    print(output)

    #branch = input("Which branch do you want to push to? ")
    branch = "main"
        
    stream = os.popen(f"git add -A; \
        git commit -m '{message}'; \
        git push origin {branch};")
        #git push origin {branch}; git push github {branch};")
    output = stream.read()
    print(output)

if __name__ == "__main__":
    stream = os.popen("git status")
    output = stream.read()
    if output.strip().endswith("nothing to commit, working tree clean"):
        print(output)
    else:
        add_commit_push(sys.argv[0],sys.argv[1])