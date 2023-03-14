# SPY game Telegram bot (in development)

## Short description
A telegram bot for spy game.
Want to play it with your friends? Message [@rpg_spy_bot](http://t.me/rpg_spy_bot) in telegram.

## Goal of the game
The game will have 2 types of players - spies and regular players.
 Non-spy players will be given the location information, while the goal of the spies is to guess the location before the game ends. 
The players' objective is to determine who the spies are.

## Rules 📌
1) When the game starts in a group chat, bot will periodically ask each player at a time 2 questions:
    - Who will they choose to answer their question.
    - What is their question.

2) Each question should be answered by the person it was directed to, and that person should then ask their own question. 

3) This cycle repeats until the estimated time is reached, then all players should leave their vote in the pole with player names.

4) The player with most votes gets eliminated (if a player was a spy, players win. Otherwise it's a spies' win).

## Commands
 - ```/help``` get a list of rules and game instructions

 - ```/new_game```
    - creates a new game inside a group (only one game can be created at a time).
    - gives all controls and permissions to the person who started the game.
    - asks for number of spies and time limit (in minutes, not more than 10).
    - waits for players to join.

 - ```/i_am_in``` adds a new player to a game.

 - ```/stop``` cancels the active game (must be a judge).

 - ```/start```:
    - starts the created game inside the group chat.
    - starts the timer.
    - randomly assigns spy roles to players based on the specified number of spies.
    - sends a message with the secret location to all non-spy players.
    - as time runs out, creates a poll with the name of each player.
    - ends the game, and reveals the winner(spies or players).
