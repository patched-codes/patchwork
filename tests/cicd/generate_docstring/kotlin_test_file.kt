package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of a numeric type and returns the result as a Double.
 * 
 * @param a The first number to add, must be of a type that extends Number.
 * @param b The second number to add, must be of a type that extends Number.
 * @return The sum of a and b, converted to a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on a given database connection and returns the results as a list of lists.
 * Each inner list represents a row of the result set, with each element being a column value.
 * 
 * @param db The database connection on which the query is executed.
 * @param query The SQL query to be executed.
 * @return A list of lists representing the result set, where each inner list is a row and each element in the row is a column value.
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
 * Compares two items based on a key extracted from each item using the given keyMap function.
 * The key is expected to be comparable. This function returns an integer indicating the order of the items:
 * -1 if the first item is less than the second, 1 if the first item is greater, and 0 if they are equal.
 * 
 * @param keyMap A function that extracts a comparable key from a given item of type T.
 * @param item1 The first item of type T to be compared.
 * @param item2 The second item of type T to be compared.
 * @return An integer indicating the order: -1 if item1 < item2, 1 if item1 > item2, or 0 if item1 == item2.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabets in both lowercase and uppercase.
 * 
 * @param length The desired length of the generated string.
 * @return A string consisting of random alphabets with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}