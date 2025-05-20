#Analyzing Antarctic Temperatures  
#Begin with the antarctic_temperatures list, which contains the daily temperature recordings.
antartic_temperatures = [20.3, 25.9, 30.0, 26.7, 24.7]
# Apply the max() function to the antarctic_temperatures list to obtain the highest temperature recorded.
highest_temperature = max(antartic_temperatures)
# Apply the min() function on the antarctic_temperatures list to determine the lowest temperature recorded.
lowest_temperature = min(antartic_temperatures)
# Print the highest and lowest temperatures.
print("Highest temperature:", highest_temperature, "°C")
print("Lowest temperature: ", lowest_temperature, "°C")
# Calculate the average temperature by summing all temperatures in the antarctic_temperatures list using the sum() function and dividing by the number of temperatures, which you can determine using the len() function. Round the calculated average temperature to one decimal place using the round() function.avg
avg_temp = round(sum(antartic_temperatures) / len(antartic_temperatures), 1)
# Print the rounded average temperature.
print("Average temperature: ", avg_temp, "°C")
# Calculate the absolute value of the coldest temperature using the abs() function.
coldest_temperature_abs = abs(lowest_temperature)
# Print the absolute value of the coldest temperature.
print("The coldest temperature was", coldest_temperature_abs, "°C below freezing.")
