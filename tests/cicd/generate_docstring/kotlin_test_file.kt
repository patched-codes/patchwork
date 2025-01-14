package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of type extending Number and returns the result as Double.
 * 
 * @param a The first number to be added.
 * @param b The second number to be added.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a given SQL query on the provided database connection and returns the result set as a list of rows.
 * Each row is represented as a list containing column values, with `null` for any SQL NULL values.
 * 
 * @param db The database connection to use for executing the query.
 * @param query The SQL query string to execute against the database.
 * @return A list of lists where each inner list represents a row from the result set, containing the column values.
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
 * Compares two items based on a key extracted from each item using a provided mapping function.
 * The comparison is done by applying the given `keyMap` function to each item to extract a
 * comparable key, then comparing these keys.
 *
 * @param keyMap A function that takes an item of type `T` and returns a comparable key of type `R`.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer that is negative if `item1` is less than `item2`, positive if `item1` is greater
 *         than `item2`, and zero if they are equal.
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
 * The string will contain both lowercase and uppercase English letters.
 * 
 * @param length The length of the random string to be generated.
 * @return A random string composed of lowercase and uppercase alphabets with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}