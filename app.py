import pysolr

# Connect to the Solr instance
solr = pysolr.Solr('http://localhost:8983/solr/my_core', always_commit=True)

# Sample data to index
data = [
    {"id": "1", "title": "Introduction to Solr", "content": "Apache Solr is a search platform from the Apache Lucene project."},
    {"id": "2", "title": "Python with Solr", "content": "This document explains how to integrate Solr with Python."},
    {"id": "3", "title": "Advanced Full-Text Search", "content": "Learn about advanced search techniques using Solr."}
]

# Index data
solr.add(data)
print("Data indexed successfully.")

# Confirm data indexing by querying all documents
print("\nAll Indexed Documents:")
all_docs = solr.search("*:*")  # Retrieves all documents
if all_docs:
    for doc in all_docs:
        print(f"ID: {doc.get('id')}, Title: {doc.get('title')}, Content: {doc.get('content')}")
else:
    print("No documents found in the index.")

# Simple search query targeting specific fields
query = "content:Solr AND content:Python"  # Search for documents containing both "Solr" and "Python" in the 'content' field

# Execute the search
results = solr.search(query)

# Print the search results
print("\nSimple Search Results:")
if results:
    for result in results:
        print(f"ID: {result.get('id')}, Title: {result.get('title')}, Content: {result.get('content')}")
else:
    print("No results found for simple search.")

# Advanced search with specific fields, filters, and sorting
query = "title:Solr"
options = {
    "fq": "content:Solr",  # Filter to documents containing "Solr" in the content
    "fl": "id, title, content",    # Retrieve 'id', 'title', and 'content' fields
    "sort": "id asc"      # Sort results by 'id' in ascending order
}

# Execute the advanced search
advanced_results = solr.search(query, **options)

# Print the advanced search results
print("\nAdvanced Search Results:")
if advanced_results:
    for result in advanced_results:
        print(f"ID: {result.get('id')}, Title: {result.get('title')}, Content: {result.get('content')}")
else:
    print("No results found for advanced search.")


