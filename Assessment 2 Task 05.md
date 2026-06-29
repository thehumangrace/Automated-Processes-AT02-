```pseudocode
//Task 5 - Relationship Between Circles
//Name: Grace Garrett
//Date: 23/04/2026

BEGIN

    // Get and validate inputs
    REPEAT
        PRINT "Enter the radius of Circle A: "
        INPUT radius_A
        IF radius_A is not a number THEN
            PRINT "Invalid input. Please enter a number."
        ELSE IF radius_A <= 0 THEN
            PRINT "Invalid input. Radius must be a positive number."
        END IF
    UNTIL radius_A is a valid positive number

    
    REPEAT
        PRINT "Enter the radius of Circle B: "
        INPUT radius_B
        IF radius_B is not a number THEN
            PRINT "Invalid input. Please enter a number."
        ELSE IF radius_B <= 0 THEN
            PRINT "Invalid input. Radius must be a positive number."
        END IF
    UNTIL radius_B is a valid positive number

    
    REPEAT
        PRINT "Enter the distance between the centres: "
        INPUT D
        IF D is not a number THEN
            PRINT "Invalid input. Please enter a number."
        ELSE IF D < 0 THEN
            PRINT "Invalid input. Distance cannot be negative."
        END IF
    UNTIL D is a valid non-negative number

    // Convert inputs from strings to integers
    SET radius_A = TO_INTEGER(radius_A)
    SET radius_B = TO_INTEGER(radius_B)
    SET D = TO_INTEGER(D)

    
    // Determine the relationship
    IF (D + radius_A) < radius_B THEN
        PRINT "Circle A is inside Circle B"
    
    ELSE IF (D + radius_B) < radius_A THEN
        PRINT "Circle B is inside Circle A"
    
    ELSE IF (radius_A + radius_B) > D AND D > ABS(radius_A - radius_B) THEN
        PRINT "The circles are overlapping"
    
    ELSE
        PRINT "The circles do not overlap"
    
    END IF

END
```
