# PROBLEM 1
# How many artists are there?
# Return a single column called "count" with a single row containing the count.
query_1 = """
select count(*) "count" from "Artist"
"""

# PROBLEM 2
# How many Artists do not have an Album associated with them?
# Return a single column called "count" with a single row containing the count.
query_2 = """
select count(*) "count" from "Artist" a left join "Album" a2 on a."ArtistId" = a2."ArtistId"
where a2."ArtistId" is null
"""




query_3 = """
select count(*) "count" from "Artist" a right join "Album" a2 on a."ArtistId" = a2."ArtistId"
where a."ArtistId" is null

"""

# PROBLEM 4
# List the tracks by "AC/DC"
# Return a single column called "AC/DC Tracks",
# in any order.
query_4 = """
select t."Name" "AC/DC Tracks" from "Artist" a join "Album" a2 ON a."ArtistId" = a2."ArtistId" 
join "Track" t on a2."AlbumId" = t."AlbumId" 
where a."Name" = 'AC/DC'

"""

# PROBLEM 5
# Find the total sales of AC/DC Tracks.
# Return a single column called "Total Sales" with a single row containing the total.

query_5 = """

"""

# PROBLEM 6
# Calculate total sales for each artist,
# as defined by the "Artist" table,
# Return two columns, "Artist" and "Total Sales",
# for the artists with less than or equal to $5 in sales,
# in any order.

query_6 = """

"""

# PROBLEM 7
# Calculate total sales for each artist,
# as defined by the "Artist" table,
# Return two columns, "Artist" and "Total Sales",
# in descending order of "Total Sales".

query_7 = """

"""

# PROBLEM 8
# Find all of "Michael Mitchell"'s direct reports.
# Return 2 columns called "Name" and "Title".
# "Name" should have the employee's name in the form "last name, first name",
# for example, someone with the last name "Smith" and first name "Bob" should be "Bob, Smith".
# Hint: this requires a self join, picking clear aliases will help.

query_8 = """

"""

# PROBLEM 9
# Make a reporting chart. For each employee, find their name, title, manager's name and manager's title.
# Return 4 columns called "Employee Name" and "Employee Title", "Manager Name" and "Manager Title",
# "Employee Name" and "Manager Name" should have the employee's name as in the form "last name, first name",
# for example someone with the last name "Smith "and first name "Bob" should be "Bob, Smith".
# Hint: this requires a self join, picking clear aliases will help.

query_9 = """

"""

# PROBLEM 10
# Find the most recently hired employee(s) and their hire date(s)
# Return two columns called "Name" and "Hire Date",
# in any order.
# "Name" should have the employee's name as in the form "last name, first name",
# for example someone with the last name "Smith "and first name "Bob" should be "Smith, Bob"

query_10 = """

"""

# PROBLEM 11
# Assume today is "2010-01-01", find every employee's tenure.
# Return 3 columns called "First Name" "Last Name", "Tenure",
# in any order.

query_11 = """

"""
# PROBLEM 12
# Assume today is 2010-01-01, find every employee with a tenure of less than 7 365-day years.
# Return 3 columns called "First Name" "Last Name", "Tenure",
# in ascending order of tenure.

query_12 = """

"""
