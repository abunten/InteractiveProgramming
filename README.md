# InteractiveProgramming
This is the base repo for the interactive programming project for Software Design, Spring 2016 at Olin College.

## Project Overview

For our Interactive Programming project we turned the keyboard of the computer into something like the keyboard of a piano where different notes could be played with different keys. The user can choose any note in three octaves and the length of the note. The keys associated with each note are organized on the keyboard to be user friendly and intuitive. In order to visualize the different notes, each note is associated with a specific shape in a specific color. The the sharp and flat of a specific note display the same shape in the same color, but the color gets brighter and lighter depending on whether the note is a sharp or a flat.

## Results

Our final product is an interactive and visual keyboard. Similar to a piano the notes A through G (A, B, C…) correspond to the keyboard keys A through J on a standard QWERT keyboard. We choose to use the letter keys along the middle of the keyboard in order to use the letter keys above and below for the sharps and flats of each note (A – G). The sharps are located on keys Q through U and the flats are located on keys Z through M. Additionally, we choose to make playing longer notes an option and to do so the user simply must press the shift key before the note they want to play. 

An interesting feature of our program is that you can change the octave you are in and play chords. We chose to use octaves 3, 4, and 5 which can be selected by pressing either number key 3, 4, or 5, however the default octave is 4, or middle C. We were able to accomplish chords by using a library that allowed for some overlap in files. When the user presses two keys at the same time the effect is a chord with those two notes.

A specific shape is also assigned to each note with a specific color depending on whether the note played was a sharp, flat, or natural. The shape is displayed as long as the note is played and updates every time a note is played. The visual effect is that the shape and color on the screen changes every time a different note is pressed. 

Link to a video of the program working: 

[link text itself]: https://drive.google.com/file/d/0B_BxF5xN1dGGYzhsOEoybUFOTFE/view?usp=drivesdk

## Implementation
Our program used an input from the user to a controller to access a shape object created and stored in our model class. Each shape object is associated with a specific note and shape which corresponds to a wave file in the controller class and a geometric shape in the view class. After a key is pressed, the shape object that is associated with that key is used to find and play the correct wave file and display the correct geometric image. 

![UML}(https://docs.google.com/drawings/d/1ElJWWhUs15-bLzPqrFeJJvZRCiu5Ha5ZQtWwIQSW8Q8/edit)

One of the big design decisions that we had to make in building our program how the user would interact with the controller. We had originally made the controller class play the sharps and flats of each note by pressing the shift key for sharps or the control key for flats. This, we discovered, was not as friendly to the user as the  user could not play a sharp or flat and a natural note in a cord. After realizing this, we reworked the controller class to make every note (natural, sharp, and flat) its own key. 

## Reflection

Looking back on this project we would say that it was fairly successful. We did appropriately scope the work, as getting an Most Viable Product up and running proved to be the most challenging aspect of the project. Our goal with our MVP was to press one key and have that one key be associated with a single shape and a specific wave file. After we had our MVP up and running we were able to divide the work between two tasks: the shapes that were displayed and the note associated with each keyboard input. In dividing the tasks than needed to be done as such, we were able to work pretty efficiently since each task was fairly independent of the other. 

One of our biggest challenges with this project in the beginning was figuring out which Python library to use in order to create and play the notes we wanted. We ended up using two different python libraries: Pysynth and Pygame. Pysynth was used to create and save the wave files for each note and then Pygame was used to play the saved wave file in our program. We originally started out using Pyaudio to play the notes, however it was incredibly slow because it would only display the shape after the wave file was completely done playing, and because each wave file is two seconds long, it was incredibly slow. 

If we were to do this project again we would plan more of our visualizations to make them cooler. With our current project we are using simple geometric shapes, but in the future it would be cool to implement more visual affects. 
