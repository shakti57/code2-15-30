#!/usr/bin/env python
# coding: utf-8

# In[2]:


def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index).

    BMI = weight (kg) / (height (m))^2
    """
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret BMI and provide a basic classification.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Get user input for weight and height
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi_result = calculate_bmi(weight, height)

# Interpret and display the result
classification = interpret_bmi(bmi_result)
print(f"Your BMI is {bmi_result:.2f}. You are classified as {classification}.")


# In[ ]:




