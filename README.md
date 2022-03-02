# SankeGame
SnakeGame is a video game genre where the player maneuvers a growing line that becomes a primary obstacle to itself.

Modules : turtle, random & time
Font : Courier

The snake will grow its body when the snake eats an egg.
So, the score will be counted.
Checking for the snake’s head collisions with the body or the wall of the window screen.

Steps:

1. Create the screen
   1. screen size : 600X600 
   2. bg color : Black

2. Create a snake adding 3 square shaped turtles
   1. snake class
   2. set it to motion
   3. It can move forwards, back, left or right.

3. Create egg and make it appear at random position when a snake touches it

4. Detect when the snake collides with walls or its tail
   #1. Display "GAME OVER" at center
   2. create a new snake and make the old snake disappear

5. Detect when the snake eat an egg
   1. increase the score +1

6. Create a score board
   1. keeps track of old score and new score
   2. write data in score_sheet 
   3. retrieve the data on updating the score


