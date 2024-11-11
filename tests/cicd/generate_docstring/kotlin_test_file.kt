package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Generic function to add two numbers of a type that extends Number and return the result as a Double.
 * 
 * @param a The first number to be added, of a type extending Number.
 * @param b The second number to be added, of a type extending Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the specified database connection and returns the result as a list of rows, 
 * with each row represented as a list of column values.
 * 
 * @param db The database connection on which the query will be executed.
 * @param query The SQL query string to be executed.
 * @return A list of lists, where each list represents a row of the result set and 
 *         contains the column values as objects. Returns an empty list if the query 
 *         produces no results.
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
 * Compares two items by applying a transformation function (keyMap) to both items 
 * and comparing the results of the transformation.
 * 
 * @param T The type of the items to compare.
 * @param R The type returned by the transformation function, which must be Comparable.
 * @param keyMap A function that transforms an item of type T to a comparable type R.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer result of the comparison: -1 if item1 is less than item2, 1 if item1
 * is greater than item2, and 0 if they are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string consisting of alphabetic characters (both lowercase and uppercase).
 * The length of the string is based on the input parameter.
 * 
 * @param length The length of the random string to be generated.
 * @return A string made up of random alphabetic characters with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}