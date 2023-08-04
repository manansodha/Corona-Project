# Corona Project
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)


Hi there! This here is my high school project which I made in 2020. This is a simple program which is on the borders of data analytics field. Why? Because one can store and add data, modify data, delete data and especially graphically represent the data which can be easily interpreted.

The main application of this project is that user is able to enter details regarding number covid patients, healed and deaths in date-wise manner and also, provide the user graphical representation of the trends created using the data that is given.

## Basic information regarding the project 
* This is a terminal based application with simple UI of menus.
* There are three menus with easy manuverability among each of them.
  * The first/main menu is the one where use can select what they want to do with the data or if the want to exit.
    ```
    Main Menu

    1. To Enter New Data
    2. To Change
    3. To Display Data
    4. To Analyse Data
    5. To delete Data
    6. Exit
    ```
  * The second menu is the reading menu, i.e., this will show options to disply data or go back to the main menu.
    ```
    Data Display Menu
    
    1. All Data
    2. Top Five Records
    3. Bottom Five Records
    4. Specific Date Records
    5. Display Selected Columns
    6. Return To Main Menu
    ```
  * The third menu is the analytics menu, from where the user can choose different types of charts with different datasets.
    ```
    Data Analysis Menu
 
    1. Histogram Chart(Total Cases)
    2. Bar Chart(Date/Active Cases)
    3. Line Chart(Date/Recovered)
    4. Histogram chart(Date/Recovered and Active Cases)
    5. Return To Main Menu
    ```

  * As the whole application is terminal based, the user has to input the index value of the corresponding option they want to choose.
* The data for this application is stored in csv format, which helps with portability and operations such as read/write can be easliy performed on the it. Also, new data can be import easily without any compatibility issues.
* The data analysis part of the application shows the user the graphical representation of the data as per the user's requirement and the pre-defined options.

## Libraries used in the project are:
* CSV: Which helps with csv files such reading, writing etc.
* Pandas: Which can be used to convert data in series or dataframe which has index and columns to represent data the data.
* Pyplot from Matplot: Which helps with the visualisation. There are many different types of graphs which can be made such as bar chart, line graph, histogram etc.
* OS: Which can help in making change in the system.
```python
import csv
import pandas as pd
import matplotlib.pyplot as plt
import os
```
## Data format and how to work with it
The data used for the project which is stored in form of comma separated values (CSV), and it has the following column headers:
- Date
- New Cases
- Active Cases
- Recovered
- Deaths
The data can be viewed in the [CSV file](cov_data.csv)

## Getting Started
To get started, follow these steps:

* Clone this repository: git clone https://github.com/manansodha/Corona-Project.git
* Navigate to the repository: cd supervised-machine-learning
* Install the required dependencies: pip install -r requirements.txt

## Contributions
Contributions are welcome and encouraged! Whether you want to add more features, improve existing code, or fix bugs, your help is appreciated.
