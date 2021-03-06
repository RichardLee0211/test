                         This is the SC-IM help file.

Use the cursor keys to move around, or 'j' to go down and 'k' to go up.
You can also use the <ENTER> key to go one line down and <DEL> to go up.

<SPACE> moves a page down, while <C-f> and <C-b> move half page down or up.

'G' moves to bottom, and <C-a> or 'gg' to the beginning of the text.

Use '/' to search for a pattern in the help.

Use ':q<Enter>' to go back to the spreadsheet.

==============================================================================
SC-IM has the following modes:

SC-IM has the following modes:
   NORMAL MODE:  In Normal mode, you can navigate cells and input normal
                 commands.
   INSERT MODE:  Use the '=', '<', '>', or '\' to go to Insert mode, where you
                 can enter new values and expressions into cells.
     EDIT MODE:  Use the 'e' or 'E' keys to go to Edit mode and enter a single
                 line, Vi-like, command to modify cell content
                 and expressions.  The 'e' and 'E' keys enter this mode.
  COMMAND MODE:  Use the ':' key to enter Command mode. This is for entering
                 special commands such as quitting the app and saving files.
   VISUAL MODE:  Visual mode is used for selecting a range of cells.  See the
                 section 'Selecting a range' below.
                 The 'v' key enters this mode from Normal mode, or <C-v> in
                 Insert and Command modes.

==============================================================================
&NORMAL MODE&

Navigation commands:
     j k l h     Move cursor down, up, right or left.

     ^           Go up to row 0 of the current column.
                 wenchen: I wanna it to be go to the first colume of this low

     #           Go down to the last valid row of the current column.  If
                 already in last valid row of the current column, then jump to
                 last valid row of the last valid cell in spreadsheet.

     0           Go left to column A in the current row.
     $           Go right to the last valid column of the current row.

     b           Go back to the previous valid cell.
     w           Go forward to the next valid cell.

     '{a-zA-Z}   Go to the cell or range marked previously with the character.
                 See 'm' for details.

     gab24       Go to cell AB24.  (There is no need to press <ENTER>.)

     g0          Go to the leftmost column visible on screen.
     g$          Go to the rightmost column visible on screen.
     gM          Go to the middle column on the screen.

     H           Go to the top row visible on screen.
     L           Go to the lowest row visible on screen.
     M           Go to the middle row on the screen.

     gg    c-a   Go to the first cell of sheet.
                 wenchen: wanna go to first row of current column
     G     gG    Go to last valid cell of sheet.
                 wenchen: wanna go to last row of current column

     gl          Go to the last (previously occupied) cell position.

                 TODO:
     c-f   c-b   Scrolls down and up full screen.
                 :set half_page_scroll=1 to scroll by half a page instead.
                 half_page_scroll=0 (default) scrolls by a full page.
                 See :set command for details.

     c-e   c-y   Scroll a row down and up.
     zh          Scroll left one column.
     zl          Scroll right one column.
     zH          Scroll left half a page.
     zL          Scroll right half page.
     zm          Scroll horizontally to position the selected cell at the
                 center of the screen.
     zz or z.    Scroll vertically to position the selected cell at the middle
                 of the screen.
     zt          Scroll vertically to position the selected cell at the top
                 of the screen.
     zb          Scroll vertically to position the selected cell at the bottom
                 of the screen.
     Vir         Select the smallest range that covers all valid cells.
     ESC or c-g  Clean stdin buffer, so SC-IM no longer waits for completing a
                 correct command.


Commands for handling cell content:
     x     dd    Delete the current selected cell or range and save its
                 content in the yankbuffer.

     m{a-zA-Z}   Mark the current cell or selected range with that letter.
                 Note: When a mark is changed, all ranges that use that mark
                 are deleted.
     c{a-zA-Z}   Copy the marked cell or range to the current position,
                 adjusting row and column references in its numeric or string
                 expression, if any.
     R{a-zA-Z}{a-zA-Z}
                 Select the range defined by the two marks.
                 Note: If a range already exists, it is replaced with the new
                 values.

     { } |       Align the content of a cell to the left, right or center.  If
                 a range is selected, every cell of the range gets aligned.

     f+ , fk , f-UP:         Change cell format: Increment decimal precision.
     f- , fj , f-DOWN:       Change cell format: Decrement decimal precision.
     f< , fh , f-LEFT:       Change cell format: Decrement column width.
     f> , fl , f-RIGHT:      Change cell format: Increment column width.

     fr          Freeze a row or the rows selected.
                 If none is selected it freezes the current row.
                 NOTE: there can be only just one frozen range defined.

     fc          Freeze a col or the cols selected.
                 If none is selected it freezes the current col.
     fa          Freeze the area selected.

     ir          Insert a row.
     ic          Insert a column.
     or          Open a row: insert after the current row.
     oc          Open a column: insert after the current column.

     sk          Shifts the current cell or range up.
     sj          Shifts the current cell or range down.
     sh          Shifts the current cell or range left.
     sl          Shifts the current cell or range right.

     yy          Yank the selected cell.
     y           If a range is selected, yank the range.
     yr          Yank current row.
     yc          Yank current column.

     p           Paste the previously yanked cell or range.
                 If yr was used to yank a row, create a new row below and
                 paste content there.
                 If yc was used to yank a column, create a new column to the
                 left and paste content there.
     Pf          Works like 'p' except that only the cell formatting is
                 merged, leaving cell values intact.
     Pv          Works like 'p' except that only cell values are copied,
                 leaving cell formatting intact.
     Pc          Works like 'p' except that all cell references are adjusted
                 in the same way that they are for the copy command.

     t           Same as 'p' but if yr was used to yank a row, create a new
                 row above and paste content there.
                 If yc was used to yank a column, create a new column to the
                 right and paste content there.
     Tf          Works like 't' except that only cell formatting information
                 is merged in, leaving cell values intact.
     Tv          Works like 't' except that only cell values are copied,
                 leaving cell formatting intact.
     Tc          Works like 't' except that all cell references are adjusted
                 in the same way that they are for the copy command.

     dr          Delete the current row.
     dc          Deletes the current column.
     .           Repeat the last normal mode command.
     -           Decrease a numeric value of the cell or range.
     +           Increase a numeric value of the cell or range.

     u           UNDO last change
     c-r         REDO last change
                 Note: Events implemented for undo and redo:
                 1. cell or range deletion
                 2. cell input
                 3. cell editing
                 4. cell or range change in alignment
                 5. pasting a cell or range
                 6. range or cell shift with sh sj sk sl
                 7. row or column insertion
                 8. row or column deletion
                 9. pasting a row or column
                 10. zap(hide) or show a row or column
                 11. reordering of a range
                 12. changing the format of a range or cell
                 13. '-' and '+' commands in normal mode
                 14. locking and unlocking of cells
                 15. the datefmt command
                 16. the cellcolor command

     c-d         Convert the text content of a selected cell or range to a
                 date, using default LOCALE's D_FMT format.
                 This converts text to a numeric value that can be shown as a
                 date. See DATE INPUT below for more info.
                 Note: USELOCALE has to be enabled during build.

     aa    c-j   Auto-resize the selected column(s) to accommodate the widest
                 cells.

 Other commands:
     ^L          Redraw the screen.
     Zr          Zap (hide) the current row.
     Zc          Zap (hide) the current column.
     Sr          If a range is selected, show the rows hidden in the range.
     Sc          If a range is selected, show the columns hidden in the range.
     '/'         Alias for ':int goto '.

                 If a number is given, SC-IM will search for a cell containing
                 that number.  Searches for either strings or numbers proceed
                 forward from the current cell, wrapping back to a0 at the end
                 of the table, and terminate at the current cell if the string
                 or number is not found.

                 Example: Type '/4' to look for cells containing the value 4.
                 Or type '/"value"' to look for cells that has "value" as
                 label content.
                 You can quote a regular expression, and SC-IM will search for
                 a cell containing a string matching the regular expression.
                 You can search for formatted numbers or expressions using
                 regular expressions by preceding the opening quotes of the
                 regular expression with a '#' (for formatted numbers) or a
                 '%' (for expressions).
                 These are handy for searching for dates within a specified
                 range or cells which reference a given cell, for example,
                 although they are somewhat slower than searching through
                 ordinary strings, since all numbers must be formatted or
                 expressions decompiled on the fly during the search.
     n           Move to next search match.
     N           Move to previous search match.

     rl          Lock the current cell or range. Locking makes cells immune to
                 any type of editing. A locked cell can't be changed in any
                 way until it is unlocked.
     ru          Unlock a locked cell or range, making it editable.
     rv          Valueize the current cell or range. Valueizing removes
                 expressions, leaving only the values.

