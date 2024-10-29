package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Computes the sum of two numbers, both of which are of a type that extends from Number. 
 * The result is returned as a Double.
 * 
 * @param a First number to be added, must be of a type that extends from Number.
 * @param b Second number to be added, must be of a type that extends from Number.
 * @return The result of adding the two numbers, converted to a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the given database connection and retrieves the result as a list of rows.
 * Each row is represented as a list of objects, with each object corresponding to a column value.
 * 
 * @param db The open connection to the SQLite database on which the query will be executed.
 * @param query The SQL query string to be executed.
 * @return A list of rows, with each row being a list of column values obtained from the query result set.
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
 * Compares two items based on a key extracted from each item using the provided key mapping function.
 * The comparison is performed on the extracted keys, which must be comparable.
 * 
 * @param keyMap A function that takes an item of type T and returns a value of type R, which is used as a key for comparison.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer indicating the comparison result: 
 *         -1 if the key of item1 is less than the key of item2,
 *         1 if the key of item1 is greater than the key of item2,
 *         or 0 if the keys are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string consisting of uppercase and lowercase alphabets.
 * 
 * @param length The desired length of the generated random string.
 * @return A random string composed of alphabets with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}