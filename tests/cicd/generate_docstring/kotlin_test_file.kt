package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Computes the sum of two numbers, converting them to double type for calculation.
 * This function is generic and can take any type of Number as arguments.
 *
 * @param a The first number to be added. It must be a subtype of Number.
 * @param b The second number to be added. It must also be a subtype of Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the provided database connection and returns the results as a list of rows.
 * Each row is represented as a list of column values, where each value can be of any type or null.
 * 
 * @param db The database connection on which the SQL query will be executed.
 * @param query The SQL query string to be executed.
 * @return A list of rows, where each row is a list of column values retrieved from the database.
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
 * Compares two items based on a key extracted by a given key mapping function and returns an integer 
 * to indicate their order. The items are compared using their comparable keys.
 * 
 * @param <T> The type of items being compared.
 * @param <R> The type of the key which is used for comparison, must be comparable.
 * @param keyMap A function that extracts a comparable key from the item.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer value: -1 if the first item's key is less than the second's, 1 if greater, or 0 if equal.
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
 * 
 * @param length The desired length of the resulting random string.
 * @return A string containing random alphabetic characters (both lowercase and uppercase) of specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}