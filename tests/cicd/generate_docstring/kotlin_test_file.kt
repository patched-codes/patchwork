package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Calculates the sum of two numbers with a generic numeric type.
 * Converts both input parameters to Double before performing addition.
 *
 * @param a First numeric parameter of type T which extends Number.
 * @param b Second numeric parameter of type T which extends Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the provided database connection and returns the query results as a list of lists. 
 * Each inner list represents a row from the result set, with each object in the list representing a column value.
 * 
 * @param db The database connection on which the SQL query will be executed.
 * @param query The SQL query string to be executed.
 * @return A list of lists where each inner list contains objects that represent values of a row from the query result.
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
 * Compares two items of type T using a key mapping function to determine their order based on the Comparable implementation of the key.
 * The function returns -1 if the key of the first item is less than the key of the second item, 1 if greater, or 0 if they are equal.
 * 
 * @param keyMap A function that maps an item of type T to a Comparable key of type R, which will be used for comparison.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer representing the comparison result: -1 if item1 is less than item2, 1 if item1 is greater than item2, or 0 if they are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string composed of alphabetic characters.
 * The resultant string consists of both uppercase and lowercase letters.
 *
 * @param length The desired length of the random string to be generated.
 * @return A random string of alphabetic characters with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}