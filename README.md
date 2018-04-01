# BooleanSearch

* Implement a keywords search in database.
* Support AND, OR, NOT operations.
* Implement inverted index with Python dictionary. Using a brute force search for the first time and store the result(index sets) which is obtained by keywords for further queries.
  ```
  record = dict()

  ...

  if content in record:
      temp_set = record[content]
  else:
    for row in source_data:
      if row[1].find(content) > -1:
          temp_set.add(int(row[0]))
    record[content] = temp_set
  ```

## Environment
* Ununtu 16.04
* Python 3.6.4

## Run
  `python main.py`
