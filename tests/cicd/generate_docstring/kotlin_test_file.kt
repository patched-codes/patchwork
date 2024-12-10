package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of a type that extends Number and returns the result as a Double.
 * 
 * @param a The first number to be added.
 * @param b The second number to be added.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the provided database connection and returns the result as a list of rows.
 * Each row is represented as a list of nullable objects corresponding to the columns in the result set.
 * 
 * @param db The database connection on which the query will be executed.
 * @param query The SQL query string to be executed on the database.
 * @return A list of rows, where each row is a list of nullable objects representing the column values of the result set.
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
 * Compares two items of type T based on a key extracted using the keyMap function.
 * The comparison is made on keys of type R, which must be comparable.
 *
 * @param keyMap A function that takes an item of type T and returns a key of type R.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer representing the comparison result: -1 if item1 comes before item2, 
 *         1 if item1 comes after item2, or 0 if they are considered equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string composed of alphabetic characters (both lower and upper case) of a specified length.
 * 
 * @param length The desired length of the resulting random string.
 * @return A random string consisting of alphabetic characters with the specified length.
 */

fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}