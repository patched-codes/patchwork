package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of type Number and returns the sum as a Double.
 * 
 * @param a The first number to be added, of any type that extends Number.
 * @param b The second number to be added, of any type that extends Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a given SQL query on the provided database connection and returns the result as a list of rows.
 * Each row is represented by a list of column values.
 * 
 * @param db The database connection used to execute the query.
 * @param query The SQL query to be executed.
 * @return A list of lists, where each inner list represents a row of the resulting query.
 *         Each element of the inner list corresponds to a column value, which can be of any type.
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
 * Compares two items based on a specified key and returns an integer indicating their order.
 * The comparison is done using the Comparable interface of the key type.
 * 
 * @param keyMap A function that extracts a comparable key from an item of type T.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return -1 if the key of item1 is less than the key of item2, 1 if the key of item1 is more than the key of item2, 
 *         or 0 if the keys are equal.
 */

fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string containing alphabets with the specified length.
 * The string is composed of both lowercase and uppercase letters.
 * 
 * @param length The length of the resulting random string.
 * @return A random string of alphabets with the specified length.
 */

fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}