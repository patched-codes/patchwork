package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of type Number and returns their sum as a Double.
 * 
 * @param a The first number to be added. Must be of a type that extends Number.
 * @param b The second number to be added. Must be of a type that extends Number.
 * @return The sum of `a` and `b` as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the provided database connection and returns the result set as a list of rows, 
 * where each row is represented as a list of objects.
 * 
 * @param db A Connection object that represents a connection to a database.
 * @param query A String containing the SQL query to be executed.
 * @return A list of lists, where each inner list represents a row returned by the query and each element in 
 *         the inner list is an object corresponding to the column value in that row.
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
 * Compares two items based on a key mapping function that extracts a comparable value from each item.
 * The function returns an integer result indicating whether the first item is less than, equal to, or greater than the second item.
 * 
 * @param keyMap A function that takes an item of type T and returns a comparable key of type R.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer: -1 if the first item is less than the second item, 0 if they are equal, and 1 if the first item is greater than the second item.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string consisting of alphabetic characters, both uppercase and lowercase.
 * 
 * @param length The desired length of the resulting string with random alphabetic characters.
 * @return A string consisting of randomly selected alphabetic characters of the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}