
In Wanderer Project I try to build a hero based walking on tiles and killing monsters.

The hero is controlled in a maze using the keyboard. Heroes and monsters have levels and stats depending on their levels. The goal is reach the highest level by killing the monsters holding the keys to the next level.

1-Resource Class: What I am trying to do in Resource class is loading the photos that we need during the whole program.

2-Game: In game tab we want to run the game. In this part with Tkinter, I try to draw a box.

3-Grid: In this part, we want to create a 10* 10-page size using two loops then try to check each part, I mean with checking X and Y, if any of them was player replaced it with the player, if it was monster replaced with the monster, and if it was wall replaced with a wall. In the end, if it was non of them replaced with the floor. It also checks if the player and one of the monsters are in the same tile if they are battle forms.

4-Block: In Block class, I create a floor and wall.

5-Player: In this part, the player should be able to move the hero by using their arrow keys. It calculates HP, DP, and SP for Hero. If the hero kills a monster it stats increase.

6-Monster: In Monsters Class we create some monsters and then I check if the monster is not spawned in a wall or another monster. In Monster class also create a Monster that can be a skeleton or a boss. Monsters also have stats that depend on their levels. Monsters move every two turns.

7-Battle: If it's the player’s turn, the player is the attacker otherwise monster is the attacker. When the player hits space the attacker attack defender and then it strikes back. This continues until one of the characters dies.
