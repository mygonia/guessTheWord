# guessTheWord
A little game I made where you are presented with 4 pictures and you have to guess the word they all refer to.

Type your answer in the text input.

Press enter to submit your answer. If it is correct, you gain 5 points. You get as many tries as you need to get it right.
Shift to use a point to get a hint revealing a letter in the correct answer.
Escape to skip the puzzle at the expense of 3 points.


For this project, I wanted to clone a simple game.
I started by getting a list of words from [The Great Noun List](http://www.desiquintans.com/downloads/nounlist/nounlist.txt).
I then used Python to loop through each word in the list, get 4 images from Google using [google_images_download](https://github.com/hardikvasa/google-images-download), then saved those images into a dictionary as a list with the noun as their key.
The dictionary was then saved into a .txt file.
I used HTML/CSS/Javascript to make the game.
