#!/usr/bin/env python
# coding: utf-8

# In[2]:
#Day17

def get_student_info():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = float(input("Enter student grade: "))
    return name, age, grade

student_info = get_student_info()
print("Student Information:")
print("Name:", student_info[0])
print("Age:", student_info[1])
print("Grade:", student_info[2])


# In[3]:


# Mapping colors to their RGB values using tuples
color_dict = {('red', 255, 0, 0): 'FF0000', ('green', 0, 255, 0): '00FF00', ('blue', 0, 0, 255): '0000FF'}

for color, hex_code in color_dict.items():
    print(f"{color}: {hex_code}")


# In[4]:


# List of tuples containing student names and their scores
students = [("Alice", 90), ("Bob", 85), ("Charlie", 95)]

# Unpacking tuple in a loop
for name, score in students:
    print(f"{name} scored {score} marks.")


# In[5]:


# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result_tuple = tuple1 + tuple2

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Concatenated Tuple:", result_tuple)


# In[6]:


def calculate_circle_properties(radius):
    circumference = 2 * 3.14 * radius
    area = 3.14 * (radius ** 2)
    return circumference, area

circle_radius = float(input("Enter the radius of the circle: "))
circle_circumference, circle_area = calculate_circle_properties(circle_radius)

print("Circle Circumference:", circle_circumference)
print("Circle Area:", circle_area)


# In[ ]:




