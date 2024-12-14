// # calculate sum of the elements of the array.

import java.util.*;

public class SumOfEle {
    public static void main(String[] args) {
        int n = 5;
        int arr[] = { 2, 3, 3, 2, 1, 5 };
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += arr[i];
        }
        System.out.println("The sum of the elements of the array is " + sum);
    }

}
