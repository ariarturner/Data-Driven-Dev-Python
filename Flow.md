# Git Flow

## Setup (One-time)
### [Generating a new SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
1. Open command prompt.  
3. Generate a new SSH key using your GitHub email address. `ssh-keygen -t ed25519 -C "[your-email@domain.com]"`  
4. Press Enter to accept default file location.  
5. Enter passphrase or hit enter to skip.  
6. Reenter passphrase or hit enter to skip.  
7. Ensure the SSH-agent is running. `eval "$(ssh-agent -s)"`  
8. Add SSH key to ssh-agent. `ssh-add ~/.ssh/id_ed25519`  
9. Copy SSH public key to clipboard. `clip < ~.ssh/id_ed25519.pub`  
### [Adding a new SSH key to GitHub Account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
10. On GitHub.com, click on your profile photo and then click Settings.  
11. In the Access section, click SSH and GPG keys.  
12. Click New SSH key or Add SSH key.  
13. Give a title for the key.  
14. Paste public key into the Key field.  
15. Click Add SSH key.  
### Check Global Configurations.
16. Check if user name is configured. `git config user.name`  
  a. If needed, configure user name. `git config --global user.name "[Your Name]"`  
17. Check if user email is configured. `git config user.email`  
  a. If needed, configure user email. `git config --global user.email "[your_email@domain.com]"`  
### Clone GitHub Repository to Local Machine
18. On GitHub.com, navigate to the main page of the repository.  
19. Above the list of files, click Code.  
20. Under Local > Clone, click SSH.  
21. Copy the key.  
22. Open command prompt.  
23. Clone repository and paste in key. `git clone [paste-key]`   

## Git Flow
1. Open command prompt.  
2. Set current directory to local repository. `cd "[your-path]"`  
3. Pull current main branch from remote repository. `git pull origin main`  
4. Checkout branch where updates will be made.  `git checkout -b "[your-branch]"`  
5. Make changes to your files on your local repository.
6. Check status. `git status`  
7. Snapshot file(s) in preparation for versioning.  
  a. To snapshot all files with changes. `git add .`  
  b. To snapshot specified files with changes. `git add "[your-file-name]"`  
8. Check differences between branches. `git diff`  
9. Check status. `git status`  
10. Commit changes to branch. `git commit -m "[descriptive message]"`  
11. Push local branch commits to GitHub. `git push origin [your-branch]`  
12. Go to github.com.
13. Create pull request for [your-branch].
14. Review changes.
15. Merge pull request.
16. Delete [your-branch].

## Helpful Resources & Notes
- [Git Commands Cheat Sheet](https://training.github.com/downloads/github-git-cheat-sheet.pdf)
- [Markdown Guide](https://www.markdownguide.org)
- [GitHub Markdown Guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- use `q` to quit if you see `(END)`
