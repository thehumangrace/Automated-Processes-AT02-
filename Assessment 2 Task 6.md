```pseudocode
// Task 6 - Bubble Sort
//Name: Grace Garrett
//Date: 20/04/2026

BEGIN

    // Get the list to sort
    PRINT "Enter a list of numbers: "
    INPUT list
    SET n = LENGTH(list)

    // Outer loop - runs n-1 passes
    FOR i FROM 0 TO n - 1 DO

        SET swapped = FALSE

        // Inner loop - compares adjacent elements
        FOR j FROM 0 TO n - i - 2 DO

            IF list[j] > list[j + 1] THEN
                // Swap the two elements
                SET temp = list[j]
                SET list[j] = list[j + 1]
                SET list[j + 1] = temp
                SET swapped = TRUE
            END IF

        END FOR

        // If no swaps were made, the list is already sorted
        IF swapped = FALSE THEN
            BREAK
        END IF

    END FOR

    PRINT "Sorted list: " + list

END
```
