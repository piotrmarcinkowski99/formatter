# Task

### Created by Piotr Marcinkowski

#### To run tests:
```shell script
python tests/test.py
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

