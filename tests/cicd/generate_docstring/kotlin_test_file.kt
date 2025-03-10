package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of a generic type that extends Number and returns the sum as a Double.
 * 
 * This method takes two parameters of the same type, which must be a subtype of Number,
 * converts them to Double, and returns their sum as a Double.
 *
 * @param a The first number to be added. Must be a subtype of Number.
 * @param b The second number to be added. Must be a subtype of Number and of the same type as 'a'.
 * @return The sum of 'a' and 'b' as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a given SQL query on the specified database connection and returns the results as a list of rows,
 * where each row is a list of column values.
 * 
 * @param db The database connection on which the query will be executed.
 * @param query The SQL query to be executed.
 * @return A list of rows, with each row represented as a list of column values from the query result set.
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
 * Compares two items based on a key extracted by the keyMap function and returns an integer indicating their relative order.
 * The comparison is based on the natural ordering of the keys obtained from the items.
 * 
 * @param <T> The type of the items to be compared.
 * @param <R> The type of the key extracted from the items, which must be comparable.
 * @param keyMap A function that extracts a comparable key from each item for comparison.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer less than, equal to, or greater than zero if the key of item1 is respectively less than, equal to, or greater than the key of item2.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabets with the specified length.
 * The string can contain both uppercase and lowercase letters.
 *
 * @param length The desired length of the resulting random alphabetic string.
 * @return A random string consisting of letters from 'a' to 'z' and 'A' to 'Z' with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}