==============================================================================
&INSERT MODE&

     =           Enter a numeric constant or expression.
     <           Enter a left justified string or string expression.
     \           Enter a centered label.
     >           Enter a right justified string or string expression.
     <TAB>       Return to Edit mode from Insert mode.
     <LEFT>, <RIGHT>
                 Move the cursor with the arrow keys.
     Keys <ENTER>
                 Input numbers, letters and operators.
     <BS>, <DELETE>
                 Delete the character after or before the cursor.
     <ESC>       Go back to NORMAL MODE. If you were in EDIT MODE before,
                 it goes back to that mode, instead of NORMAL MODE.
     c-r{a-zA-Z}
                 If the character is a mark of a cell or range, the range
                 represented is inserted into the field.
     c-v         Enter Visual mode. See C-o and C-k commands in VISUAL MODE.

==============================================================================
&EDIT MODE&

     e           In normal mode, enter Edit mode to edit a numeric value.
     E           In normal mode, enter Edit mode to edit a text value.
     h           Move a character left.
     l           Move a character right.
     w           Move to the beginning of the next word.
     e           If at the end of a word, move to the end of the next word.
                 Otherwise, move to the end of word under the cursor.
     b           If at the beginning of a word, move to beginning of the
                 previous word. Otherwise, move to beginning of word under the
                 cursor.
     0           Move to the beginning of the line.
     $           Move to the end of the line.
     f{char}     Move to the next occurrence of {char} to the right.
     r{char}     Replaces the character under the cursor with {char}.
     R{word}     Each character you type replaces an existing character,
                 starting with the character under the cursor.
                 ESC key or ENTER key must be pressed when finished typing the
                 new word.

     de          Delete until the end of the word.
     dw          Delete until the beginning of the next word.
     db          If at the beginning of a word, delete until the beginning of
                 the previous word. Otherwise, delete until the beginning of
                 the word under the cursor.
     daw         Delete the word under the cursor.
     dE          Delete until the end of WORD.
     dW          Delete until the beginning of the next WORD.
     dB          If at the beginning of a word, delete until the beginning of
                 previous WORD. Otherwise, delete until the beginning of the
                 WORD under the cursor.
     daW         Delete the WORD under the cursor.
     dl          Delete the character under the cursor.
     d<RIGHT>    Delete the character under the cursor.
     dh          Delete the character before the cursor.
     d<LEFT>     Delete the character before the cursor.

     ce          Same as "de", then enter Insert mode.
     cw          Same as "dw", then enter Insert mode.
     cb          Same as "db", then enter Insert mode.
     caw         Same as "daw", then enter Insert mode.
     cE          Same as "dE", then enter Insert mode.
     cW          Same as "dW", then enter Insert mode.
     cB          Same as "dB", then enter Insert mode.
     caW         Same as "daW", then enter Insert mode.
     cl          Same as "dl", then enter Insert mode.
     c<RIGHT>    Same as "d<RIGHT>", then enter Insert mode.
     ch          Same as "dh", then enter Insert mode.
     c<LEFT>     Same as "d<LEFT>", then enter Insert mode.

     x           Delete the character under the cursor.
     X           Delete the character before the cursor.
     i or =      Go back to Insert mode.
     a           Append a character after the cursor.
     s           Delete a character under the cursor, then enter Insert mode.
     A           Append at the end of the line.
     I           Append at the beginning of the line.
     D           Delete from the current cursor position to end of line.
     <SPACE>     Add a space under the cursor.
     <ENTER>     Confirm changes.
     <ESC>       Go back to NORMAL MODE. If you were in INSERT MODE before,
                 it goes back to that mode, instead of NORMAL MODE.
