package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Sums two numeric values of the same type and returns the result as a Double.
 * 
 * @param a The first numeric value of a type that extends Number.
 * @param b The second numeric value of a type that extends Number.
 * @return The sum of the two values as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on a given SQLite database connection and returns the results as a list of rows, where each row is a list of column values.
 * This function utilizes the provided database connection to execute the given query and process the ResultSet into a list of lists containing the query results.
 * 
 * @param db The SQLite database connection used to execute the SQL query.
 * @param query The SQL query to be executed on the database.
 * @return A list of lists representing the query result, where each internal list corresponds to a row of the result with each element representing a column value.
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
 * Compares two items based on a mapped key function and returns an integer result indicating their order.
 * 
 * @param keyMap A function that maps an item of type T to a comparable key of type R.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer: -1 if item1 is less than item2, 1 if item1 is greater than item2, or 0 if they are equal.
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
 * The string consists of both uppercase and lowercase letters.
 * 
 * @param length The desired length of the generated string.
 * @return A random string composed of alphabets with the given length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}