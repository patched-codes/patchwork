package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Computes the sum of two numbers of type `T`, where `T` is a subclass of `Number`,
 * and returns the result as a `Double`.
 * 
 * @param a The first number to be added.
 * @param b The second number to be added.
 * @return The sum of `a` and `b` as a `Double`.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query against a given database connection and returns the results as a list of rows, 
 * where each row is represented as a list of column values.
 * 
 * @param db A Connection object representing the database connection.
 * @param query A String representing the SQL query to be executed.
 * @return A List of Lists, where each inner List contains the column values for a row 
 *         retrieved from the execution of the query, with each column value as an Any? 
 *         to accommodate null and non-null values.
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
 * Compares two items based on a specified key extracted from them using a key mapping function. 
 * Returns -1 if the key of item1 is less than the key of item2, 1 if it is greater, or 0 if they are equal.
 * 
 * @param keyMap A function that extracts a comparable key from an item of type T.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer indicating whether the key from item1 is less than, equal to, or greater than the key from item2.
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
 * @param length The length of the desired random string.
 * @return A string containing random alphabets of the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}