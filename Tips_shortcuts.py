## Ubuntu
'''cd = means change directory
cd .. = one step back
ls = list = the items that you have on that carpet
cd mnt = change of directory mounting = it will take you to the files
cd c = local user
cd / = take you all the way back to the user or main current computer
 the comandas go like this
 cd / 
 cd mnt
 cd c
 cd user
 cd "your name"
 ls
 choose de file that you need to get in
 cd "file"
 ls
 
 commands to clear
  cd clear
  
  commands to create a new directory = folder
  mkdir== making a directory
  go like this will create a new directory and sub directory
  mkdir test =  creating the new directory
  ls = checking everything was executed correctly
  mkdir service = ceting the sub directory
  ls = check once again,
  
  commands to erase files
  in order to erase or deleted those documents all we got to do is to delete the main one
  rm -rf test ==  this way both files get deleted
  
  Creating directorys and files 
  mkdir "name" creating a directory= folder
  Touch file.csv == creating any file in this instance i created a csv file
    
    deleting files
    
    rm file.csv == done rm = remove
    
    ### Git
     git init = inicializar el git
     git status == revisar el estado del repositorio
     git add . == subir al staging area los cambios de todos los arcivos
     git add "file name" ==  subira solo los cambios de ese archivo
     git commit -m"mensaje" ==  now you will commit all the changes reminder put the comment if not it will give you a default messague or it will give you and error
     git rm --cache "file name" == will put your file on standby
     git log == its to track the movements of your commits or going back or forward
     git checkout "id number" == te deja ir hacia ese commit
     git checkout master == take you back to the actual commit
     git revert ==is more safe it will take all the change made in the past commit
     git reset == is hard it will erase all the commit and it will take you back to the commit that you point
     types of gits resets
     git soft == take you one back in time then you can make changes and make add , commits afterwars
     git mix ==this one take back the commits and the stages start from cero making changes and need to follow the procedeers once again
     git hard == is to completly removed them from stages and working areas
     git ignore creation
     Touch git ignore
     git add 
     git commit -m"message"
     here you will put the unwanted files that you dont want or need to track
       
       
       ##GIT HUB
       this is the structure
       git status
       git add . or file name
       git commit -m"message"
       git remote v == to check if you hace conected the local with the remote ssh
        git remote add origin “here copy and paste the ssh code from your repo in the remote repo”
        git push -u origin main == you push or pull because it will be connected
         if they large files you need to follow this structure
       
       git lfs installe
         git status
       git add . or file name
       git commit -m"message"
       git push -u origin main 
        BRANCHES
        has to be added and commited into the initial because if not the branch will go to the master
        Git status
       Git add  . 
         Git checkout -b dev  == creating a new branch name dev
           Git checkout master == going back to my master one
          Git branch -a ==listed all the branches that we have
        
        Deleting branches
         Git branch -d “file”
         
         Editing branches
        Adding  commits
            Git checkout dev
            Git add  .
            Git commit -m “new commit branch”
        
        Merging branches
        Two different commands
        
        Basically first yo have to follow some procedures as usual 
 Git status 
Git add .
Git commit -m”release v”
Git checkout master
Git status to check everything is good

Git merge dev == we will merge with the file that we specified DEV
 fork is producing a personal copy of someone else's project. Forks act as a sort of bridge between the original repository and your personal copy. You can submit Pull Requests to help make other people's projects better by offering your changes up to the original project. Forking is at the core of social coding at GitHub.
After forking this repository, you can make some changes to the project, and submit a Pull Request as practice.

Never download not useful..

        


       
       
       
    
  
  
  '''