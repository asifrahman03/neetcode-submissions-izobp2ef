class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        final int ROWS = matrix.length;
        final int COLS = matrix[0].length;

        int begin = 0, end = ROWS-1;
        int saved = 0;
        while(begin <= end){
            int row = (begin+end)/2;
            if(target > matrix[row][COLS-1]){
                begin = row+1;
            }
            else if(target < matrix[row][0]){
                end = row-1;
            }
            else{
                saved = row;
                break;
            }
        }
        // if(!(begin <= end)){
        //     return false;
        // }
        int row2 = saved;
        int low = 0, high = COLS-1;
        while(low <= high){
            int index = (low+high)/2;
            if(target == matrix[row2][index]){
                return true;
            }
            else if(target > matrix[row2][index]){
                low = index+1;
            }
            else{
                high = index-1;
            }
        }
        return false;
    }
}
