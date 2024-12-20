package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of a generic type that extends Number and returns the result as a Double.
 * 
 * @param a The first number to be added.
 * @param b The second number to be added.
 * @return The sum of a and b as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the given database connection and returns the result as a list of rows,
 * where each row is represented as a list of column values.
 * 
 * @param db The database connection on which the query is to be executed.
 * @param query The SQL query string to be executed.
 * @return A list of rows, with each row being a list of column values of type Any?. 
 *         The column values can be null.
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
 * Compares two items based on a key extracted from each item using the provided key mapping function.
 * This comparison returns an integer based on the natural ordering of the keys.
 *
 * @param keyMap A function that extracts a key of type R from an item of type T for comparison.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer: -1 if item1's key is less than item2's key, 1 if item1's key is greater than item2's key, and 0 if they are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabetic characters with the specified length.
 * The characters are chosen randomly from the set of uppercase and lowercase English letters.
 * 
 * @param length The length of the random string to be generated.
 * @return A randomly generated string consisting only of alphabetic characters.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}