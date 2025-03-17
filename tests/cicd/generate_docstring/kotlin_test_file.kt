package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of any type that extends Number and returns the result as a Double.
 * 
 * @param a The first number to add.
 * @param b The second number to add.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a given SQL query on the provided database connection and returns the result as a list of rows.
 * Each row is represented as a list of objects, corresponding to the columns of the result set.
 * 
 * @param db The database connection on which the query is to be executed.
 * @param query A SQL query string to be executed.
 * @return A list of rows, where each row is a list of objects representing the data in each column.
 *         Returns an empty list if there are no results.
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
 * Compares two items of type T based on a specified key extracted using the keyMap function. 
 * The key must be of a type that implements Comparable.
 * 
 * @param keyMap A function that takes an item of type T and returns a key of type R for comparison.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer result of the comparison: -1 if item1 is less than item2, 1 if item1 is greater than item2, or 0 if they are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabets, both uppercase and lowercase, of a specified length.
 * 
 * @param length The desired length of the resultant random string.
 * @return A string consisting of randomly selected uppercase and lowercase alphabet characters of the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}