package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of any numeric type and returns the result as a Double.
 * 
 * @param a The first number to add, extends the Number class.
 * @param b The second number to add, extends the Number class.
 * @return The sum of the two numbers as a Double.
 */

fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the given database connection and retrieves the results as a list of rows.
 * Each row is represented as a list of column values.
 * 
 * @param db A Connection object representing the active database connection.
 * @param query A String containing the SQL query to be executed.
 * @return A List of Lists, where each inner List contains column values from a row in the result set.
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
 * Compares two items of type T based on a key extracted by a key mapping function.
 * The items are compared using the natural ordering of the keys.
 * 
 * @param <T> The type of items being compared.
 * @param <R> The type of the key extracted from the items. The type must be Comparable.
 * @param keyMap A function that extracts a Comparable key from each item of type T.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return -1 if the key of item1 is less than the key of item2, 1 if the key of item1 is greater than the key of item2,
 *         and 0 if the keys are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabets with a specified length.
 * The string will be composed of both uppercase and lowercase English letters.
 * 
 * @param length The desired length of the random string to generate.
 * @return A randomly generated string consisting of uppercase and lowercase alphabets.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}