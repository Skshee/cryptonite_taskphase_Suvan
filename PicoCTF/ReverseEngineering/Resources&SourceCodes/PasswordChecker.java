public class PasswordChecker {
    public static void main(String[] args) {
        // Arrays for character positions and their respective characters
        int[] positions = {0, 29, 4, 2, 23, 3, 17, 1, 7, 10, 5, 9, 11, 15, 8, 12, 20, 14, 6, 24, 18, 13, 19, 21, 16, 27, 30, 25, 22, 28, 26, 31};
        char[] characters = {'d', '3', 'r', '5', 'r', 'c', '4', '3', 'b', '_', '4', '3', 't', 'c', 'l', 'H', 'c', '_', 'm', '5', 'r', '3', '4', 'T', 'H', 'f', 'b', '_', '3', '6', 'f', '0'};

        // Simple bubble sort to order the positions and characters
        for (int i = 0; i < positions.length - 1; i++) {
            for (int j = 0; j < positions.length - i - 1; j++) {
                if (positions[j] > positions[j + 1]) {
                    
                    int tempPos = positions[j];
                    positions[j] = positions[j + 1];
                    positions[j + 1] = tempPos;

                    // Swapping characters along with the positions
                    char tempChar = characters[j];
                    characters[j] = characters[j + 1];
                    characters[j + 1] = tempChar;
                }
            }
        }

        for (int i = 0; i < positions.length; i++) {
            System.out.print(characters[i]);
        }
    }
}
