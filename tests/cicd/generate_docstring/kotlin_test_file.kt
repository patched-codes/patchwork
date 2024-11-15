package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of a generic numeric type and returns their sum as a Double.
 * 
 * @param a The first number of a generic numeric type.
 * @param b The second number of a generic numeric type.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query using the provided database connection and returns the results as a list of rows,
 * with each row represented as a list of column values.
 * 
 * @param db The database connection to use for executing the query.
 * @param query The SQL query to execute.
 * @return A list of rows, each row is a list containing the column values retrieved from the query result set.
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
 * Compares two items based on a given key mapping function. The key mapping function 
 * maps each item to a comparable object, which is then used for comparison.
 * 
 * @param keyMap A function that maps an item of type T to a comparable type R.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer representing the comparison result: 
 *         -1 if the key of item1 is less than the key of item2,
 *         1 if the key of item1 is greater than the key of item2,
 *         0 if both keys are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string consisting of alphabetic characters (both lowercase and uppercase).
 *
 * @param length The desired length of the generated string.
 * @return A random string of the specified length, composed of characters from 'a' to 'z' and 'A' to 'Z'.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}