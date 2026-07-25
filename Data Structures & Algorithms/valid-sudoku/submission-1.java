class Solution {
    public boolean isValidSudoku(char[][] board) {
        //add each row to a hashmap and chdck for duplicwrs for all rows
        for (char[] row : board) {
            HashSet<Character> hashRow = new HashSet<Character>();
            for (char num : row) {
                if (hashRow.contains(num)) { 
                    return false;
                }
                if (num != '.') {
                hashRow.add(num);
            }}
        }
        //add each column to hashset wndh check sduplicsts
        for (int col = 0; col < 9; col++) {
            HashSet<Character> hashCol = new HashSet<Character>();
            for (int row = 0; row < 9; row++) {
                if (hashCol.contains(board[row][col])) {
                    return false;
                }
                if (board[row][col] != '.') {
                    hashCol.add(board[row][col]);

                }
            }
        }
        //check for sub array
        // for rows 1-3 
        // for col 1-3
        // create set and add row 
        for (int row = 0; row < 3; row ++) {
            for (int col = 0; col < 3; col++) {
                HashSet<Character> subBoard = new HashSet<Character>();
                for (int subrow = 0; subrow < 3; subrow++) {
                    for (int subcol = 0; subcol < 3; subcol++) {
                        if (subBoard.contains(board[row * 3 + subrow][col * 3 + subcol])) {
                            return false;
                        }
                        if (board[row * 3 + subrow][col * 3 + subcol] != '.') {
                            subBoard.add(board[row * 3 + subrow][col * 3 + subcol]);
                        }
                    }
                }
            }
        }
        
        
        
        return true;
    }
}