==============================================================================
&COMMAND MODE&

     <LEFT>, <RIGHT>
                 Move the cursor position with the arrow keys.

     <ENTER>
                 Confirm a command.

     <DELETE>, <BS>
                 Delete the character under the cursor, or before the cursor.

     <HOME>, <END>
                 Move the cursor to the beginning or end of the line.

     <TAB>       Complete a command that begins with the text already entered
                 in the command line.

     <C-w>, <C-b>
                 Move forward or backwards a word.

     <C-f>
                 Paste the current cell format (if any) to the command line.

     <C-v>       Starts VISUAL MODE. See C-o and C-k commands in VISUAL MODE.

     :w          Save the current spreadsheet.
     :w {file}   Save the current spreadsheet as {file}.
     :w! {file}  Save the current spreadsheet as {file}, forcing an overwrite
                 if {file} already exists.

     :h          Show this help.
     :help       Show this help.

     :q[uit]     Quit SC-IM.
     :q[uit]!    Quit SC-IM, ignoring unsaved changes.

     :load {file}
                 Load {file} into the SC-IM database.

                 {file} can be an sc format file (.sc), a comma-separated file (.csv),
                 a tab-separated file (.tab, .tsv), an xlsx or xls file.

                 If loading a csv, tab or tsv file and 'import_delimited_as_text' configuration variable is set
                 Sc-im will import numbers as text.

                 If loading an xlsx file and 'xlsx_readformulas' is set, Sc-im will try to import
                 formulas, rather than the final values of a cell.

     :load! {file}
                 Same as previous, but ignore changes done to the current
                 loaded spreadsheet.

     :x          Save the current spreadsheet and quit SC-IM.
     :wq

     :x {file}   Save the current spreadsheet to {file} and quit SC-IM.

     :x! {file}  Like ":x", but overwrite {file} if it exists.

     :e tab      Export the current spreadsheet to a tab-separated file.
                 The name of the created file comes from the current
                 spreadsheet, with ".tab" appended.
                 If a range is selected, only that range is exported.
                 NOTE: If you do an export with the :e command, current file name stays unchaged.
                 See :file command for more details.

     :e txt      Export current spreadsheet to plain text.
                 If a range is selected, only that range is exported.

     :e csv {file}
                 Export the current spreadsheet to comma-separated file
                 {file}.

     :e! csv {file}
                 Like ":e csv", but overwrite {file} if it exists.

     :e tab {file}
                 Export the current spreadsheet to tab-separated file {file}.

     :e! tab {file}
                 Like ":e tab", but overwrite {file} if it exists.
                 If a range is selected, only that range is exported.

     :e txt {file}
                 Export the current spreadsheet to plain text file {file}.

     :e! txt {file}
                 Like ":e txt", but overwrite {file} if it exists.

     :e xlsx {file}
                 Export the current spreadsheet to xlsx file {file}.
                 If 'xlsx_readformulas' is set, SC-IM tries to export
                 formulas, rather than the final values of a cell.

     :e! xlsx {file}
                 Like ":e xlsx", but overwrite {file} if it exists.

     :ccopy      Copy a selected range to clipboard.
                 When 'ccopy' command is executed, the default value of macro
                 DEFAULT_COPY_TO_CLIPBOARD_CMD (set in Makefile during build)
                 is executed.
                 That value contains a system command that is executed to copy
                 to an specific clipboard. See in Makefile the different
                 options available.
                 You can also set a different value of 'default_copy_to_clipboard_cmd'
                 configuration variable at runtime, using the :set command.
                 This process will export content as plain text.
                 It will not delimit columns with '\t' chars.
                 If you wish to delimit columns with tabs, to paste content
                 directly to other spreadsheet programs, rather than an
                 editor, set "copy_to_clipboard_delimited_tab" variable to "1".

     :cpaste     Paste clipboard content to Sc-im.
                 When 'cpaste' command is executed, the default value of macro
                 DEFAULT_PASTE_FROM_CLIPBOARD_CMD (set in Makefile during build)
                 is executed.
                 That value contains a system command that is executed to
                 paste content of a specific clipboard to Sc-im.
                 See in Makefile the different options available.
                 You can also set a different value of 'default_paste_from_clipboard_cmd'
                 configuration variable at runtime, using the :set command.
                 This process will treat '\t' chars as column delimiter, and '\n' chars
                 as rows delimiters.

     :version    Show SC-IM version number.

                 If you start Sc-im with ./sc-im --version
                 version number of Sc-im will be printed on screen, including
                 the different features that were enabled when Sc-im was compiled.
                 Afterwards Sc-im will exit.

     :refresh    Refresh the UI. Acts like the <C-l> command of NORMAL_MODE.

     :set        Show all configuration options and their values.

     :set {option}={value}
                 Set a configuration option to {value}. The arguments may be
                 repeated.
                 Example:    :set half_page_scroll=0 numeric_zero=1
                             :set numeric          (same as :set numeric=1)
                             :set nonumeric        (same as :set numeric=0)
                             :set default_paste_from_clipboard_cmd="xsel"

     :showmaps   Show all key mappings.

     :nmap {lhs} {rhs}
                 Map the key sequence {lhs} to {rhs} This mapping takes effect
                 only in NORMAL_MODE.
                 Example:  :nmap "H" ":h<cr>"

     :imap {lhs} {rhs}
                 Map the key sequence {lhs} to {rhs} This mapping takes effect
                 only in INSERT_MODE.
                 Example:  :imap "<C-f>" "format"

     :nnoremap {lhs} {rhs}
                 This is the non-recursive version of ":nmap". See NOTES on
                 MAPPING below

     :inoremap {lhs} {rhs}
                 This is the non-recursive version of ":imap". See NOTES on
                 MAPPING below

     :nunmap {lhs}
                 Remove the map sequence {lhs} that takes effect in
                 NORMAL_MODE.

     :iunmap {lhs}
                 Remove the map sequence {lhs} that takes effect in
                 INSERT_MODE.

     :file [{file}]
                 If {file} is given, expand {file}, and set the current file
                 name to the result of the expansion.

                 If {file} is not given, display the current file name on
                 the status line.
                 Take note that current file name is set during loading of
                 Sc-im or with this command. If you do an export with the :e
                 command, current file name stays unchaged.

     :fill {range} {initial_number} {increment_number}
                 Fill range {range} with values. The first cell of the range
                 will have {initial_number} and each successive cell
                 increments by {increment_number}.
                 Example:   :fill A0:A100 1 0.25

     :format "{format_string}"
           Set the numeric format for the selected cell or range.
           {format_string} can contain one or more of these:

           #    Digit placeholder.  If the number has fewer digits on either
                side of the decimal point than there are '#' characters in
                the format, the extra '#' characters are ignored.  The number
                is rounded to the number of digit placeholders as there are
                to the right of the decimal point.  If there are more digits
                in the number than there are digit placeholders on the left
                side of the decimal point, then those digits are displayed.

           0    Digit placeholder.  Same as for '#' except that the number
                is padded with zeroes on either side of the decimal point.
                The number of zeroes used in padding is determined by the
                number of digit placeholders after the '0' for digits on
                the left side of the decimal point and by the number of
                digit placeholders before the '0' for digits on the right
                side of the decimal point.

           .    Decimal point.  Determines how many digits are placed on
                the right and left sides of the decimal point in the number.
                Note that numbers smaller than 1 will begin with a decimal
                point if the left side of the decimal point contains only
                a '#' digit placeholder.  Use a '0' placeholder to get a
                leading zero in decimal formats.

           %    Percentage.  For each '%' character in the format, the actual
                number gets multiplied by 100 for the purposes of formatting
                (the original value is unmodified) and the '%' character is
                placed in the same position as it is in the format.

           ,    Thousands separator.  The presence of a ',' in the format
                (multiple commas are treated as one) will cause the number
                to be formatted with a ',' separating each set of three digits
                in the integer part of the number with numbering beginning
                from the right end of the integer.

           d    Specifies a date format that is applied to the numeric value
                of a cell. (See also the DATE INPUT section below.) Date
                format strings are identified by the presence of a 'd' in the
                first position.  If this is present, the remainder of the
                string is passed to the strftime() function, and therefore
                uses the same conversion specifiers as strftime().
                For more information on conversion specifiers for date format
                strings, see the man page for strftime(3).

           E- E+ e- e+
                Scientific format.  Causes the number to formatted in
                scientific notation.  The case of the 'E' or 'e' given is
                preserved. If the format uses a '+', then the sign is always
                given for the exponent value.  If the format uses a '-', then
                the sign is only given when the exponent value is negative.
                Note that if there is no digit placeholder following the '+'
                or '-', then that part of the formatted number is left out. In
                general, there should be one or more digit placeholders after
                the '+' or '-'.

           Examples:     :format "###,###,000"
                         :format "d%d/%m/%Y"
                         :format "####.####E+3"


    :datefmt "{date_format_string}"   See the DATE INPUT section below.


    :sort {range} "{sort_string}"
                Sort a range of cells with a given criteria.
                The rows in the specified range will be sorted according
                to a criteria given in the form of a string of characters.
                This string, enclosed in double quotes, may comprise a
                single criterion or multiple criteria in decreasing order
                of precedence. Each criterion has three parts, all of which
                are mandatory.

                The first part is a single character, either + or -, which
                specifies whether the sort should be done in ascending or
                descending order, respectively.

                The second part, also a single character, is either # or $,
                and specifies whether the sort should be based on the numeric
                portion or the string portion, respectively, of the cells
                being
                used for the comparison.

                The third part is one or two letters (case insensitive) that
                specify the column used for making the comparisons.  This
                column must be in the range being sorted.

                Criteria may be concatenated with ';' and are applied in the
                order specified.

                Examples:        :sort C10:E13 "+#D"
                                 :sort C10:E13 "+#C;-#D"

    :sort "{sort_string}"
                Like ":sort {range}", but the sort is performed on the
                selected range.

    :subtotal {col_range} {operation} {col_operation}
                Apply subtotals over the data in a selected range.
                {col_range} is the column to group by.
                {operation} can be one of the followings:
                    @sum, @prod, @avg, @count, @stddev, @max, @min
                {col_operation} is the column whose values will be used
                to do the {operation}.
                Example: load the file example examples/sc/subtotals.sc,
                select the A1:C9 range, and type    :subtotal A @sum C

    :addfilter "{filter_string}"
    :showfilters
    :filteron {range}
    :filteroff
    :delfilter {filter_number}
    :delfilters
                These commands filter a range of rows by multiple criteria.

                ":addfilter" defines a filter according to {filter_string} in
                this format:

                The first part is either '#' or '$', and specifies whether the
                expression evaluates the numeric portion or the string portion
                of the cell.

                The second part specifies the column that contains the values
                to be evaluated with the expression.

                The third part is the actual expression evaluated.

                Multiple criteria can be separated with the ';' character.

                Examples:
                            :addfilter "#B<8000"
                            :addfilter "#C>1500"
                            :addfilter "@eqs(@substr($B,1,3),'SEP')"
                            :addfilter "#B>3000;#B<5000;#B>@avg(B1:B20)"

                Once filters are added, you can see the details of each filter
                with ":showfilters".
                Each filter is preceded by a number. You can delete a filter
                with ":delfilter {filter_number}".
                For example, to remove the first filter defined:
                            :delfilter 0

                ":delfilters" deletes all defined filters.

                ":filteron {range}" applies the filters to the range.
                Example:        :filteron B10:C13

                If a range is selected you can simply type ":filteron".

                ":filteroff" turns off the filters.

    :int "{string}"
                Send a command to the interpreter.
                Example:          :int goto B2


    :hidecol {column}
    :hidecol {column:column}
                Hide the column or column range given. (Case insensitive.)

    :hiderow {row}
    :hiderow {row:row}
                Hide the row or rows given.

    :showcol {column}
    :showcol {column:column}
                Show columns that were previously hidden.

    :showrow {rows}
    :showrow {row:row}
                Show rows that were previously hidden.

    :hiddenrows
                Show details of hidden rows.

    :hiddencols
                Show details of hidden columns.

    :freeze {column}
    :freeze {column:column}
                Freeze the column or column range given. (Case insensitive).
                (the rest of the screen scrolls but the column/s stays fixed on the screen).
                NOTE: there can be only just one frozen range defined.

    :freeze {row}
    :freeze {row:row}
                Freeze the row or row range given.
                (the rest of the screen scrolls but the row/s stays fixed on the screen).

    :freeze {range}
                Freeze a range given.  (Case insensitive).
                (the rest of the screen scrolls but the range stays fixed on the screen).

    :unfreeze
                Remove a previous frozen row / col or range.

    :pad {spaces}
                Apply a left padding {spaces} characters in width to a column.
                If a range selected, pad the columns inside that range.

    :color "{key}={arg} .."
                Change a color definition.

                {key} is one of the following:
                type, fg, bg, bold, dim, reverse, standout, underline, blink
                Note: The type, fg, and bg keys are mandatory.

                The value of type shall be one of the following:
                     HEADINGS, MODE, NUMB, STRG, DATEF, EXPRESSION,
                     CELL_ERROR, CELL_NEGATIVE, CELL_SELECTION,
                     CELL_SELECTION_SC, INFO_MSG, ERROR_MSG, CELL_ID,
                     CELL_FORMAT, CELL_CONTENT, WELCOME, NORMAL, INPUT.

                The value of fg and bg shall be one of the following:
                     WHITE, BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN or DEFAULT_COLOR.
                     DEFAULT_COLOR just takes the default color of your
                     terminal. If you set it as fg color it will take default
                     color of your foreground. If you set it as bg color it
                     will take the default background color of your terminal.

                The value of other parameters are booleans, 1 or 0.

                Example:  :color "type=HEADINGS bold=0 fg=BLACK bg=YELLOW"

                Colors can be set at runtime or specified in:
                     a. the .scimrc file stored in $HOME
                     b. the current .sc file.

                color "type=HEADINGS fg=WHITE bg=CYAN"

    :cellcolor "{key}={arg} .."
                Change the color of the current cell or range.
                Example:   :cellcolor "bg=CYAN fg=WHITE"
                           :cellcolor "fg=RED bold=1 underline=1"
                           :cellcolor A2:A6 "fg=CYAN bold=1 underline=1"

    :unformat
    :unformat {range}
                Removes a previous format set over a range.
                If not range is specified, it removes the format over current cell.

    :redefine_color "{color}" {R} {G} {B}
                Change the RGB values of the colors defined by ncurses.
                RGB values range from 0 to 1000.

                Note: This requires that ncurses is built with
                --enable-ext-colors, and the terminal must support 256 colors.
                For example, TERM=xterm-256color.  SC-IM must link to
                ncursesw library and not the common ncurses library.

                Example:   :redefine_color "RED" 700 100 100

                To make this take effect every time SC-IM is started, you can
                add it to $HOME/.scimrc:
                            REDEFINE_COLOR "RED" 700 100 100

                Redefining the BLACK color itself is another way to change the default
                background color of SC-IM.

    :lock       Lock the current cell or range.  Locked cells are immune to
                any type of editing and can't be changed in any way until
                unlocked.

    :unlock     Reverses the effect of ":lock", making the current cell or
                range editable.

    :valueize   Replace expressions in the current cell or range with the
                values evaluated from the expressions.

    :! {cmd}    Executes shell command {cmd}.

    :autojus {column}
    :autojus {column}:{column}
                Auto-resize the column or column range to fit their contents.

    :autojus    Auto-resize the columns covered by the selected cell or range.

    :trigger    Trigger action on cell or range. Trigger can be Read or Write
                or Both. On Read, trigger is executed before evaluating cells
                value, on Write, after the evaluation. Type of Trigger can be
                Lua or C. In Lua there are scim specific function available
                accessing cells, more in "examples/lua* directory.

                Example:
                :trigger a5 "mode=R type=LUA file=trg.lua function=trg"

                Triggers when ever cell a5 is read and calls function
                trg() in file trg.lua. In Lua column, row and mode is
                passed as parameter to the function. Mode is whether
                it was a READ or WRITE trigger.

                :trigger b10 "mode=W type=C file=trg.so function=wr2mysql"

                Function "wr2mysql" in trg.so is called when to
                cell b10 is writen a new value.
                See "examples/Module/module.c" for more Infos.
                Adding "-Wl,--export-dynamic" in Makefile for linking
                sc-im, will export all symbols from sc-im, making it
                available for dynamic linking with modules.

                The search path for LUA trigger files is
                $PWD/lua/ or $HOME/.scim/lua/ or /usr/local/share/scim/lua
                (in that order) and for C Trigger
                $HOME/.scim/module or /usr/local/share/scim/module


    :untrigger  Delete Trigger action on cell. Use with care.

    :fsum       Sum the numeric values of a range.

                The range is defined by the immediate cell above the current
                cell for vertical ranges, or by the immediate cell at the left
                of the current cell for horizontal ranges.

                The top or left corner is limited by the first non-numeric
                cell found.

    :fcopy      Copy the formula of a selected cell down a number of rows.
                The number of rows down is determined by the first empty cell
                in the column to the left of current cell.

                If a range is selected, the formula in the top left cell will
                be copied down to the end of the range.

    :fcopy {action}
                Copy the formulas of multiple selected cells into a direction.

                Use "c" or "columns" to copy every formula in the first
                selected row down its column, "r" or "rows" to copy every
                formula in the first selected column to the right in its row
                or "cells" to copy the formula of the first selected cell into
                all cells of the selected range.

    :plot {type}
                Plot a graphic using a selected range.
                Right now, only 'line', 'scatter', 'bar' and 'pie' types are allowed.

                Ex. of use:     :plot line
                This command calls gnuplot using the file called 'plotline'
                that is first looked in $HOME/.scim/, and if not found in
                /usr/local/share/scim/ (or HELPDIR path of Makefile).
                This 'plotline' can be customized by user. (See :plotedit
                command below). You can set terminal and other gnuplot
                parameters. Default terminal is 'dumb', although 'caca'
                terminal is recommended for colors and wide chars support.

    :plotedit {type}
                Edit a plot file that will be used for plotting.
                Can contain any gnuplot command.
                Right now, only 'line' type, 'scatter' type, 'bar' type and
                'pie' type files can be edited.

                Ex. of use:     :plotedit scatter

    c-r{a-zA-Z}
                If the character is a mark of a cell or range, the range
                represented is inserted into the command line.

                Command line history is stored in $HOME/.sciminfo.

    c-p
    <UP>        Go back in command line history.
                NOTE: if inputline is not empty, up and down keys recall older commands from history,
                but taking whose commands that beginning matches the current inputline content.

    c-n
    <DOWN>      Go forward in command line history.

