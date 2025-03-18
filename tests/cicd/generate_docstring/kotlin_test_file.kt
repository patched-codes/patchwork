package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of a generic type that extends the Number class and returns the result as a Double.
 * 
 * @param a First number to be added, of a type that extends Number
 * @param b Second number to be added, of a type that extends Number
 * @return The sum of the two numbers as a Double
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a given SQL query on the provided database connection and returns the result as a list of lists.
 * Each inner list represents a row, with elements corresponding to the column values.
 * 
 * @param db The database connection to be used for executing the query.
 * @param query The SQL query as a string to be executed on the database.
 * @return A list of lists containing the query results, where each list is a row of column values.
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
 * Compares two items by applying a transformation function to each item and then comparing the results.
 * 
 * @param keyMap A transformation function that takes an item of type T and returns a value of type R, which is comparable.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return -1 if the transformed value of item1 is less than that of item2, 1 if it is greater, or 0 if they are equal.
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
 * 
 * @param length The number of characters in the generated string.
 * @return A string consisting of random alphabetic characters (both uppercase and lowercase) with the given length.
 */

fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}