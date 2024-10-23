package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of the same type and returns the result as a Double.
 * 
 * @param a The first number to be added
 * @param b The second number to be added
 * @return The sum of a and b as a Double
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQLite query on the given database connection and returns the results as a list of lists.
 * 
 * @param db The database connection to execute the query on
 * @param query The SQL query string to execute
 * @return A list of lists representing the query results, where each inner list represents a row and contains column values as Any? objects
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
 * Compares two items of type T based on a key extracted by the provided function.
 * 
 * @param keyMap A function that extracts a comparable key of type R from an item of type T
 * @param item1 The first item to compare
 * @param item2 The second item to compare
 * @return An integer value: -1 if item1 < item2, 1 if item1 > item2, 0 if item1 == item2
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
 * 
 * @param length The desired length of the random string
 * @return A string containing random alphabets (both uppercase and lowercase) of the specified length
 */

fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}