==============================================================================
&VISUAL MODE& - Selecting a range

    Visual mode is used for selecting a range of cells for an operation.

    You can enter this mode with 'v' in Normal mode, or with <C-v> in Insert
    and Command mode.

    When entering Visual mode from Normal mode, the top left and the bottom
    right limit of the selected range is set to current row and column.

    From Insert or Command mode, press <C-v>, then position the cursor with
    arrow keys or hjkl keys, and then press <C-o> to begin selection.
    Move the cursor to complete the selection, then press <C-k> to input
    the range into the cell.

    The following motion commands move the cursor during selection:
    j k l h     Move down, up, right or left.
    0           Move to column A.
    $           Move forward to the last valid column of the current row.
    #           Move down to the last valid row of the current column.
    ^           Move up to row 0 of the current column.
    '{a-zA-Z}   Move to the cell or select the range marked previously with
                {a-zA-Z}.  See the 'm' command for details.
    c-f c-b     Increase selection down or up a full screen.
                :set half_page_scroll=1 to scroll by half a page instead.
                See :set command for details.
    c-a         Moves to first cell of spreadsheet.

    y           Yank the selected cell or range and exit Visual mode.
    x , dd      Delete the current range, saving its content to the
                yankbuffer.
    H           Move to the first row visible on screen.
    L           Move to the last row visible on screen.
    M           Move to the middle row visible on screen.
    w           Move forward to the next valid cell.
    b           Move back to the previous valid cell.
    G           Move to last valid cell of spreadsheet.

    :           Enters Command mode preserving the range selection, so a
                special command can be entered.
    Zr          Zap (hides) the rows covered by the selected range.
    Zc          Zap (hides) the columns covered by the selected range.
    Sr          Show rows that are hidden and that are covered by the selected
                range.
    Sc          Show columns that are hidden and that are covered by the
                selected range.
    { } |       Align the content of the cells covered by the selected range
                to the right, left or center.
    rl          Lock the current cell or range. Locking makes cells immune to
                any type of editing. A locked cell can't be changed in any
                way until it is unlocked.
    ru          Unlock a locked cell or range, making it editable.
    rv          Valueize the current cell or range. Valueizing removes
                expressions, leaving only the values.
    m{a-zA-Z}   Mark the current cell or selected range with that letter.
                Note: When a mark is changed, all ranges that use that mark
                are deleted.
    c-d         Convert the text content of a selected cell or range to a
                date, using default LOCALE's D_FMT format.
                This converts text to a numeric value that can be shown as a
                date. See DATE INPUT below for more info.
                Note: USELOCALE has to be enabled during build.
    c-j         Auto-resize the selected column(s) to accommodate the widest
                cells.

