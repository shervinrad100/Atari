# The Idea
A practice to create a scalable cloud based app.

## Phase 1
To have an Atari style gaming cartridge that can have mulitple games on it. The games are structured as microservices so that you can add or remove them and tweak them without breaking the whole game. We also want to add authentication capabilities so that we can track each user's score and collect data on what they play and how much. 
## Phase 2
The aim is to then scale this game on a cluster so that it can sustain a large number of players. Of course, this will be a psudo-scalable game because it will be run on one machine but the kubernetes cluster will allow this to be changed in the future (also its a practise anyway). 
## Phase 3
Finally we want to create a React front end because I want to learn React and also because why not. And with that the project will be complete.


# Code of Conduct 
- Please branch before committing so we can know who wrote what code in case there are mistakes or questions
- Pull before you push
- To submit code to main branch please create a PULL REQUEST so we can formally go through the code and make sure its compatible. Its going to be a big project so its gonna get messy if we dont be strict with these
- Please include ISSUE NUMBER in COMMIT MESSAGE 
- DOCUMENT EVERYTHING! Please comment your code and add to the documentation so that a beginner using your code can understand the datastructers or parameters needed
- Create tickets as issues. If you think there is a cool feature please share ideas as issues. Just make sure to label them properly and give descriptions
- Don't forget to put tickets into the "In progress" column on the project Kanban to avoid duplicating work


### Dependencies 
- python 3
- Docker 
  - (WSL if windows)
