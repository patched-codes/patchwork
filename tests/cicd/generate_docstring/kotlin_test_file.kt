package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Computes the sum of two numbers, converting them to Double.
 * 
 * This function takes two parameters of a type that extends Number,
 * converts them to Double, and returns their sum as a Double.
 * 
 * @param a The first number to add, must extend Number.
 * @param b The second number to add, must extend Number.
 * @return The sum of a and b as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the given database connection and returns the 
 * results as a list of rows, where each row is a list of column values.
 * 
 * @param db The database connection to be used for executing the query.
 * @param query The SQL query string to be executed on the database.
 * @return A list of lists, where each inner list represents a row of the 
 * query result. Each element of the inner list corresponds to a column value 
 * in that row. If the query returns no results, an empty list is returned.
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
 * Compares two items based on a specified key mapping function and returns an integer indicating their order.
 * 
 * @param keyMap A function that maps an item of type T to a comparable key of type R. This function is used to determine the attribute by which the comparison occurs.
 * @param item1 The first item of type T to be compared.
 * @param item2 The second item of type T to be compared.
 * @return An integer: -1 if item1 is less than item2, 1 if item1 is greater than item2, and 0 if they are equal based on the key map.
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
 * The string includes both lowercase and uppercase letters.
 * 
 * @param length The number of characters in the generated string.
 * @return A string composed of random alphabetical characters.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}