==============================================================================
&MAPPING&

    Mapping can be done in any SC-IM file or in a .scimrc file in the home
    directory.

    Maps can be added with the :nmap and :imap commands and removed with
    the :nunmap and :iunmap commands.
    Example:
        :nmap "d" ":h<cr>"  ->   Maps d to ':help<cr>' in Normal mode.
        :imap "f" "foo"     ->   Maps f to the string 'foo' in Insert mode.

    Some notes:
    The Left and Right sequence of a mapping cannot contain numbers.

    The <ESC> key cannot be mapped, but other special keys can.  They are:
    <CR> <C-x> <TAB> <LEFT> <RIGHT> <DOWN> <UP> <DEL> <BS> <HOME> <END>
    <PGDOWN> <PGUP>

    If an existing map sequence is remapped, it is replaced with the new one.
    Mapping is recursive by default. The non-recursive versions of :nmap and
    :imap are :nnoremap and :inoremap.
    Example:
        nmap "a" "b",
        nnoremap "b" "j"
        nmap "j" ":h<cr>"
    With this, 'a' maps to 'j', and only 'j' maps to ':h<cr>'.

==============================================================================
&COMMAND MULTIPLIER&

    An optional number may precede commands in Normal, Visual or Edit mode to
    multiply or iterate the command.
    Ex. '4j' in Normal mode, translates to 4 times 'j'.
    Ex. '4yr' in Normal mode, yanks current row and the 3 rows below it.

    Note: The 'x' command in Visual mode, and the shift commands in Visual
    mode and Normal mode when a range is selected, cannot be multiplied.

