package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Calculates the sum of two numeric values.
 *
 * This function takes two input parameters of type `Number`, converts them to `Double`, 
 * and returns their sum as a `Double`.
 * 
 * @param a The first numeric value to be added.
 * @param b The second numeric value to be added.
 * @return The sum of `a` and `b` as a `Double`.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the provided database connection and returns the result as a list of rows,
 * where each row is represented as a list of column values.
 * 
 * @param db The database connection to use for executing the query.
 * @param query The SQL query to be executed.
 * @return A list of rows, where each row is a list of column values from the query result set. 
 *         Each value can be of any type, including null.
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
 * Compares two items based on a key extracted using the given key mapping function.
 * The key is required to be comparable, allowing for a typical comparison of less than,
 * greater than, or equal to.
 * 
 * @param keyMap Function that extracts a comparable key from the items.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer representing the comparison result:
 *         - A negative integer if the key of item1 is less than the key of item2.
 *         - Zero if the keys of both items are equal.
 *         - A positive integer if the key of item1 is greater than the key of item2.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabets of the specified length.
 * The generated string can include both uppercase and lowercase letters.
 * 
 * @param length The length of the resulting random alphabet string.
 * @return A random string consisting of uppercase and lowercase alphabetic characters.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}