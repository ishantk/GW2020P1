cpp_program="""
#include <iostream>
using namespace std;


void hello(){
    cout<<"Hello World";
}

int main() {
	hello();
	return 0;
}
"""

java_program="""
import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class MyApp
{
	public static void main (String[] args) throws java.lang.Exception
	{
		System.out.println("Hello World");
	}
}
"""

print(cpp_program)
print(java_program)

file1 = open("/Users/ishantkumar/Downloads/MyApp.cpp", "w")
file2 = open("/Users/ishantkumar/Downloads/MyApp.java", "w")

file1.write(cpp_program)
file2.write(java_program)

file1.close()
file2.close()

print("Programs Generated")

# Assignment
# create a menu driven program to generate a hello world program
# in the program hello world must be printed from a user-defined function
# Create Hello World Programs for below Languages

# 1. Dart
# 2. Go
# 3. Kotlin
# 4. Scala
# 5. Javacript/TypeScript
