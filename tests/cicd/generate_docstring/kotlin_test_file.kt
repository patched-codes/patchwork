package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Calculates the sum of two numbers and returns the result as a Double.
 * This function accepts any numeric type that extends the Number class.
 * 
 * @param a The first number to add, of a type that extends Number.
 * @param b The second number to add, of a type that extends Number.
 * @return The sum of the two numbers, converted to a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the given database connection and returns the results as a list of rows,
 * where each row is a list containing the column values.
 * 
 * @param db The database connection to be used for executing the query.
 * @param query The SQL query to be executed.
 * @return A list of rows, with each row represented as a list of column values (which can be of any type).
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
 * Compares two items by applying a key generating function to them and comparing the results.
 * 
 * The function `keyMap` is called on both `item1` and `item2`, and the resulting keys of type `R` (which must be comparable) are compared to determine the order of `item1` and `item2`. 
 * 
 * @param keyMap Function that generates a comparable key from an item of type `T`.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer representing the comparison result: `-1` if `item1` is less than `item2`, `1` if `item1` is greater than `item2`, or `0` if they are equal.
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
 * @param length The length of the string to generate.
 * @return A random string of the specified length containing only alphabetic characters.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}