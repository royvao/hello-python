# Variables
my_variable_string = 'My String variable'
print(my_variable_string)

my_variable_int = 6
print(my_variable_int)

my_variable_int_to_str = str(my_variable_int)
print(my_variable_int_to_str)
print(type(my_variable_int_to_str))

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables de distinto tipo en un print
print(my_variable_string, my_variable_int_to_str, my_bool_variable)

# Funciones del sistema
print(len(my_variable_string))

# Variables en una línea
name, surname, alias, age = "Roy", "Vao", 'LambdaR', 25
print("Me llamo", name, surname, ". Tengo", age, "años, y mi alias es", alias)
