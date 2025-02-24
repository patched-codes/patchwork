package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numeric values and returns the sum as a Double.
 * This function is generic and works with any type that inherits from Number.
 * 
 * @param a The first number to be added.
 * @param b The second number to be added.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a query on the given SQLite database connection and returns the result as a list of rows, 
 * where each row is represented as a list of objects corresponding to the column values.
 * 
 * @param db The SQLite database connection to execute the query on.
 * @param query The SQL query to be executed.
 * @return A list of rows, where each row is a list of column values represented as objects.
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
 * Compares two items based on a mapping function that extracts a comparable key from each item.
 * 
 * @param keyMap A function that maps an item of type T to a comparable key of type R.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer value: -1 if the key of item1 is less than the key of item2, 
 *         1 if the key of item1 is greater than the key of item2, 
 *         or 0 if the keys are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabets of the specified length. The 
 * alphabets can be either lowercase or uppercase.
 * 
 * @param length The length of the desired random alphabetic string.
 * @return A randomly generated string consisting of uppercase and lowercase alphabets.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}