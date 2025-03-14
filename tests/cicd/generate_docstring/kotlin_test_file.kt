package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of a generic type that extends Number and returns the result as a Double.
 * 
 * @param a The first number to add, of a generic type T that extends Number.
 * @param b The second number to add, of a generic type T that extends Number.
 * @return The sum of a and b as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on a given database connection and returns the result as a list of rows,
 * with each row represented as a list of column values.
 * 
 * @param db The database connection to use for executing the query.
 * @param query The SQL query to execute.
 * @return A list of rows, where each row is a list of column values. Each value can be of any type or null.
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
 * Compares two items based on a key extracted using the specified key mapping function.
 * Returns -1, 0, or 1 if the key of item1 is less than, equal to, or greater than the key of item2, respectively.
 * 
 * @param keyMap A function that extracts a comparable key from an item of type T.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer indicating the order of item1 and item2 based on their keys: 
 *         -1 if item1 < item2, 1 if item1 > item2, or 0 if item1 == item2.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string composed of alphabetic characters (both uppercase and lowercase).
 * 
 * @param length The desired length of the generated string.
 * @return A random string of the specified length containing only alphabetic characters.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}