# Roguelike

### Description
A very basic roguelike game

### Requirments

- [x] art
- [x] random room placement
- [x] combat system
- [x] wall collisions
- [x] animations

### Optional Additions
(Ranked in order of importance)
- [x] Good player ui
- [ ] More rooms
- [ ] boss room
- [ ] tile animations
- [ ] loot system with varied weapons
- [ ] chest mimics
- [ ] A better dungeon generation system
- [ ] Sound
- [ ] calculations to make the floor an wall pygame surfaces only as large as  
they need to be to conserve memory
- [ ] different characters
- [ ] Use wave function collapse for variation in the rooms


## Credits
Enemy and tile art thanks to [0x72](https://0x72.itch.io/dungeontileset-ii)  
UI thanks to [0x72](https://0x72.itch.io/dungeonui)
Restart Button thanks to https://pixelartmaker.com/art/2f1d67196a2b469  
Any math help is linked in the code


## Log

### Day 1 4/19
I spent most of the day trying to figure out how to best turn the generated dungeon into  
a dungeon that was drawn on the map, and had corridors between them. I was having trouple with the corridors being weirdly  
offset from the room.

### Day 2 4/20
added a map data json file for storing width and height information, and spent the rest of class talking about ap exams

### Day 3 4/24
I forgot my computer

### Day 4 4/25
My computer was broken

# Day 5 4/27
Began work on getting a proper enemy spawner working. My main issue with this was that the entire console program was crashing,
although I later found out that restarting my computer was enough to fix that (My best guess is the computer was running out of ram)

# Day 6 4/28
worked on getting the player offset so that they spawned in the center of the map, and also fixed the console crashing by restarting my computer

# Day 7 5/1
Got the player spawning in the middle of the dungeon, this took way longer than it should have

# Day 8 5/2
Added a basic game over screen and began working on buttons for a start screen and restart button, ran into a bug causing the button to only  
be able to be pressed once although I ended up fixing it. Also as of currently restarting causes the game to crash

# Day 9 5/3
Added a restart button as well as a player health ui that uses hearts instead of a number
