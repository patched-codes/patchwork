package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Calculates the sum of two numbers and returns the result as a Double.
 *
 * @param a The first number to be added, must be a type that is a subclass of Number.
 * @param b The second number to be added, must be a type that is a subclass of Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on a SQLite database and returns the results.
 * 
 * This function utilizes a given connection to execute a provided SQL query string,
 * iterating over the result set to extract and return the data as a list of rows,
 * where each row is represented as a list of objects.
 *
 * @param db The database connection to be used for executing the SQL query.
 * @param query The SQL query string to be executed.
 * @return A list of rows, where each row is a list of column data, represented as objects.
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
 * Compares two items using a specified key mapping function and returns an integer indicating their order.
 * 
 * @param keyMap A function that transforms items of type T into a comparable type R.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return -1 if item1 is less than item2, 1 if item1 is greater than item2, and 0 if they are equal.
 */

fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string consisting of alphabetic characters.
 * The string contains both uppercase and lowercase letters.
 * 
 * @param length The length of the desired random string.
 * @return A randomly generated string of alphabetic characters of the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}