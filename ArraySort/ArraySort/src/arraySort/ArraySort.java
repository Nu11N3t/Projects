package arraySort;

import java.util.Scanner;

public class ArraySort {

	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		System.out.println("How long do you want the array?");
		int arrayLength = input.nextInt();
		
		int[] unsortedArray = new int[arrayLength];
		
		for (int i = 0; i < unsortedArray.length; i++) {
			
			unsortedArray[i] = (int)(Math.random() * 3 )- 1;
			
		}
		
		System.out.print("Unstorted: ");
		PrintArray(unsortedArray);
		System.out.print("Sorted array: ");
		int[] sortedAray = Sort(unsortedArray);
		PrintArray(sortedAray);
		
	}
	
	public static void PrintArray(int[] printedArray) {
		
		for (int i = 0; i < printedArray.length; i++) {
		System.out.print(printedArray[i] + " ");
		
	}
		
		System.out.println();
		
	}
	
	public static int[] Sort(int[] sortingArray) {
		
		int temp;
		
		for (int i = 0; i < sortingArray.length - 1; i++ ) {
			
			for (int j = i + 1; j < sortingArray.length; j++ ) {
				
				if (sortingArray[j] < sortingArray[i]) {
					
					temp = sortingArray[i];
					sortingArray[i] = sortingArray[j];
					sortingArray[j] = temp;
					
				}
				
				
			}
			
			
		}
		
		return sortingArray;
		
	}
	
}
