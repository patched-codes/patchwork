package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Calculates the sum of two numbers of type Number and returns the result as a Double.
 * 
 * @param a The first number to add, which is of type Number.
 * @param b The second number to add, which is also of type Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a given SQL query on the specified database connection and retrieves the result set as a list of rows,
 * where each row is represented as a list of column values.
 * 
 * @param db The database connection through which the query is executed.
 * @param query The SQL query to be executed on the database connection.
 * @return A list of rows retrieved from the query, each row being a list of column values (nullable).
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
 * Compares two items of type T based on a provided key mapping function that extracts
 * a comparable attribute of type R from each item. The result of the comparison determines
 * the order of the two items.
 * 
 * @param keyMap A mapping function that takes an item of type T and returns a comparable attribute of type R.
 * @param item1 The first item of type T to be compared.
 * @param item2 The second item of type T to be compared.
 * @return An integer indicating the order of the two items: -1 if item1 < item2, 1 if item1 > item2, and 0 if they are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabetic characters with the specified length.
 * The string contains both uppercase and lowercase letters.
 * 
 * @param length The length of the random string to generate.
 * @return A string composed of random alphabetic characters with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}