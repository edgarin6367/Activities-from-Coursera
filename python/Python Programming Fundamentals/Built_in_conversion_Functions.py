# Start with the provided variables int_value, float_value, and text_value.
int_value = 15
float_value = 4.1
text_value = "33"

# Use the type() function to save the data type of float_value in the variable type_of_float_value where it says STEP 2: YOUR CODE HERE. The type function can be used to determine the data type of variables, and can be used to avoid errors and exceptions.
type_of_float_value = type(float_value)
# Use the int() function to convert the value of text_value to an integer and store in the variable text_value_as_int where it says STEP 3: YOUR CODE HERE. Even if a string holds a numeric value, it must be converted to a numeric value (int or float) to be used as part of mathematical operations.
text_value_as_int = int(text_value)
# Use the str() function to convert the value of int_value to a string and store in the variable int_value_as_text where it says STEP 4: YOUR CODE HERE. Often times, numeric values that will not have mathematical operations performed on them (for example, credit card numbers, serial numbers, American ZIP codes) will be converted to text.
int_value_as_text = str(int_value)
# The results will print. You will see the data type of the float variable, followed by the results of adding two numeric values, followed by the results of adding those same two values as strings.
print("Float_value type:", type_of_float_value)
print("INteger addition: adding text_value_as_int (33) to int_value (15):", text_value_as_int + int_value)
print("Text addition: adding text_value (33) to int_value_as_text (15):", text_value + int_value_as_text)