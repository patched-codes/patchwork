package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numeric values of the generic type that extends Number and returns their sum as a Double.
 * 
 * @param a The first numeric value.
 * @param b The second numeric value.
 * @return The sum of the two numbers converted to a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the provided database connection and returns the result as a list of rows, 
 * where each row is a list of column values.
 * 
 * @param db The database connection on which the query is to be executed.
 * @param query The SQL query string to be executed.
 * @return A list of rows retrieved by the query, where each row is a list of objects representing column values.
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
 * Compares two items of type T based on a key extracted by `keyMap` and returns an integer
 * indicating the order of these items. The comparison is done based on the natural ordering 
 * of the extracted key which should be of a type that implements the Comparable interface.
 * 
 * @param keyMap a function that extracts a Comparable key from an item
 * @param item1 the first item to compare
 * @param item2 the second item to compare
 * @return -1 if `item1` is less than `item2`, 1 if `item1` is greater than `item2`, and 0 if they are equal
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string composed of lowercase and uppercase alphabets.
 * 
 * @param length The length of the desired random string.
 * @return A string of the specified length containing random letters from a to z and A to Z.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}