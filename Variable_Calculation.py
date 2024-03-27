#Here I will give an example of a calculation, for a month-to-month variable in percentage.
#You can use this calculation to compare your data on the dashboard.
#The code will print as a percentage, this can be useful for analyzing the performance of the current period, over the previous period.

#1 Create a Measure for the Current Value: Ex Measure in DAX

Current Sales = SUM('SalesTable'[SalesValue])

#1 Create a Measure for the Current Value: Ex Measure in PYTHON

import pandas as pd

sales_table = pd.read_csv("sales_table.csv")

current_sales = sales_table["SalesValue"].sum()

print(current_sales)


#2 Create a Measure for the Previous Month's Amount:  Ex Measure in DAX

Previous Month Sales = CALCULATE(
     SUM('SalesTable'[SalesValue]),
     SAMEPERIODLASTYEAR('SalesTable'[SalesDate])
)


#2 Create a Measure for the Previous Month's Amount:  Ex Measure in PYTHON

import pandas as pd

def sales_previous_month(sales_table):
   """
   Calculates sales from the previous month.

   Arguments:
     sales_table: Pandas DataFrame with the "SalesData" and "SaleValue" columns.

   Returns:
     The total sales for the previous month.
   """

   previous_month = pd.to_datetime('today') - pd.offsets.MonthBegin(1)

   sales_previous_month = sales_table.loc[
       mesa_vendas['DataSales'].dt.month == month_previous.month,
       'SaleValue'
   ].sum()

   return sales_previous_month

# Example of use
sales_table = pd.read_csv("sales_table.csv")

sales_previous_month = sales_previous_month(sales_table)

print(previous_month_sales)


#3 Calculate the Percentage Change:  Ex Measure in DAX

Percentage Change Month to Month =
     (
         [Current Sales] - [Previous Month Sales]
     ) / [Previous Month Sales] * 100



#3 Calculate the Percentage Change:  Ex Measure in PYTHON

def variation_percentual_month_by_month(current_sales, previous_month_sales):
   """
   Calculates the percentage change month to month.

   Arguments:
     current_sales: Total sales for the current month.
     sales_previous_month: Total sales for the previous month.

   Returns:
     The percentage change month to month.
   """

   if sales_previous_month == 0:
     return 0
   else:
     return ((current_sales - previous_month_sales) / previous_month_sales) * 100

# Example of use
current_sales = 1000
sales_previous_month = 800

percentage_variation = percentage_variation_month_by_month(current_sales, previous_month_sales)

print(f"Percentage variation month to month: {percentage_variation:.2f}%")








