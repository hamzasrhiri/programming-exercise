## MasterMind Game:

I chose to use string comparison to solve the problem.
Each element is being compared with the input from the user, and if its correct we increment the counter by one. Same reasoning is used to find the correct number but in the wrong position.
The game continues until all the attempts are exhausted or the correct answer is guessed.

Note: To prevent double-counting when a match is found, the found element is set to None. This make sure that repeated numbers are only counted once(in cases like 1122 etc).