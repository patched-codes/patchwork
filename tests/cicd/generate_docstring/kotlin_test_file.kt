package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of a type that extends Number and returns their sum as a Double.
 * 
 * @param a A number of type T which extends Number, representing the first term in the addition.
 * @param b A number of type T which extends Number, representing the second term in the addition.
 * @return The sum of a and b converted to a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes the given SQL query using the provided database connection and retrieves
 * the results as a list of rows, where each row is represented as a list of column values.
 * 
 * @param db The database connection to use for executing the query.
 * @param query The SQL query to execute.
 * @return A list of rows, with each row being a list of column values retrieved from the query result.
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
 * Compares two items based on a key extracted using a provided mapping function.
 * The key values are compared using their natural ordering defined by the Comparable interface.
 * 
 * @param <T> The type of the items to be compared.
 * @param <R> The type of the comparable key extracted from the items.
 * @param keyMap A lambda function that extracts a key of type R from an item of type T.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer representing the comparison result: -1 if the key of item1 is less than that of item2,
 *         1 if the key of item1 is greater than that of item2, or 0 if both keys are equal.
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
 * The string is composed of both uppercase and lowercase letters.
 * 
 * @param length The length of the random string to be generated.
 * @return A string of random alphabets of the given length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}