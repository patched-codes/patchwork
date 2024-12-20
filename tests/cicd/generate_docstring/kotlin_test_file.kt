package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Computes the sum of two numbers, converting each to a Double.
 * 
 * @param a The first number to be added.
 * @param b The second number to be added.
 * @return The sum of the two numbers as a Double.
 */

fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the given database connection and returns the result as a list of rows.
 * Each row is represented as a list of column values.
 * 
 * @param db The database connection to be used for executing the query.
 * @param query The SQL query to be executed.
 * @return A list of rows, where each row is a list of column values as Any? objects.
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
 * Compares two items using a key function and returns an integer based on their comparison.
 * 
 * @param keyMap A function that extracts the key to compare from the given items.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer representing the order of the items. Returns -1 if the key of item1 is less than item2, 
 *         1 if the key of item1 is greater than item2, and 0 if they're equal.
 */

fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabets with the specified length.
 * The string consists of both uppercase and lowercase English letters.
 * 
 * @param length The desired length of the random alphabet string.
 * @return A string of random alphabets with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}