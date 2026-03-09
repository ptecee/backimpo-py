# backimpo-py

## Концепция и 
Python скрипт, делает резервные копии важных файлов на локальном компьютере. То какие файлы и директории бэкапить задается в переменных в отдельном файле `values.py`, архив создается в формате `zip` архива.  

Формат переменных:
- `list_of_directories = {"folder-name": "/path/to/folder-name"}` в словарь помещаются все директории которые планируем бэкапить, ключ значения потом будет использоваться для создания имени архива
- `/path/to/backups/` место куда мы планируем складывать наши бэкапы. 

## Документация которая использовалась при создании
**os — Miscellaneous operating system interfaces**  
https://docs.python.org/3/library/os.html  

**pathlib — Object-oriented filesystem paths**  
https://docs.python.org/3/library/pathlib.html  

**zipfile — Work with ZIP archives**  
https://docs.python.org/3/library/zipfile.html  

**logging — Logging facility for Python**  
https://docs.python.org/3/library/logging.html  