package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Computes the sum of two numeric values.
 * 
 * This function takes two parameters of a generic type `T` that extends the `Number` class,
 * converts them to `Double`, and returns their sum as a `Double`.
 * 
 * @param a The first numeric value to be added.
 * @param b The second numeric value to be added.
 * @return The sum of `a` and `b` as a `Double`.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the given database connection and returns the query result as a list of rows.
 * Each row is represented as a list of column values.
 * 
 * @param db The database connection on which the query is to be executed.
 * @param query The SQL query to be executed.
 * @return A list of lists, where each inner list represents a row from the query result with column values.
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
 * Compares two items based on a provided key mapping function and returns their relative ordering.
 * 
 * @param <T> The type of items being compared.
 * @param <R> The type of the key extracted by the keyMap function. Must be comparable.
 * @param keyMap A function that takes an item of type T and returns a key of type R for comparison.
 * @param item1 The first item of type T to be compared.
 * @param item2 The second item of type T to be compared.
 * @return An integer representing the comparison result: 
 *         -1 if item1 is less than item2, 
 *          1 if item1 is greater than item2,
 *          0 if both are equal.
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
 * The string includes both uppercase and lowercase letters.
 * 
 * @param length The desired length of the random string.
 * @return A random string of alphabets with the length specified by the input parameter.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}