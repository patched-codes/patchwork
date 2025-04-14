package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Sums two numbers that are subclasses of the Number class and returns the result as a Double.
 * 
 * @param a The first number of type T to be added.
 * @param b The second number of type T to be added.
 * @return The sum of the two numbers as a Double.
 */

fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a given SQL query on the provided database connection and returns the results.
 *
 * @param db The database connection object to use for executing the query.
 * @param query The SQL query to be executed.
 * @return A list of lists, where each inner list represents a row of the result set, 
 *         and each element in the row corresponds to a column value.
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
 * Compares two items based on a key determined by the provided key mapping function.
 * The key mapping function converts each item to a comparable result upon which the comparison is based.
 * 
 * @param keyMap A function that maps an item of type T to a Comparable key of type R.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer representing the result of the comparison: -1 if item1 is less than item2,
 *         1 if item1 is greater than item2, or 0 if they are equal according to the key mapping.
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
 * @param length The length of the desired random string.
 * @return A random string of alphabets with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}