package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Computes the sum of two numbers of type T, which is a subtype of Number, and returns the result as a Double.
 *
 * @param a The first number to be added, must be of a type that extends Number.
 * @param b The second number to be added, must be of a type that extends Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on a given SQLite database connection and returns the results as a list of rows, 
 * where each row is represented as a list of column values.
 *
 * @param db The database connection on which the query is to be executed.
 * @param query The SQL query to be executed on the database.
 * @return A list of lists, where each inner list represents a row of the result set, 
 * containing column values as objects.
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
 * Compares two items of type T using a key extraction function, which maps item to a comparable key of type R.
 * The function returns an integer: -1 if item1 < item2, 1 if item1 > item2, and 0 if they are equal according to their keys.
 * 
 * @param keyMap The function that extracts a comparable key of type R from an item of type T.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer representing the comparison result: -1 if item1 < item2, 1 if item1 > item2, 0 if they are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string consisting of alphabets (both uppercase and lowercase) of a specified length.
 * 
 * @param length The length of the random string to be generated.
 * @return A string containing randomly selected alphabets of the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}