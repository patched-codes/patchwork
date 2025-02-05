package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Calculates the sum of two numbers and returns the result as a Double.
 *
 * @param a First number, a generic type extending Number, to be added.
 * @param b Second number, a generic type extending Number, to be added.
 * @return The sum of the two numbers as a Double.
 */

fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the provided database connection and returns the results as a list of rows.
 * Each row is represented as a list of column values.
 * 
 * @param db The database connection to be used for executing the query.
 * @param query The SQL query string to be executed.
 * @return A list of lists, where each inner list represents a row of the query result, 
 *         with each item in the inner list corresponding to a column value in that row.
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
 * Compares two items of type T based on a comparable key retrieved by a key-mapping function.
 * The function evaluates which of the two items should be prioritized by the mapping to a comparable value.
 * 
 * @param keyMap A lambda function that maps an item of type T to a comparable value of type R.
 * @param item1 The first item of type T to be compared.
 * @param item2 The second item of type T to be compared.
 * @return Returns -1 if the first item's key is less than the second item's key, 
 * returns 1 if the first item's key is greater than the second item's key, 
 * and returns 0 if both keys are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabets with the specified length. The alphabets
 * are randomly chosen from upper and lower case English letters.
 * 
 * @param length The desired length of the generated string.
 * @return A random string composed of alphabetic characters of the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}