public class Solution {

    public List<int[]> pacificAtlantic(int[][] matrix) {
        int m = matrix.length;
        if(m == 0) {
            return new ArrayList<int[]>();
        }
        int n = matrix[0].length;
        boolean[][] pacific = new boolean[m][n];
        boolean[][] atlantic = new boolean[m][n];
        // Step 1. Find all solutions for pacific
        for(int i = 0; i < n; i++) {
            pacific[0][i] = true;
        }
        for(int i = 0; i < m; i++) {
            pacific[i][0] = true;
        }
        for(int i = 1; i < m; i++) {
            for(int j = 1; j < n; j++) {
                // Check up
                if(pacific[i-1][j] && matrix[i][j] >= matrix[i-1][j]) {
                    pacific[i][j] = true;
                }
                // Check left
                if(pacific[i][j-1] && matrix[i][j] >= matrix[i][j-1]) {
                    pacific[i][j] = true;
                }
            }
        }
        for(int i = m-1; i >= 0; i--) {
            for(int j = n-1; j >= 0; j--) {
                // Check down
                if(i+1 < m && pacific[i+1][j] && matrix[i][j] >= matrix[i+1][j]) {
                    pacific[i][j] = true;
                }
                // Check right
                if(j+1 < n && pacific[i][j+1] && matrix[i][j] >= matrix[i][j+1]) {
                    pacific[i][j] = true;
                }
            }
        }
        // Step 2. Find all solutions for atlantic
        for(int i = 0; i < n; i++) {
            atlantic[m-1][i] = true;
        }
        for(int i = 0; i < m; i++) {
            atlantic[i][n-1] = true;
        }
        for(int i = m-2; i >= 0; i--) {
            for(int j = n-2; j >= 0; j--) {
                // Check down
                if(atlantic[i+1][j] && matrix[i][j] >= matrix[i+1][j]) {
                    atlantic[i][j] = true;
                }
                // Check right
                if(atlantic[i][j+1] && matrix[i][j] >= matrix[i][j+1]) {
                    atlantic[i][j] = true;
                }
            }
        }
        for(int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // Check up
                if(i-1 >= 0 && atlantic[i-1][j] && matrix[i][j] >= matrix[i-1][j]) {
                    atlantic[i][j] = true;
                }
                // Check left
                if(j-1 >= 0 && atlantic[i][j-1] && matrix[i][j] >= matrix[i][j-1]) {
                    atlantic[i][j] = true;
                }
            }
        }
        System.out.println("Pacific");
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                System.out.print(pacific[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("Atlantic");
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                System.out.print(atlantic[i][j] + " ");
            }
            System.out.println();
        }
        ArrayList<int[]> result = new ArrayList<int[]>();
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(pacific[i][j] && atlantic[i][j]) {
                    int[] pair = new int[2];
                    pair[0] = i;
                    pair[1] = j;
                    result.add(pair);
                }
            }
        }
        return result;
    }
}