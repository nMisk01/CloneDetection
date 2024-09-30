UNIVERSAL_NODES = {
    'FILE',  # File node
    'SCRIPT',  # Script node
    'IDENTIFIER',  # Actual name for functions, classes, variables, etc
    'DEFINE',  # Define preprocessor #define directive
    'INCLUDE',  # Define preprocessor #include directive
    'STRUCT',  # Define struct declaration, composite data type
    'UNION',  # Define union declaration, different variable datatype collection
    'MALLOC',  # Define malloc function for dynamic memory allocation
    'FREE',  # Define free function to release dynamic memory
    'CALLOC',  # Define calloc function for dynamic memory allocation
    'REALLOC',  # Define realloc function for dynamic memory reallocation
    'SIZEOF',  # Define sizeof operator
    'CLASS_DECL',  # Class declaration
    'CONSTRUCTOR_DECL',  # Constructor declaration
    'PARAMETER_LIST',  # List of parameters for everything
    'PARAMETER',  # Node that identifies a single parameter
    'CONSTRUCTOR_CALL',  # Create new object from constructor
    'CLASS_BODY',  # Defines a body for a class
    'CLASS_MEMBER',  # Define a member of a class
    'ENUM_DECL',  # Define a enumeratio
    'ENUM_BODY',  # Defines a enumeration body
    'POINTER',  # Define pointer dereferencing operator
    'ADDRESS_OF',  # Define address-of operator (&)
    'POINTER_ARITHMETIC',  # Define pointer arithmetic operations
    'MULTI_DIMENSIONAL_ARRAY',  # Define multi-dimensional array access
    'FUNCTION_DECL',  # Function declaration
    'FUNCTION_BODY',  # Define the body function
    'FUNCION_CALL',  # Define a function call
    'FUNCTION_POINTER', # Define a function pointer
    'RETURN', # Define a return statement for a function
    'ATTRIBUTE_DECL',  # Attribute declaration
    'VARIABLE_DECL',  # Variable declaration
    'GETTER',  # Getter declaration
    'SETTER',  # Setter declaration
    'TYPE_ALIAS',  # Define a type alias, shorter name type that can be created
    'PARAMETER_TYPE',  # Define the type of a parameter
    'TYPE',  # Define a type
    'NULLABLE_TYPE',  # Define a nullable type
    'FUNCTION_TYPE',  # Define a function type
    'USER_TYPE',  # Define a user type
    'OR',  # Define conjuction || conjuction
    'AND',  # Define something && something
    'XOR', # Define bitwise OR | bit reversal
    'BITWISE_AND',  # Define bitwise AND operator
    'BITWISE_OR',  # Define bitwise OR operator
    'BITWISE_XOR',  # Define bitwise XOR operator
    'BITWISE_NOT',  # Define bitwise NOT operator
    'TERNARY',  # Define a ternary/elvis operation
    'AS',  # Define as expression - casting
    'PREFIX',  # Define a prefix operation ++, --, +=, -=, etc.
    'POSFIX',  # Define a posfix operation ++, --, !, etc
    'COLLECTION_INDEXING',  # Index an array
    'VALUE_ARGUMENT_LIST',  # List of arguments used for a call
    'VALUE_ARGUMENT',  # Value argument ^^
    'TYPE_ARGUMENT_LIST',  # List of type arguments <Type1, Type2>
    'TYPE_ARGUMENT',  # Type Argument ^^ 
    'STRING',  # Define a String literal
    'COLLECTION',  # Define a collection, can be an array, etc
    'SUPER_CALL',  # Defines a call to super
    'CONDITION',  # Defines a condition, if, when, switch, etc
    'BODY',  # Defines the body of a control structure: for, while, if, etc
    'TRY',  # Defines a try block
    'CATCH',  # Defines a catch block
    'FINALLY',  # Defines a finally block
    'LOOP_STATEMENT',  # Defines loop statement for, while, dowhile
    'JUMP_STATEMENT',  # Defines jump statement break, continue, return
    'EQUALITY_OPERATOR',  # Define an equality operation == !==
    'COMPARISON_OPERATOR',  # Define a comparison operation >, <
    'MEMBER_OF',  # Define if x is IN container or NOT IN
    'IS_TYPE',  # Define if x IS of type or NOT IS
    'ADDITIVE_OPERATOR',  # Define an additive/subtraction operation
    'MULTIPLICATIVE_OPERATOR',  # Define a multiplication/division/modulus
    'LOGICAL_OPERATOR',  # Define a logical operator like not, !
    'ACCESS_OPERATOR',  # Define an access operator like '.' or '::'
    'VISIBILITY_MODIFIER',  # Define the visibility public, private, protected
    'CONST_DECL',  # Declare a constant , cons keyword
    'INHERITANCE_MODIFIER',  # Declare if the inheritance is abstract, final
    'LITERAL',  # Defines the value of a constant, integer, boolean, etc
    'ASSIGNMENT_OPERATOR',  # Give value to a variable var x = 3
    'EXPRESSION',  # Define a expression of the language, if, for, while, condition, etc
    'THROW',  # Define a throw exception expression
    'THIS',  # Define a this, self expression
    'AWAIT_EXPRESSION',  # Define an await expression
    'ASSERT',  # Define assert expression
    'ATOMICS',  # Define atomic operations in C11 (_Atomic)
    'THREADS',  # Define threading support in C11 (threads.h)>
    'GENERIC',  # Define generic macros (_Generic in C11)
    'STATIC_ASSERT',  # Define static assertion support in C11 (_Static_assert)
    'ALIGNOF',  # Define alignment support in C11 (alignof)
    'ALIGNAS',  # Define alignment specifier in C11 (_Alignas)
}
#Copy of universal_nodes.py that accomodates the needed C support 