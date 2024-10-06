# Mo-Sike

## Question
Youâ€™ve uncovered the truth: it was a Trojan all along. Disguised as an integral part of the OASIS, the virus has been feeding vital information to IOI, undermining the system from within. Now, with its cover blown, you must track the data trails left behind by the Trojan before it can do any more damage. These data trails are in the form of a file containing a sequence of color names, each representing a piece of a larger mosaic. This mosaic forms a square grid, and when the squares are correctly arranged, they reveal a hidden image of a video game character. Your task is to decipher the relationship between the color list and the grid, reconstructing the image by placing each colored square in its correct position. The challenge lies in ensuring that the final arrangement reveals the intended character, with no visual discrepancies. Follow the breadcrumbs and uncover its next move. Flag format: OASIS{nameofcharacter_nameofgame} in lowercase.

Attachment: [text](../../../../../Pictures/colors.txt)

## Approach

So the question mentions that we  have a sequence of color names, and we need to reconstruct a square grid from it.

So first I found the number of lines  in the file, which is 3136.

From this I deciphered that the square  grid must be 56x56, since 56*56 = 3136.

After going through the contents of the file, I found that there were primarily 4 colours - White, Black, Red and Yellow.

We then wrote a code to basically make a 2-d matrix and put the first letter of each colour in their respective position based on the  line number. For example, if the first line is "White", then the first letter "W" and so on.

Now we just have to apply the required colours  to the grid in excel based on the box letter.

We did this on excel using the following steps

1) Select the grid and apply conditional formatting.
2) Click highlight cell rules and format the  cells based on the value of the cell and apply the respective colour.
3) Now we have the grid with all the required colours.

![alt text](<image.jpg>)

However, we weren't able to understand what this image was.

After a few minutes of brainstorming we used Google Lens to search for the image, and it opened a YouTube link.

https://youtu.be/TCKui8usQzE?si=lvRdRB_pLiMvwp6q

This video is about a glitch called MissingNo.
MissingNo. is an unofficial Pokémon species found in the video games Pokémon Red and Blue.

## Flag

**OASIS{missingno_pokemon}**

## Code

[Column_to_file.c](column_to_file.c)


