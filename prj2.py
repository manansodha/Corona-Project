import pandas as pd
import matplotlib.pyplot as plt
import csv
import os

main_menu = '''
Main Menu

1. To Enter New Data
2. To Change
3. To Display Data
4. To Analyse Data
5. To delete Data
6. Exit'''

display = '''
Data Display Menu

1. All Data
2. Top Five Records
3. Bottom Five Records
4. Specific Date Records
5. Display Selected Columns
6. Return To Main Menu'''

analysis = '''
Data Analysis Menu

1. Histogram Chart(Total Cases)
2. Bar Chart(Date/Active Cases)
3. Line Chart(Date/Recovered)
4. Histogram chart(Date/Recovered and Active Cases)
5. Return To Main Menu
'''


def data_display():
    df = pd.read_csv('C:\\Users\\Manan\\Desktop\\prj\\cov_gj2.csv',
                     names=['Date', 'Total_Cases', 'Active_Cases', 'Recovered', 'Deaths'],
                     skiprows=1)
    while True:
        print(display)
        print()
        ip = int(input("Enter Choice: "))
        print()
        if ip == 1:
            print(df)
        elif ip == 2:
            print(df.head(5))
        elif ip == 3:
            print(df.tail(5))
        elif ip == 4:
            n = input('\nEnter the date for search(DD\MM\YYYY):')
            df1 = df[df.Date == n]
            if df1.empty:
                print('\nNo Data Available for', df1)
            else:
                print(df1)
            print()
        elif ip == 5:
            print('\nList of Columns are')
            for i in df.columns:
                print(i, end=', ')
            cols = []
            while True:
                cols_ = input('\nEnter the column name(Case sensitive): ')
                cols.append(cols_)
                x = input('Want to select more columns?(y/n): ')
                if x in 'Nn':
                    break
            print('Records in the selected columns -> ')
            print(df[cols])
            print()
        else:
            break


def data_input():
    with open('C:\\Users\\Manan\\Desktop\\prj\\cov_gj2.csv', mode='w') as pj_file:
        pj_writer = csv.writer(pj_file, delimiter=',')
        a = int(input("Number of entries: "))
        df = pd.read_csv('C:\\Users\\Manan\\Desktop\\prj\\cov_gj2.csv',
                         names=['Date', 'Total_Cases', 'Active_Cases', 'Recovered', 'Deaths'],
                         skiprows=1)
        for i in range(a):
            d1 = input("Enter the last date of entry(DD\MM\YYYY)")
            d2 = input("Enter the date(DD\MM\YYYY): ")
            b = int(input("Number of new cases: "))
            c = int(input("Patients recovered: "))
            d = int(input("Number of deaths: "))
            c_t = df.at[d1, 'Total_Cases'] + b
            c_a = df.at[d1, 'Active Cases'] + b - c - d
            c_r = df.at[d1, 'Recovered'] + c
            c_d = df.at[d1, 'Deaths'] + d
            ab = [d2, c_t, c_a, c_r, c_d]
            pj_writer.writerow(ab)
            print()
    df = pd.read_csv('C:\\Users\\Manan\\Desktop\\prj\\cov_gj2.csv',
                     names=['Date', 'Total_Cases', 'Active_Cases', 'Recovered', 'Deaths'])
    print(df)


def data_append():
    with open('C:\\Users\\Manan\\Desktop\\prj\\cov_gj2.csv', mode='a') as pj_file:
        pj_writer = csv.writer(pj_file, delimiter=',')
        df = pd.read_csv('C:\\Users\\Manan\\Desktop\\prj\\cov_gj2.csv',
                         names=['Date', 'Total_Cases', 'Active_Cases', 'Recovered', 'Deaths'],
                         skiprows=1)
        d1 = input("Enter the last date of entry(DD\MM\YYYY): ")
        d2 = input("Enter the date(DD\MM\YYYY): ")
        b = int(input("Number of new cases: "))
        c = int(input("Patients recovered: "))
        d = int(input("Number of deaths: "))
        c_t = df.loc[d1].at['Total_Cases'] + b
        c_a = df.loc[d1].at['Active_Cases'] + b - c - d
        c_r = df.loc[d1].at['Recovered'] + c
        c_d = df.loc[d1].at['Deaths'] + d
        ab = [d2, c_t, c_a, c_r, c_d]
        pj_writer.writerow(ab)
        print()

    df.pd.read_csv('C:\\Users\\Manan\\Desktop\\prj\\cov_gj2.csv', header=None)
    print(df)


def data_analysis():
    df = pd.read_csv('C:\\Users\\Manan\\Desktop\\prj\\cov_gj2.csv',
                     names=['Date', 'Total_Cases', 'Active_Cases', 'Recovered', 'Deaths'],
                     skiprows=1)
    while True:
        print(analysis)
        print()
        a = int(input("Enter the choice: "))
        print()
        if a == 1:
            df.plot.hist('Total_Cases', bins=10000, color='b')
            plt.xlabel('Total Cases')
            plt.title('Total Number of Cases', fontsize=16)
            plt.show()
        elif a == 2:
            df.plot.bar('Date', 'Active_Cases', width=0.15, color='g')
            plt.xlabel('Date')
            plt.ylabel('Active cases')
            plt.title('Date v/s Active', fontsize=16)
            plt.grid()
            plt.show()
        elif a == 3:
            df.plot('Date', 'Recovered', width=0.15, color='g')
            plt.xlabel('Date')
            plt.ylabel('Recovered')
            plt.title('Date v/s Recovered', fontsize=16)
            plt.grid()
            plt.show()
        elif a == 4:
            df.plot.hist(['Active_Cases', 'Recovered'], bins=10000, histtype='barstacked')
            plt.title('Date v/s Recovered and Active Cases', fontsize=14)
            plt.grid()
            plt.show()
        else:
            break


def data_remove():
    df = pd.read_csv('C:\\Users\\Manan\\Desktop\\prj\\cov_gj2.csv',
                     names=['Date', 'Total_Cases', 'Active_Cases', 'Recovered', 'Deaths'])
    print(df)
    n = int(input('Enter the row index number for deletion ->  '))
    df.drop(n, inplace=True)
    print()
    print(df)
    print()
    print('Record deleted from Data Frame')
    print()
    print()
    ch = input("Do you want to change data in the Csv file?(Y/N) ")
    if ch in 'yY':
        df.to_csv(r'C:\Users\Manan\Desktop\prj\cov_gj.csv', index=False, sep=',')
        print('\nData changed in [new_1.csv] file.........\n\n')

    os.remove("C:\\Users\\Manan\\Desktop\\prj\\cov_gj2.csv")
    os.rename(r'C:\Users\Manan\Desktop\new_2.csv', r'C:\Users\Manan\Desktop\cov_gj2.csv')


while True:
    print(main_menu)
    choice = int(input("Enter choice: "))
    print()
    if choice == 1:
        data_input()
    elif choice == 2:
        data_append()
    elif choice == 3:
        data_display()
    elif choice == 4:
        data_analysis()
    elif choice == 5:
        data_remove()
    elif choice == 6:
        print('Closing the project...'
              'Good Bye')
        break
