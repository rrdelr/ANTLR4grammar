// TODO: From typing import list

/// Gramatica Final, Lenguajes de Programacion
// Del Rio, Imbett

grammar grammatica;

expr: ddl       # ddlExpr
    | dql       # dqlExpr
    | sql       # sqlExpr
    | atom=INT  # numberExpr
    | atom=STR  # strExpr
    ;

/// DDL EXPRESSIONS

ddl:    create
       | drop
       | alter
       | truncate
       | rename
       ;

//create: 'CREATE' expr '(' middle=mittlal* terminal ')';
create: 'CREATE' name=expr '(' pair=terminal ')';
drop: 'DROP' name=expr;
alter: 'ALTER' name=expr 'ADD' '(' pair=terminal ')';
truncate: 'TRUNCATE' name=expr;
rename: 'RENAME' oldname=expr 'TO' newname=expr;

/// DDL AUXILIARIES

//mittlal: key=expr ':' value=expr ',';
terminal: key=expr ':' value=expr;

/// DQL EXPRESSIONS

dql: select;

select: 'SELECT' key=expr 'FROM' name=expr;

/// SQL EXPRESSIONS

sql:     insert
       | update
       | delete
       ;

//insert: 'INSERT' 'INTO' name=expr '(' smallmittlal* smallterminal')' 'VALUES' '(' smallmittlal* smallterminal ')';
insert: 'INSERT' 'INTO' name=expr '(' key=smallterminal')' 'VALUES' '(' value=smallterminal ')';
update: 'UPDATE' name=expr 'SET' key1=expr '=' key1value=expr 'WHERE' key2=expr '=' key2value=expr;
delete: 'DELETE' 'FROM' name=expr 'WHERE' key=expr '=' value=expr;

/// SQL AUXILIARIES

//smallmittlal: value=expr ',';
smallterminal: value=expr;

/// DATATYPES

STR         : '"' .*? '"' ;
INT         : [0-9]+;
WS          : [ \t]+ -> skip ;
