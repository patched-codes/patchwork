package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Calculates the sum of two numbers and returns the result as a Double.
 * 
 * @param a The first number to be summed. Must be a subtype of Number.
 * @param b The second number to be summed. Must be a subtype of Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a given SQL query on the provided database connection and returns the result as a list of lists.
 * Each inner list represents a row with its columns as elements.
 * 
 * @param db The database connection on which the query will be executed.
 * @param query The SQL query to be executed.
 * @return A list of lists where each inner list represents a row from the query result, 
 *         and each element in the inner list corresponds to a column value.
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
 * Compares two items using a key-mapping function which extracts a comparable key from each item.
 * Returns -1, 0, or 1 if the key for the first item is less than, equal to, or greater than the key for the second item, respectively.
 * 
 * @param keyMap A function that maps the items of type T to a comparable key of type R.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer value representing the comparison result: -1 if the first item is less than the second, 0 if they are equal, and 1 if the first item is greater.
 */

fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string consisting of uppercase and lowercase alphabets.
 * 
 * @param length The length of the random string to generate.
 * @return A string containing randomly selected alphabets of the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}