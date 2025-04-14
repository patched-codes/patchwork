package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Computes the sum of two numbers and returns the result as a double.
 * The function takes two parameters of type Number, converts them to Double,
 * and returns their sum.
 *
 * @param a First number of type T (where T extends Number).
 * @param b Second number of type T (where T extends Number).
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the provided SQLite database connection and returns 
 * the results as a list of rows, where each row is represented as a list of column values.
 * 
 * @param db the SQLite database connection to be used for executing the query
 * @param query the SQL query to be executed on the database
 * @return a list of rows resulting from the query execution, with each row represented as a list of values
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
 * Compares two items based on a key extracted from them using a specified key mapping function. 
 * Returns -1 if the key of the first item is less than the key of the second item,
 * 1 if it's greater, or 0 if both keys are equal.
 * 
 * @param keyMap Function to extract the key of type R from each item of type T.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer indicating the comparison result: 
 *         -1 if item1 < item2, 1 if item1 > item2, or 0 if they are equal based on the extracted key.
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
 * @return A string of random alphabetic characters with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}