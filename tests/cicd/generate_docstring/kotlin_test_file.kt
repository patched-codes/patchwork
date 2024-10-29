package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Computes the sum of two numbers, converted to type Double.
 * 
 * @param a The first number of type Number.
 * @param b The second number of type Number.
 * @return The sum of the two numbers as a Double.
 */

fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the provided database connection and returns the results.
 * 
 * @param db The database connection to execute the query on.
 * @param query The SQL query to be executed on the database.
 * @return A list of rows, where each row is a list of any objects representing the columns in the result set.
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
 * Compares two items of type T using a key mapping function and returns an integer to indicate their order.
 * 
 * @param keyMap A function that takes an item of type T and returns a Comparable type R, used for comparison.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer where -1 indicates item1 is less than item2, 1 indicates item1 is greater than item2, and 0 indicates both are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string composed of alphabetic characters (both uppercase and lowercase).
 * 
 * @param length The length of the string to be generated.
 * @return A random string of the specified length consisting of alphabetic characters.
 */

fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}