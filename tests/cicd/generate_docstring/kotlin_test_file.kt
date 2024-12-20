package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Computes the sum of two numbers, converting them to doubles first.
 * 
 * @param a First number of generic type T which must be a subclass of Number.
 * @param b Second number of generic type T which must be a subclass of Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes the given SQL query on the provided database connection and returns the results as a list of rows.
 * Each row is represented as a list of column values, where each column value is of type Any?.
 * 
 * @param db The database connection object to be used for executing the query.
 * @param query The SQL query string to be executed.
 * @return A list of rows, where each row is a list of column values obtained from the query execution.
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
 * Compares two items based on the result of applying a given key mapping function to each.
 *
 * This function takes a key-mapping function and two items of a generic type T,
 * then applies the key-mapping function to each item to obtain values of type R.
 * It returns an integer indicating whether the first item's key is less than,
 * greater than, or equal to the second item's key.
 * 
 * @param keyMap A function that takes an item of type T and returns a comparable key of type R.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer: -1 if the first item's key is less than the second item's key,
 *         1 if the first item's key is greater than the second item's key,
 *         or 0 if both keys are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string composed of alphabetic characters (both uppercase and lowercase) with the specified length.
 * 
 * @param length The length of the random string to be generated.
 * @return A string consisting of random alphabetic characters.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}