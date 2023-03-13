# SPY game Telegram bot (in development)

## Short description
A telegram bot for spy game.
Want to play with your friends? Message [@rpg_spy_bot](http://t.me/rpg_spy_bot) in telegram.

## Goal of the game
As soon as the game starts there will be 2 types of players (spies and players).
Every non-spy player will be given the information about location.
Goal of a spy is to guess the location untill the end of a game.
Goal of a player is to find out who is the spy.

## Rules 📌
1) As soon as the game starts in a group chat, bot should periodically ask 1 player at a time 2 things:
    - Who do you want to ask a question
    - Your question

2) Each time only the person who was asked the question should answer it, soon after the person who answered, should be next to ask a question.

3) This cycle repeats until the estimated time runs out, and then all players should leave their vote in the pole with player names.

4) The person who gets most votes gets eliminated (if a player was a spy, players win. Otherwise spies win and players loose).

## Commands
 - ```/help``` get a list of rules and game instructions

 - ```/new_game```
    - create a new game inside a group (not more than one)
    - gives all controls and permissions to the person who started
    - asks for number of imposters and time (in minutes, not more than 10)
    - waits for players to join

 - ```/i_am_in``` adds a new player to a game

 - ```/stop``` cancels the active game (must be a judge)

 - ```/start```:
    - starts the created game inside the group chat
    - starts the timer
    - randomly sets a spy role to players according to setted number of spies
    - sends a message with the secret location to all non-spy players
    - as time runs out, creates a poll with the name of each player
    - ends the game, and shows who own (spies or players)