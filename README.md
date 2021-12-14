# Hand Gesture Control Game With CV & ML

### SUPERVISOR: DR. ABDUL HAFEEZ
### Project Members: Muhammd ijaz & Muhmmad jawad

![fig-5-full](https://user-images.githubusercontent.com/75518471/145942424-2eed386c-66f3-4f40-b63a-b10e8928989d.png)




### Market problem:
Keyboard is the static and traditional method to interact with computer and games, for which player need to sit on a chair at a corner in static position for long time. Which effect health, especially repetitive strain injury (R.S.I) and blood circulation due to sit on a place
for long time in static position.

Besides that, often typing mistakes make the reason of game over. Which is bad experience for players.
#

#### Problem with keyboard use:
- Extra hardware
- Load on system and consume device charge
- keys loss functionality, stack or hard to press
- Miss use can lead us to repair (laptop keyboard)

![two images to stop with keyboard](https://user-images.githubusercontent.com/75518471/145939296-9791f9ba-4b1f-40be-8dea-ec7713f8dada.jpg)


#
### Problem Solution:
We create dynamic web cam hand tracking system, with help of player could control the game dynamic with body motion (gestures), which can be perform on chair or in a standing position.it not only protect health from damage but as long as player play the game, will get physical exercise.

Besides that, dynamic physical interaction make the game more interesting and effective.
#

#### Benefits:
- Long time pc use but healthy
- Get enjoyment and body exercise
- Make the games more interesting
- Dynamic physical interaction with pc
- no need of extra hardware
- less cost effective

![Webp net-resizeimage](https://user-images.githubusercontent.com/75518471/145939994-86f1d4a6-fe0d-4bb5-bb03-74cc7c6fe99f.png)

#

### Possible Improvement
In feature, it is possible to convert the web tracking system to CCTV camera.
Where the player can play the game in particular room with more body tracking
functionalities and features.

Note: we will discuss it with our supervisor then will look forward
#

### Project deployment & deployment
#### Methodologies:
1. Computer vision (To detect hand)
2. Machine Learning (make predictions for upcoming matches)
3. Web development with database (For user interference & score storage)
4. Game development (Hill claim car racing game, online source)
#

### Python libraries use:
1. Mediapipe: will use for Hand Tracking
2. Opencv: opencv will help in image processing
3. TenserFlow: Tenserflow will help in understanding the hand gestures.
#

### Web development:
- Django
- Django rest Api's
#

### Database:
- Mysql databse

#

### Project boundary
<br>

![Webp net-resizeimage (2)](https://user-images.githubusercontent.com/75518471/145946519-31dc6415-2218-4dc6-98d0-26d36548adf3.jpg)


There are a lot of games are around, which can automate to hand gestures control but we elect “Hill Climb Car Racing Game” because it’s available and run on any Android and OS devices and fixable with version control. There are two functionalities, to control the game,“gas” and break of a car.

With computer vision, we will add another feature. We will assign, and train our model on a specific hand gesture (victory or like sign) to collect player game score (car distance travel) and store it in the database.
#

### Gesture Detection

Media Pipe is a cross-platform framework, which we will use for humanbodytracking.

![media pipe hand gesture](https://user-images.githubusercontent.com/75518471/145894618-f1b3ce57-ba71-4d3d-acd2-df79b9430252.png)
#

With media pipe, we can track fingers upper landmarks (4, 8, 12, 16,
20) and middle landmarks (6, 10, 14, 19). Middle landmarks will be
focus points. In fist (✊) shape upper landmarks comes down of focus
point, which will be use for brick and vice versa.
#
<br> 

![imgonline-com-ua-twotoone-l5BMxNCJ4gaUtrW](https://user-images.githubusercontent.com/75518471/145945315-8cb61f05-3115-4368-8d9e-7d61144a50c8.jpg)

<br><br><br>

#

![guesture partern indexing](https://user-images.githubusercontent.com/75518471/145945354-bc02657c-b53a-4296-85fe-02d801c8a0e9.jpg)

#

According to above diagram, we will convert images into binary digits with the help of Numpy library. We will feed that binary image to Tenserflow trained model to extract and recognize the hand gesture and convert it into keyboards commands.
#

### Machine learning part:

![ml_pic](https://user-images.githubusercontent.com/75518471/145895785-a0c2e6c2-9f79-488a-888a-9c5630bdf056.png)


Machine Learning model will trained on a lot of games data, each game score
will feed to ML model to production score for next match.

#

### Project Milestones:
<img width="576" alt="chart" src="https://user-images.githubusercontent.com/75518471/145895511-a73cdb36-e801-4f7d-bf97-67b98116b6cf.png">

### Milestones:
-  Gather dependencies + hand tracking
-  Gesture recognitions model + deploy model on game
-  Website + server + database for storing player data + thesis
-  Total time taken and distance travel collect and store in database.
-  Collect data (Number of breaks, gas, total time taken, distance travel) and create and deploy machine learning model for next game score.
#

### Software Process Model (Incremental Model)
This will use “incremental Software Model”. In which project will divide into
increments. We will gather and freeze requirements for a specific increment
at time. After completion and deployment of one increment, another
increment will start.
#

### Process Framework
1. Software specification
2. Software design
3. Software implementation
4. Software validation
5. Software evolution
#

### Relevant Reference
![image](https://user-images.githubusercontent.com/75518471/145895579-fa69c8ce-9e71-413d-8e5d-8b14342cfdc8.png)

###### This idea is pick from virtual reality game movie “Ready Player One”.
In “Ready player one” there are a few different ways that players manage to walk and run through virtual reality, while staying in place in the real world. Wadeuses an omni In “Ready player one” there are a few different ways that players manage to walk and run through virtual reality, while staying in place in the real world. Wadeuses an omni allows him to travel in 360 degrees, at any speed he likes.

YouTube: https://youtu.be/dVjAjQAeYtM
