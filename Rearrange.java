import java.util.Arrays;

public class Rearrange {

    public static void main(String args[]) {

        int arr[] = { 8, 7, 1, 6, 5, 9 };
        int n = arr.length;
        Arrays.sort(arr);
        for (int i = 0; i < n / 2; i++) {
            System.out.print(arr[i] + " ");
        }
        for (int i = n - 1; i >= n / 2; i--) {
            System.out.print(arr[i] + " ");
        }
    }
}


// Output: 1 5 6 9 8 7
// Time Complexity: O(nlogn) +O(n), O(nlogn) for sorting the array and O(n) for printing the elements. 
// Space Complexity: O(1).