import csv
import statistics

PyBankpath = r"C:\Users\chard\Desktop\UCDSAC201902DATA4\03-Python\Homework\Instruction\PyBank\Resources\budget_data.csv"

with open(PyBankpath, newline='') as PybankCSV:
    Pybank = csv.reader(PybankCSV, delimiter = ",")
    PyBheader = next(Pybank, None)
    months=[]
    profit = []
    change = []
    for row in Pybank:
        months.append(row[0])
        profit.append(int(row[1]))                 
    for i in range(1,len(profit)):
        change.append(int(profit[i]-profit[i-1]))
        
avgchange = statistics.mean(change)
    
      
print(f'Total Months: {len(months)}')
print(f'Total: ${sum(profit)}')
print(f'Average Change: ${avgchange}')
print(f'Greatest increase in profits: {months[change.index(max(change))+1]} ${max(change)}')
print(f'Greatest decrease in profits: {months[change.index(min(change))+1]} ${min(change)}')
