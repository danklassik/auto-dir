## Создание папок из excel-файла. 

Просто попроcили помочь человеку чтобы та не сидела всю ночь и не создавал 9000 папок/подпапок.
1) Создаем файл "dirs.xls" (пример файла выкладываю).
2) Убеждаемся что в файле dirs.xls нет двойных скобочек --> "
3) Кладем файл в ту же директорию что и скрипт.
4) Запускаем скрипт и отходим на безопасное расстояние.

В папке "Output" скомпилированный exe файл.
Скомпилирован через:
```
pyinstaller --noconfirm --onefile --console "./magic.py"
```
