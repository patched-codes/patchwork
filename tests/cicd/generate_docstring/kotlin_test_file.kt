package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Computes the sum of two numbers, converting them to `Double` type before performing addition.
 *
 * @param a The first number to be added, constrained to types that implement `Number`.
 * @param b The second number to be added, constrained to types that implement `Number`.
 * @return The sum of `a` and `b` as a `Double`.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a given SQL query on the provided database connection and returns the result as a list of rows.
 * Each row is represented as a list of column values.
 * 
 * @param db Database connection object to execute the query on.
 * @param query SQL query to be executed.
 * @return List of rows, each represented as a list of column values, or an empty list if no results.
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
 * Compares two items based on the provided key mapping function and returns an integer 
 * indicating the relative order of the items as follows:
 * - Returns -1 if item1 is less than item2.
 * - Returns 1 if item1 is greater than item2.
 * - Returns 0 if item1 is equal to item2.
 *
 * @param keyMap A function that extracts a comparable key from an item.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer representing the comparison result: -1, 0, or 1.
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
 * The generated string comprises a mix of uppercase and lowercase letters.
 * 
 * @param length The length of the random string to be generated.
 * @return A randomly generated string made up of alphabets.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}