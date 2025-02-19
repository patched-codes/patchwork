package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Calculates the sum of two numbers and returns the result as a Double.
 * The input numbers can be of any type that extends from Number.
 * 
 * @param a The first number to be added. It must extend from Number.
 * @param b The second number to be added. It must extend from Number.
 * @return The sum of `a` and `b`, converted to a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the provided SQLite database connection and returns the results.
 * 
 * This function takes a database connection and a SQL query string, executes the query,
 * and retrieves the results. The results are returned as a list of lists, where each
 * inner list represents a row from the query result and contains objects of the columns.
 * 
 * @param db The database connection to be used for executing the query.
 * @param query The SQL query string to be executed.
 * @return A list of lists containing the query results, where each inner list represents
 *         a row and each element is a column value.
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
 * Compares two items based on a key extracted from each item using a key mapping function.
 * The function returns an integer indicating the order of the two items.
 * 
 * @param keyMap A function that extracts a comparable key from the items of type T.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer: -1 if item1's key is less than item2's key, 1 if item1's key is greater than item2's key,
 *         and 0 if both keys are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabets with a specified length.
 * 
 * @param length The desired length of the output string, comprised of random alphabets.
 * @return A string containing random alphabets (both uppercase and lowercase) of the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}