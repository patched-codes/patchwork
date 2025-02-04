package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Computes the sum of two numbers of type T, where T extends Number, and returns the result as a Double.
 * This function uses the `toDouble()` method to convert the input parameters to Double before summing them.
 * 
 * @param a The first number of type T to be added.
 * @param b The second number of type T to be added.
 * @return The sum of the two input numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes the given SQL query using the provided database connection and returns the results.
 *
 * This function takes a SQL query and a database connection, executes the query, and retrieves
 * the resulting data. It returns a list of lists representing rows and columns of the result set.
 * Each row is represented as a list of Any? (nullable Any) to accommodate different data types.
 *
 * @param db The database connection object used to execute the SQL query.
 * @param query A string representing the SQL query to be executed.
 * @return A list of rows, where each row is a list of column values. Each value is of type Any?, 
 *         accommodating nullable data types.
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
 * Compares two items based on a key extracted from them using the provided key mapping function.
 * 
 * @param keyMap A function that takes an item of type T and returns a comparable key of type R.
 * @param item1 The first item of type T to compare.
 * @param item2 The second item of type T to compare.
 * @return -1 if the key of item1 is less than the key of item2, 1 if it is greater, or 0 if they are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string composed of alphabetic characters (both lowercase and uppercase).
 * The string will have a length specified by the `length` parameter.
 * 
 * @param length An integer specifying the length of the generated random string.
 * @return A string containing randomly selected alphabetic characters.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}