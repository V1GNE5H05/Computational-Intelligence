% Arithmetic Operations
add(X, Y, R) :- R is X + Y.
subtract(X, Y, R) :- R is X - Y.
multiply(X, Y, R) :- R is X * Y.
divide(X, Y, R) :- R is X / Y.

% Menu Display
show_menu :-
    nl,
    write('1. Addition'), nl,
    write('2. Subtraction'), nl,
    write('3. Multiplication'), nl,
    write('4. Division'), nl,
    write('5. Exit'), nl,
    write('Enter choice: ').

% Start
start :-
    repeat,
    show_menu,
    read(Choice),
    ( Choice == 5 ->
        write('Bye!'), nl, !
    ;
        write('Enter first number: '), read(X),
        write('Enter second number: '), read(Y),
        perform_operation(Choice, X, Y),
        fail
    ).

% Operations
perform_operation(1, X, Y) :- add(X, Y, R),      write('Answer = '), write(R), nl.
perform_operation(2, X, Y) :- subtract(X, Y, R),  write('Answer = '), write(R), nl.
perform_operation(3, X, Y) :- multiply(X, Y, R),  write('Answer = '), write(R), nl.
perform_operation(4, X, Y) :- divide(X, Y, R),    write('Answer = '), write(R), nl.