package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Computes the sum of two numbers and returns the result as a Double.
 * 
 * This generic function accepts two parameters of type Number and 
 * converts them to Double before performing the addition.
 * 
 * @param a The first number to add, of type T.
 * @param b The second number to add, of type T.
 * @return The sum of the two parameters as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the provided database connection and returns the results as a list of rows, each row being a list of column values.
 * 
 * @param db The database connection on which the SQL query is to be executed.
 * @param query The SQL query string to be executed.
 * @return A list of rows, where each row is represented as a list of column values from the query result set. Each column value can be `null`.
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
 * Compares two items based on a key extracted by the provided keyMap function. 
 * The comparison is based on the natural ordering of the key type, which must be comparable.
 * 
 * @param keyMap A function that extracts a comparable key from an item of type T.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer result of the comparison: -1 if item1 < item2, 1 if item1 > item2, and 0 if they are equal.
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
 * The string contains a mix of uppercase and lowercase letters.
 * 
 * @param length The length of the random string to generate.
 * @return A random string consisting of alphabetic characters.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}