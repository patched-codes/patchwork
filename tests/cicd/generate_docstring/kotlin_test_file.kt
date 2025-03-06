package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numeric values and returns the result as a Double.
 * 
 * This function takes two parameters of a numeric type (e.g., Int, Double, etc.)
 * and converts them to Double before performing the addition.
 * 
 * @param a First numeric value to be added.
 * @param b Second numeric value to be added.
 * @return The sum of `a` and `b` as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the provided database connection and returns the results as a list of rows, 
 * where each row is represented as a list of column values.
 * 
 * @param db The database connection to use for executing the query.
 * @param query The SQL query to execute.
 * @return A list of lists, where each inner list represents a row returned by the query, and each element is a column value.
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
 * Compares two items of type T based on a key extracted by the provided keyMap function.
 * The key extracted from each item is of type R, which must be Comparable.
 * 
 * @param keyMap A lambda function that extracts a comparable key of type R from an item of type T.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer result of the comparison: -1 if the key of item1 is less than the key of item2,
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
 * Generates a random string composed of alphabetic characters (both lowercase and uppercase) with a specified length.
 * 
 * @param length The length of the random string to generate.
 * @return A randomly generated string of the specified length containing only alphabetic characters.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}