package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numeric values of type T and returns the result as a Double.
 * 
 * @param a The first numeric value of type T.
 * @param b The second numeric value of type T.
 * @return The summation of a and b converted to a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the provided database connection and returns the result as a list of rows, where each row is represented as a list of column values.
 * 
 * @param db The database connection used to execute the SQL query.
 * @param query The SQL query to be executed on the database.
 * @return A list of rows resulting from the query execution, where each row is a list containing the column values.
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
 * Compares two items based on the results of a given key mapping function.
 * The function maps each item to a comparable key, and the items are compared 
 * based on these keys.
 * 
 * @param keyMap a function that maps an item of type T to a comparable key of type R
 * @param item1 the first item to be compared
 * @param item2 the second item to be compared
 * @return -1 if the key of item1 is less than the key of item2, 1 if the key 
 *         of item1 is greater than the key of item2, or 0 if the keys are equal
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string composed of uppercase and lowercase alphabets with the specified length.
 * 
 * @param length The length of the random alphabetic string to generate.
 * @return A string of random alphabets with the provided length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}