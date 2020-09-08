# Task

### Created by Piotr Marcinkowski

### Description:
- The main point of this application is the possibility of formatting files with extension "txt". The program replaces spaces to tabs and vice versa. 

#### To run tests:
```shell script
python tests/test.py
```

#### To get coverage of tests:
1. Install requirements.txt 
    ```shell script
    pip install -r requirements.txt
    ```
2. Get coverage:
    ```shell script
    coverage run -m unittest discover
    ```
3. Display statistics:

    In the terminal
    ```shell script
    coverage report -m
    ```
    In browser 
    ```shell script
    coverage html
    ```



#### To run formatter:
```shell script
python -m modul -f [tabs/spaces] -r -t [length of a tab character]
```
![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) `The formatter formats only files that are in the text_files folder!` 

![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+) `Without -f param the formatter only displays information about tabs and space in the file!!!`
#### Params 
To get info about params in terminal use command:
```shell script
python -m modul --help
```

*  -f / --form (tabs/spaces)
    * determines the type of character that will be converted
*  -r / --replace 
    * with this param, the formatter does not make a save copy of file
*  -t / --tab-chars 
    * optional param which determines the number of space which replace a single tab character

