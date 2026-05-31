# backimpo-py

## Концепция
Python скрипт, делает резервные копии важных файлов на локальном компьютере. То какие файлы и директории бэкапить задается в конфиг файле `config.toml`, архив создается в формате `zip` архива.  

## То что нужно доработать
- обернуть логирование в декораторы
- разработать функцию которая будет ротировать архивы и оставлять три последних

## Документация, которая использовалась при создании
**os — Miscellaneous operating system interfaces**  
https://docs.python.org/3/library/os.html  

**pathlib — Object-oriented filesystem paths**  
https://docs.python.org/3/library/pathlib.html  

**zipfile — Work with ZIP archives**  
https://docs.python.org/3/library/zipfile.html  

**logging — Logging facility for Python**  
https://docs.python.org/3/library/logging.html  
