package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of a generic type that extends Number and returns the result as a Double.
 * 
 * @param a The first number to be added.
 * @param b The second number to be added.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes the given SQL query using the provided database connection and returns the results.
 * 
 * @param db The database connection to be used for executing the query.
 * @param query The SQL query string to execute.
 * @return A list of lists containing the query results, where each inner list represents a row and each element in the inner list represents a column value.
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
 * Compares two items based on a key extracted from each item using the provided key mapping function.
 * The comparison is done in terms of natural ordering of the extracted keys.
 *
 * @param keyMap A function that extracts the key used for comparison from an item.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer value: -1 if the key of item1 is less than the key of item2, 1 if the key of item1 is greater than the key of item2, 
 *         or 0 if both keys are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string consisting of uppercase and lowercase alphabets with the specified length.
 * 
 * @param length The number of characters in the resulting string.
 * @return A string containing random alphabets of the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}