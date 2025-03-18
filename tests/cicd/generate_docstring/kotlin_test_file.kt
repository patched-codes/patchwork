package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Computes the sum of two numbers and returns it as a Double.
 * 
 * This generic function takes two parameters of a number type and converts 
 * them into Double, then returns the sum. The function is restricted to 
 * types that inherit from Number. Suitable for addition of numeric types 
 * such as Int, Float, etc.
 * 
 * @param a The first number to be added.
 * @param b The second number to be added.
 * @return The sum of 'a' and 'b' as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a given SQL query on a database connection and returns the results as a list of rows, 
 * where each row is represented as a list of column values.
 * 
 * @param db The database connection on which the query will be executed.
 * @param query The SQL query to be executed.
 * @return A list of rows, where each row is a list of column values extracted from the result set.
 */
fun sqlite(db: Connection, query: String): List<List<Any?>> {
    db.createStatement().use { statement ->
        statement.executeQuery(query).use { resultSet ->
            val results = mutableListOf<List<Any?>>()
            val columnCount = resultSet.metaData.columnCount

            while (resultSet.next()) {
                val row = mutableListOf<Any?>()
                for (i in 1..columnCount) {
                    row.add(resultSet.getObject(i))
                }
                results.add(row)
            }
            return results
        }
    }
}


/**
 * Compares two items by their keys obtained from the specified mapping function and returns an integer 
 * indicating their order based on natural ordering.
 * 
 * @param keyMap A mapping function that returns a comparable key of type R for a given item of type T.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer indicating the comparison result: -1 if the key of item1 is less than the key of item2, 
 * 1 if the key of item1 is greater than the key of item2, and 0 if both keys are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabets of the specified length.
 * The string includes both uppercase and lowercase letters.
 * 
 * @param length The length of the random string to generate.
 * @return A string containing randomly selected alphabets.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}