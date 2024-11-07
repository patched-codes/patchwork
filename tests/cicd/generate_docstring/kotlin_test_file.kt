package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of type Number and returns the result as a Double. This function is generic and can accept any type that extends Number.
 * 
 * @param a The first number to be added. Must be a subtype of Number.
 * @param b The second number to be added. Must be a subtype of Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a given SQL query on the provided database connection and returns the result as a list of rows,
 * where each row is represented as a list of column values.
 * 
 * @param db The database connection object used to execute the SQL query.
 * @param query The SQL query to be executed.
 * @return A list of rows resulting from the query execution, where each row is a list of column values. 
 *         Each column value can be of any type and may be null.
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
 * Compares two items using a specified key mapping function and returns an integer indication of their order.
 * 
 * @param keyMap a lambda function that maps an item of type T to a comparable key of type R
 * @param item1 the first item to compare
 * @param item2 the second item to compare
 * @return -1 if item1 is less than item2, 1 if item1 is greater than item2, or 0 if they are equal
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
 * The string is composed of both uppercase and lowercase letters.
 *
 * @param length The desired length of the random string to generate.
 * @return A string of random alphabetic characters of the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}