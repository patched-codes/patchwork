// Java example to demonstrate how to use Test class methods

// Method `a_plus_b` example(s)
int sum = Test.a_plus_b(3, 5); // Expected output: 8
System.out.println("Sum of 3 and 5 is: " + sum);

// Custom comparator using a lambda function
int comparisonResult = Test.a_plus_b(x -> (Integer) x, 10, 20);
System.out.println("Comparison result of 10 and 20 is: " + comparisonResult);
