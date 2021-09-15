I might have taken some notes
install: https://github.com/andmarti1424/sc-im/wiki/Installing-on-Debian

it doesn't have a tutorial online, and function based article

some useful key strocks
```
     fr          freeze a row, usually row 0
     aa    c-j   Auto-resize the selected column(s) to accommodate the widest
                 cells.
     :set {option}={value}
                 Set a configuration option to {value}. The arguments may be
                 repeated.
                 Example:    :set half_page_scroll=0 numeric_zero=1
                             :set numeric          (same as :set numeric=1)
                             :set nonumeric        (same as :set numeric=0)
                             :set default_paste_from_clipboard_cmd="xsel"
```

If I wanna input records, each ENTER would bring me to the next cell in a colmn, not a row
maybe we seldom input data manually, rather use a HTML fill tables and program input spreadsheet format

sort
    :sort C10:E13 "+#C;-#D"

search
    /123123
    /"String"