==============================================================================
&DATES INPUT&

    Dates are internally stored in SC-IM as numeric values, and they are
    displayed as dates if a date format is applied to the cells that store
    them.  Dates can be entered as a label and then converted to a numeric
    value with the :datefmt command. Another option is to enter the numeric
    value and apply a format with the :format special command.

    The :datefmt command takes the cell's text content that represents a date,
    and uses a given format to set the numeric value of the cell.
    Its format is ':datefmt "{strftime_format}"', taking a strftime-compatible
    format string.  The format is applied to the cell (as could be done with
    the :format function) so that the value is displayed as a date.

    Example:      :datefmt "%d/%m/%Y"

    The c-d command, used in Normal and Visual modes, acts as the :datefmt
    described above, but uses the locale's D_FMT format.

==============================================================================
&Other configuration variables&

    'autocalc'
    Set it to recalculate values automatically, or to '0' to do it manually
    upon execution of a '@' command.

    'numeric'
    Set it to '1' to make an initial digit start a numeric value.
    Set it to '0', to make a digit act as a command multiplier.

    'numeric_zero' [default off]
    'numeric_decimal' [default off]
    When these are set, the zero digit or decimal point will correspondingly
    initiate numeric entry, but only when 'numeric' is also set.

    'newline_action' [default 0]
    Set it to 'j' to move the cursor down after an entry.
    Set it to 'l' to move right, or set it to '0' to take no action.

    'external_functions' [default off]
    Disabled by default, set this variable to enable external functions.  See
    @ext function below.

    'overlap' [default off]
    If cell content exceedes column width it gets cut off to fit the column
    width.  If overlap is set, the content overflows into the next column.

    'debug' [default off]
    set this to see debug messages in screen

    'half_page_scroll' [default off]
    set this to scroll by half a page instead of full page.

    'xlsx_readformulas' [default off]
    If 'xlsx_readformulas' is set, SC-IM tries to import formulas, rather than
    the final values of a cell.

    'tm_gmtoff' [default -10800 seconds]
    set gmtoffset used for converting datetimes to localtime.

    'ignorecase' [default off]
    set this to ignore case in searches done with '/' command.

    'autobackup' [default 0 (no autobackup)]
    set this to a number in seconds 'n', to backup current file every 'n' seconds.
    AUTOBACKUP must be set during Sc-im build for this feature to be
    available.
    If you set this to 0 but AUTOBACKUP was set during build, it still will
    check for existance of backups before loading a file.

