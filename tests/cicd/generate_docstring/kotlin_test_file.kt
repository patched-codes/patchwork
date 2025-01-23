package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of a generic type that extends Number and returns the result as a Double.
 * 
 * @param a The first number of a generic type that extends Number.
 * @param b The second number of a generic type that extends Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a given SQL query on the provided database connection and returns the result as a list of rows,
 * where each row is a list of column values. Each column value can potentially be null.
 * 
 * @param db The database connection to be used.
 * @param query The SQL query to execute.
 * @return A list containing the rows fetched from the database. Each row is represented as a list of column values.
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
 * Compares two items using a key extraction function that maps each item to a comparable value.
 * 
 * @param keyMap A function that extracts a comparable key from each item for comparison.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return -1 if the key of item1 is less than the key of item2, 1 if the key of item1 is greater than the key of item2, and 0 if the keys are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabets with a specified length.
 * The string will contain both uppercase and lowercase letters.
 * 
 * @param length The number of characters in the resulting string.
 * @return A string consisting of random alphabets of the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}