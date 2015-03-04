This file discusses the gml programs provided. Unlike many of my other provided work, all of
these were parts of personal gaming projects and done outside of school.

TextBoxScripts

- Purpose is to take a string and display each character individually and in a timely manner.
	- For instance, the word "Hello" would not appear all at once. Instead, it would appear
	  in the order "H, E, L, L, O" at a specified time interval.

- scr_split_string()
	- This script was made because Game Maker did not seem to provide a built in .split
	  function. This function takes in a string and splits it with a provided "splitter"
	  (ex. Hello|Bob, | is the splitter)

- scr_cal_totalString()
	- This script takes in the result from scr_split_string() and combines the individual
	  letters together. It also adds a "\n" (in Game Maker this is a # sign) whenever the
	  specified letters-per-line limit is reached. 

- scr_typing_text()
	- This script takes the result from scr_cal_totalString() and displays it to the screen
	  based on given time intervals


OtherScripts

scr_ghost_movement()

	- Purpose is to provide basic AI for a ghost in Pac-Man
	- While the logic for each individual ghost is under-contruction, this provides a strong
	  base.
	- The ghost moves in the best direction towards Pac-Man when it hits a wall
	- When the ghost "sees" Pac-Man, it will change course to attack him

scr_jump()
	- This is a general jump script created for a main platformer character
	- Jump and DoubleJump are implemented here
	- Gravity is applied properly
	- Different jump heights are possible based on how long the user presses down the jump
	  button