==============================================================================
&Built-in Range Functions&

    The following functions return the result of performing an operation on
    all valid (nonblank) entries in the given {range}. The optional second
    argument {expr} is an expression that is to be evaluated for each cell
    in the specified range to determine which cells to include in the function.
    Only those cells for which the expression evaluates to true (non-zero)
    will be used in calculating the value of the function.


    @sum({range})
    @sum({range},{expr})
        Sum up the values.
        examples with optional {expr} argument:
            @sum(D1:D20,D1>25)
            @sum(D1:D20,E1>25)
            @sum(D1:D20,@eqs(C1,"s"))

    @prod({range})
    @prod({range},{expr})
        Multiply the values together.

    @avg({range})
    @avg({range},{expr})
        Average the values.

    @count({range})
    @count({range},{expr})
        Count the values.

    @max({range})
    @max({range},{expr})
        Find the maximum value.
        See also the multi-argument version of @max below.

    @min({range})
    @min({range},{expr})
        Find the minimum value.
        See also the multi-argument version of @min below.

    @stddev({range})
    @stddev({range},{expr})
        Get the sample standard deviation of the values.

    @rows({range})
    @cols({range})
        Count the number of rows or columns.

==============================================================================
&Built-in Numeric Functions&

    @exp({expr})
        Return e (Euler's number) raised to the {expr} power.

    @ln({expr})
        Return the natural logarithm of {expr}.

    @log({expr})
        Return the base-10 logarithm of {expr}.

    @floor({expr})
        Return the largest integer not greater than {expr}.

    @ceil({expr})
        Return the smallest integer not less than {expr}.

    @rnd({expr})
        Round {expr} to the nearest integer.  Numbers halfway between integers
        are rounded up.

    @round({expr},{n})
        Round {expr} to {n} decimal places.  {n} may be positive to round off
        the right side of the decimal point or negative to round off the left
        side.  See @rnd({expr}) above for rounding types.

    @ascii("{se}")
        Interpret the string expression {se} as a base-256 number without
        digit 0 and convert to a base-10 nonnegative number.
        See also @chr.

    @frow({var})
        Return the row of the cell {var}. Ex. @frow(A4) returns 4

    @fcol({var})
        Return the number of the col of the cell {var}. Ex. @fcol(D4) returns 3

    @abs({expr})
    @fabs({expr})
        Return the absolute value of {expr}.

    @pow({expr1},{expr2})
        Return {expr1} raised to the power of {expr2}.

    @hypot({expr1},{expr2})
        Return @sqrt({expr1}*{expr1}+{expr2}*{expr2}), taking precautions
        against overflows.

    @pi
        Return a constant quite close to pi.

    @dtr({expr})
        Convert {expr} from degrees to radians.

    @rtd({expr})
        Convert {expr} from radians to degrees.

    @sin({expr})
    @cos({expr})
    @tan({expr})
        Evaluate the trigonometric functions on {expr}, in radians. The
        magnitude of the arguments are not checked to assure meaningful
        results.

    @asin({expr})
        Return the arc sine of {expr} in the range -pi/2 to pi/2.

    @acos({expr})
        Return the arc cosine of {expr} in the range 0 to pi.

    @atan({expr})
        Return the arc tangent of {expr} in the range -pi/2 to pi/2.

    @atan2({expr1},{expr2})
        Returns the arc tangent of e1/e2 in the range -pi to pi.

    @max({expr1},{expr2},...)
    @min({expr1},{expr2},...)
        Return the maximum or minimum of the values of the expressions. Two or
        more expressions may be specified.
        See also the range version of @max and @min above.

    @ston("{se}")
        Convert string expression {se} to a numeric value.

    @nval("{se}",{expr})
        Return the numeric value of a cell selected by name. String expression
        {se} must evaluate to a column name ("A" - "ZZ") and {expr} must
        evaluate to a row number (0 - maxrows, by default 65536).
        If {se} or {expr} is out of bounds, or the cell has no numeric
        value, the result is 0.
        You can use this for simple table lookups. See also @sval below.

    @eqs("{se1}","{se2}")
        Return 1 if string expressions {se1} and {se2} have the same value, 0
        otherwise.

    @slen("{se}")
        Returns the length of string expression {se}.



==============================================================================
&String Expressions&

    String expressions are made up of string constants (characters surrounded
    by double quotation marks), variables (cell names, which refer to the
    cell's label strings or expressions), and string functions.

    Note: String expressions are only allowed when entering a cell's label
    string, not its numeric part.  They are entered with a backslash followed
    by a double quote.
               Examples:  \"@coltoa(4)
                          \"A0 # "Plate"

    Note: String expression results may be left or right flushed or centered,
    according to the type of the cell's string label.

    #      Concatenate strings.
           For example, if the value of A0's string is "the la", then the
           string expression

               A0 # "zy dog"

           returns the string "the lazy dog".

==============================================================================
&Built-in String Functions&

    String functions can be entered typing \"

    @substr("{se}",{expr1},{expr2})
        Extract from string expression {se} the substring indexed by character
        number {expr1} through {expr2}. (Defaults to the length of {se} if
        greater than the length.)  If {expr1} is less than 1 or greater than
        {expr2}, the result is the null string.  For example,

        @substr ("River Plate", 4, 8)

        returns the string 'er Pl'.

    @upper("{se}")
    @lower("{se}")
        Convert the string expression {se} to uppercase or lowercase.

    @capital("{se}")
        Convert the initial letter of words in {se} to upper case and other
        letters to lower case.

    @replace("{se}","{eold}","{enew}")
        Replace occurrences of {eold} in {se} with {enew}.
        For example, having in A1 the string "Extension" and entering in A2
        the following:
        @replace(A1,"n","Z")
        will result "ExteZsioZ" in A2.

    @ext("{se}",{expr})
        Call an external program or script.  This allows arbitrary functions
        on values, e.g. table lookups and interpolations.  String expression
        {se} is a command or command line to call with popen(3).  {expr} is
        evaluated, converted to a string, and appended to the command line
        as an argument.  The result of @ex is a string: the first line printed
        to standard output by the command.  The command should emit exactly
        one output line.  Additional output, or output to standard error,
        messes up th  screen.  @ext returns a null string and prints an
        appropriate warning if external functions are disabled, {se} is null,
        or the attempt to run the command fails.

        External functions can be slow to run, and if enabled are called at
        each screen update, so they are disabled by default. Use the set
        command to enable them when needed.

        Example:
            @ext ("echo", a1)

        You can use @ston to convert the @ext result back to a number.

        Example:
            @ston (@ext ("form.sc.ext", a9 + b9))

        Note: You can build a command line (including more argument values)
        from a string expression with concatenation.  You can also "hide" the
        second argument by ending the command line (first argument) with a "#"
        shell comment.

    @coltoa({expr})
        Return a string name for a column from the numeric result of {expr}.

        Example:
            @coltoa(@mycol-1)      @nval(coltoa(@mycol-1), @myrow+1)

    @sval("{se}",{expr})
        Return the string value of a cell selected by column and row.  String
        expression {se} must evaluate to a column name (A - AE) and {expr}
        must evaluate to a row number (0 - 199).  If {se} or {e} is out of
        bounds, or the cell has no string value, the result is the null
        string.

    @set8bit("{se}")
        Return the string "{se}" with 8th bit set.

    @chr({expr})
        Interpret {expr} as a base-10 nonnegative integer and convert to a
        string (base-256 number without digit 0).
        See also @ascii.

    @lua("luascript",0)
        Executes a "luascript". Using Lua script scim can be extend with lot
        new functionality, such as complex programming, accessing databases etc.
        The search patch for LUA scripts files is $PWD/lua/
        $HOME/.scim/lua/ or /usr/local/share/scim/lua (in that order)
        Always use it only with @ston see example:
        @ston(@lua("luascript",0))

==============================================================================
&Built-in Date and Time Functions&

    The following functions operate on an expression {date_expr} denoting a
    UNIX timestamp.

    @year({date_expr})
        Return the year. Valid years begin with 1970, although many systems
        will return years prior to 1970 if e is negative. The last legal year
        is system dependent.

    @month({date_expr})
        Return the month, encoded as 1 (January) to 12 (December).

    @day({date_expr})
        Return the day of the month, encoded as 1 to 31.

    @hour({date_expr})
        Return the number of hours since midnight, encoded as 0 to 23.

    @minute({date_expr})
        Return the number of minutes since the last full hour, encoded as 0 to
        59.

    @second({date_expr})
        Return the number of seconds since the last full minute, encoded as 0
        to 59.

==============================================================================
&Other functions&
    @if({expr}, {expr}, {expr})
        Conditional:   If the  first  expression  is  true  then  the  value  of
        the  second  is  returned,  otherwise the  value  of  the  third.
        example of use: @if(@eqs(A1,"a"),B1,0)
        example of use with string expression: @if(A1>100,"over","not enough")
        Remember string expressions should be entered by typing \"


==============================================================================
&LUA Scripts and Triggers&
     SC-IM was extended with LUA capabilities and also provided with helper
     Function for manipulate SC-IM data with Lua at runtime. Since it is a
     fully functional Lua, you can use all Lua packages also for sc-im lua
     scripts. Use luarocks to install additional packages.

     Function provided to lua script/triggers :

     sc.lgetnum (c, r)       - get numeric value of cell c,r (c/r is number column/row)
                               returns value
     sc.lsetnum (c, r, val)  - set numeric value to a cell c,t
     sc.lsetform (c, r, str) - set formula to a cell. Basically it does "let cell= str"
     sc.lsetstr(c, r, str)   - set string to a cell
     sc.lgetstr(c, r, str)   - get string from a cell
     sc.lquery(str)          - query input from user, but first prints str. Use with care!!
                               Dont use this function within triggers!!
                               returns string
     sc.sc(str)              - send str to sc-im parser
     sc.a2colrow(str)        - convert ascii cell representation to numeric column/row
                               returns column, row example:
                               c,r=sc.a2colrow("c5")
     sc.colrow2a(c,r)        - returns ascii representation of numeric column/row
     sc.maxcols()            - return current maximum columns
     sc.maxrows()            - return current maximum rows
     sc.curcol()             - return current column
     sc.currow()             - return current row

     The search patch for LUA scripts files is $PWD/lua or
     $HOME/.scim/lua/ or /usr/local/share/scim/lua (in that order)
     Example can be found in sc-im/examples/lua in source code tree.


==============================================================================
&Supported file formats / File import&

    SC-IM can open the following file formats:
        .sc     SC-IM's native text format
        .xls    Microsoft Excel Spreadsheet
        .xlsx   Microsoft Office Open XML Workbook
        .csv    Comma-separated values
        .tsv    Tab-separated values
        .tab    Tab-separated values
        .txt    Simple text files

    You can pass files of any of the above formats to SC-IM binary.
    If you pass a .txt or .csv file to SC-IM, it is imported using a comma as
    the delimiter.
    If you pass a .tsv or .tab file to SC-IM, it is imported using the tab
    character as the delimiter.

    Note: You can always override the delimiter used passing the --txtdelim
    parameter to SC-IM.

    Example: ./sc-im --txtdelim="\t" file.txt

    Possible values are:
        --txtdelim="\t"
        --txtdelim=","
        --txtdelim=";"

    If you pass a .xlsx file to SC-IM, you can specify which sheet to load
    with the --sheet parameter, which can be the name or number of a sheet.
    Default value is 1.

    Example: ./sc-im --sheet=dogs file.xlsx

    Some possible values are:
        --sheet=3
        --sheet=dogs

==============================================================================
&External scripts&

    SC-IM can read data from a external script, either through a pipeline or
    redirection.
    This enables SC-IM to be used as a non-interactive calculator.

    It can also be run interactively without the ncurses interface if you pass
    the --nocurses flag.

    You can set the --output parameter to save the results to a file.

    If you set the --quit_afterload flag, SC-IM will quit after loading all
    files, but before becoming interactive.

    Suppose you have a file called "script" with the following content:
        let A2=0
        let A3=A2+14
        recalc
        getnum A3

    The following invocations demonstrate SC-IM's input and output options.

    Output to stdout, then quit:
        cat script | ./sc-im --nocurses --quit_afterload

    Receive data from a pipe and output results to a file:
        cat script | ./sc-im --quit_afterload --output=return_file

    Receive data from a pipe and continue in non-ncurses mode:
        cat script | ./sc-im --nocurses

    Read data from a script and output to a file:
        ./sc-im a.sc --quit_afterload --output=return_file

    Receive data from both a pipe and a script, and output to file:
        cat script | ./sc-im a.sc --quit_afterload --output=return_file

    Start interactive mode but with no ncurses interface:
        ./sc-im --nocurses

    Note: Setting the --output parameter implies setting the --nocurses flag.

 vim:tw=78:ts=8:ft=help:norl:
