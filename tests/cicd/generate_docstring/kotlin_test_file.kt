package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Calculates the sum of two numbers that are subclasses of the Number type.
 * Converts both numbers to Double and returns their sum as a Double.
 * 
 * @param a The first number to be added.
 * @param b The second number to be added.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the provided database connection and returns the results as a list of rows.
 * Each row is represented as a list of column values. This function handles closing the 
 * statement and result set resources automatically.
 * 
 * @param db The active database connection on which the SQL query will be executed.
 * @param query The SQL query string to be executed on the database.
 * @return A list of rows with each row being a list of column values; returns an empty list if no results are found.
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
 * Compares two items using a keySelector function and returns an integer indicating their relative order.
 * The keySelector function determines the key to compare for each item.
 *
 * @param keyMap A function that accepts an item of type T and returns a comparable key of type R.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer: -1 if item1 is less than item2, 1 if item1 is greater than item2, or 0 if they are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabets containing both uppercase and lowercase characters.
 * 
 * @param length The desired length of the random string to be generated.
 * @return A random string of alphabets with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}