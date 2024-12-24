package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of type Number and returns the result as a Double.
 * 
 * @param a First number to add, of type Number.
 * @param b Second number to add, of type Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes the provided SQL query on the given database connection and returns the results.
 *
 * This method uses the provided database connection to execute a SQL query and retrieves the
 * results as a list of rows, each represented as a list of objects. The method supports queries
 * that return any number of columns, and each row in the result set is converted into a list
 * containing the column values as objects.
 * 
 * @param db The database connection to use for executing the query.
 * @param query The SQL query to be executed.
 * @return A list of rows, where each row is represented as a list of column values obtained from the query execution.
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
 * Compares two items of type T based on a key extracted by a key mapping function, returning 
 * an integer to indicate their relative order.
 * 
 * @param keyMap A lambda function that maps an item of type T to a comparable key of type R
 * @param item1 The first item to be compared
 * @param item2 The second item to be compared
 * @return An integer result: -1 if the key of item1 is less than the key of item2, 
 *         1 if the key of item1 is greater than the key of item2, 
 *         and 0 if the keys are equal
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string consisting of alphabetic characters (both uppercase and lowercase).
 * The length of the generated string is specified by the input parameter.
 * 
 * @param length The desired length of the resulting random string. Should be a non-negative integer.
 * @return A random string composed of alphabetic characters with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}