```pseudocode
// Task 7 - Walking Directories
//Name: Grace Garrett
//Date: 20/04/2026

BEGIN

    // Get and validate the directory path
    REPEAT
        PRINT "Enter a directory path: "
        INPUT path
    UNTIL path is a valid directory

    // Call the recursive function
    CALL list_files(path)

END

FUNCTION list_files(directory):

    // Get all items in the current directory
    SET items = GET_CONTENTS(directory)

    // Loop through each item
    FOR EACH item IN items DO

        SET full_path = directory + "/" + item

        IF item is a file THEN
            // Print the full path of the file
            PRINT full_path

        ELSE IF item is a directory THEN
            // Recursively call the function on the subdirectory
            CALL list_files(full_path)

        END IF

    END FOR

END FUNCTION

```
