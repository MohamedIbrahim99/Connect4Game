# Connect-4 Game
AI agent solving Connect-4 using minimax algorithm (with and without pruning)

![GIF](http://i.imgur.com/Ssfp7.gif)

### How to run
- It is run from */GUI/Main.py* file. 

### User Guide
1. Choose if you want to apply pruning to the minimax algorithm and set the K value.
Then, press the play button.

![Main](/readme/Main.jpg)

2. The red (Human) and yellow (Computer) checkers are added to the grid from the
white bar above by pressing above the column we want to add the new checker to
as a black outline box appears when hovering to add the checker.

![Game](/readme/Game.jpg)

3. The minimax tree produced for applying this turn appears besides the game. It
shows each state with its parent state, the utility value, depth and to which column
the checker was added resulting in this state.

4. When the game is finished, the game shows a message presenting if you win, lose or
a Tie.

![EndGame](/readme/Lose.jpg)
