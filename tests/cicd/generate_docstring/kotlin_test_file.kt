package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Computes the sum of two numbers and returns the result as a Double.
 * This function accepts parameters of any type that extends Number.
 * 
 * @param a The first number to be added.
 * @param b The second number to be added.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on a given database connection and returns the result set as a list of lists,
 * with each nested list representing a row and each element within the nested list representing a column value.
 * 
 * @param db The database connection used to execute the SQL query.
 * @param query The SQL query to be executed.
 * @return A list of lists where each list represents a row of the result set, 
 *         and each element of the row list is a column value retrieved from the result set.
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
 * Compares two items using a key mapping function and returns an integer value 
 * for the comparison result. The items are compared based on the comparable 
 * result of applying the keyMap function to each item.
 *
 * @param <T> The type of the items being compared.
 * @param <R> The type of the result of the key mapping, which must be comparable.
 * @param keyMap A function that maps an item of type T to a comparable key of type R.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return A negative integer, zero, or a positive integer if the key of item1 
 *         is less than, equal to, or greater than the key of item2, respectively.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabets with the given length.
 * 
 * @param length The length of the desired random string of alphabets.
 * @return A string containing randomly selected alphabetic characters (both uppercase and lowercase) with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}