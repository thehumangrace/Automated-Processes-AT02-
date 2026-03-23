Author: Grace Garrett

Student ID: 13260436

Date Last Modified: 19/03/2026

'''mermaid

graph TD
    A([Start]) --> B[/Input positive integer n/]
    B --> C[Set counter = 0]
    C --> D{Is n > 1?}
    D -- No --> E[Print final n and counter]
    E --> F([End])
    D -- Yes --> G[Print n]
    G --> H{Is n even?}
    H -- Yes --> I[n = n / 2]
    H -- No --> J["n = (n * 3) + 1"]
    I --> K[Increment counter by 1]
    J --> K
    K --> D

'''

%% graph td - Draw a flowchart from Top Down

%% ([Start]) and ([End]) - Gives rounded edges 

%% [/Input/]  - Makes parallelograms for operations

%% {Is n even?} - Diamond if/else logic

%% [Process] - Rectangle calculations 

%% K --> D - The while loop arrow 
