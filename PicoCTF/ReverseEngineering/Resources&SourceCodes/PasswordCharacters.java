import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class PasswordCharacters {
    public static void main(String[] args) {
        ArrayList<CharPosition> charPositions = new ArrayList<>();

        // Adding each character condition with its respective index
        charPositions.add(new CharPosition(0, 'd'));
        charPositions.add(new CharPosition(29, '3'));
        charPositions.add(new CharPosition(4, 'r'));
        charPositions.add(new CharPosition(2, '5'));
        charPositions.add(new CharPosition(23, 'r'));
        charPositions.add(new CharPosition(3, 'c'));
        charPositions.add(new CharPosition(17, '4'));
        charPositions.add(new CharPosition(1, '3'));
        charPositions.add(new CharPosition(7, 'b'));
        charPositions.add(new CharPosition(10, '_'));
        charPositions.add(new CharPosition(5, '4'));
        charPositions.add(new CharPosition(9, '3'));
        charPositions.add(new CharPosition(11, 't'));
        charPositions.add(new CharPosition(15, 'c'));
        charPositions.add(new CharPosition(8, 'l'));
        charPositions.add(new CharPosition(12, 'H'));
        charPositions.add(new CharPosition(20, 'c'));
        charPositions.add(new CharPosition(14, '_'));
        charPositions.add(new CharPosition(6, 'm'));
        charPositions.add(new CharPosition(24, '5'));
        charPositions.add(new CharPosition(18, 'r'));
        charPositions.add(new CharPosition(13, '3'));
        charPositions.add(new CharPosition(19, '4'));
        charPositions.add(new CharPosition(21, 'T'));
        charPositions.add(new CharPosition(16, 'H'));
        charPositions.add(new CharPosition(27, 'f'));
        charPositions.add(new CharPosition(30, 'b'));
        charPositions.add(new CharPosition(25, '_'));
        charPositions.add(new CharPosition(22, '3'));
        charPositions.add(new CharPosition(28, '6'));
        charPositions.add(new CharPosition(26, 'f'));
        charPositions.add(new CharPosition(31, '0'));

        // Sorting based on the index
        Collections.sort(charPositions, Comparator.comparingInt(cp -> cp.index));

        // Printing the sorted character positions
        for (CharPosition cp : charPositions) {
            System.out.print(cp.character);
        }
    }
}

class CharPosition {
    int index;
    char character;

    CharPosition(int index, char character) {
        this.index = index;
        this.character = character;
    }
}
