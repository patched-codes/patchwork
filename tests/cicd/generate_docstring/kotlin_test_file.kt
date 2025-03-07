package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Computes the sum of two numbers and returns the result as a Double.
 * The numbers can be of any type that is a subclass of Number.
 * 
 * @param a The first number of type T to be added.
 * @param b The second number of type T to be added.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a given SQL query on a provided database connection and returns the result as a list of rows,
 * where each row is represented as a list of column values.
 * All objects are retrieved as instances of Object, and thus this method is type-agnostic.
 * The connection and statement resources are automatically closed after execution.
 * 
 * @param db The database connection on which the query is to be executed.
 * @param query The SQL query to be executed against the database.
 * @return A list of rows resulting from the query execution, with each row being a list of column values.
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
 * Compares two items of type T based on a specified comparable key extracted using the provided keyMap function.
 * Returns -1 if item1 is less than item2, 1 if item1 is greater than item2, or 0 if they are equal.
 * 
 * @param keyMap A function that defines a mapping from an element of type T to a comparable key of type R.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer indicating the order of item1 and item2: -1 if item1 < item2, 1 if item1 > item2, or 0 if they are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabets of a specified length.
 * 
 * The generated string contains a mix of lowercase and uppercase English alphabets.
 * 
 * @param length The desired length of the random string.
 * @return A random string composed of alphabetic characters with the specified length.
 */

fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}