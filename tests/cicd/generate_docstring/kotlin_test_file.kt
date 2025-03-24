package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Calculates the sum of two numbers and returns the result as a Double.
 * 
 * @param a The first number of generic type T which extends Number.
 * @param b The second number of generic type T which extends Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a given SQL query on the provided database connection and retrieves the results.
 * The results are returned as a list of lists, where each inner list represents a row of the result set.
 * 
 * @param db The database connection to be used for executing the query.
 * @param query The SQL query to be executed.
 * @return A list of rows, where each row is represented as a list of objects. 
 *         Each object corresponds to a column value in the result set.
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
 * Compares two items using a specified key extraction function and returns an integer result.
 *
 * This method takes a function, `keyMap`, which extracts a key of a comparable type from
 * the items to be compared (`item1` and `item2`). It returns -1, 0, or 1 depending on whether
 * the key from `item1` is less than, equal to, or greater than the key from `item2`.
 * 
 * @param keyMap A function that takes an item of type T and returns a key of type R, 
 *               where R implements Comparable.
 * @param item1 The first item of type T to be compared.
 * @param item2 The second item of type T to be compared.
 * @return An integer representing the comparison result: 
 *         -1 if `item1` is less than `item2`, 
 *          0 if they are equal, 
 *          1 if `item1` is greater than `item2`.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabetic characters of a specified length.
 * 
 * @param length The desired length of the generated string. Must be a non-negative integer.
 * @return A string consisting of random uppercase and lowercase alphabetic characters.
 */

fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}