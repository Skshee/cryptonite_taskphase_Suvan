# A Rocky Start

## Question

The game has finally loaded! Yet, as you start to play, a sinking realization dawns: youâ€™ve been led into a trap. The virus has ensnared you in a loop, wasting precious time. The game is rigged to stall your progress. To save OASIS, you must break free of this digital decoy and bypass the virusâ€™s stalling tactics. Sometimes, you need to overflow the memoryâ€™s expectations to find a way out. The game is broken; you can't shoot. However, only if you get a score of 100 or more can you get the flag.

Attachment: [text](Asteroids.x86_64)

## Approach

When we opened the file, it loaded a Unity game. We had to enter a username to start the game. The game was about trying to escape an asteroid belt.

However when we played the game, we noticed there wasn't any change in the scoreboard.

Now, the question mentioned that we needed to overflow the memory's expectations.Hence we decided to give a very long username  to see if it would change anything. This worked and we were able to get the flag.

## Flag

**OASIS{D0DG3_4LL_TH3_R0CK5_0R_N07}**
