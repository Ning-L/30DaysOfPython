# Day 21: 30 Days of python programming

# Exercises: Level 1

# 1. Python has the module called _statistics_ and we can use this module
#  to do all the statistical calculations. However, to learn how to make
#  function and reuse function let us try to develop a program,
#  which calculates the measure of central tendency of a sample
#  (mean, median, mode) and measure of variability (range, variance,
#  standard deviation). In addition to those measures,
#  find the min, max, count, percentile, and frequency distribution of
#  the sample. You can create a class called Statistics and create all
#  the functions that do statistical calculations as methods for the
#  Statistics class. Check the output below.

class Statistics():
    def __init__(self, lst):
        self.lst = lst

    def count(self):
        return len(self.lst)

    def sum(self):
        return sum(self.lst)

    def min(self):
        return min(self.lst)

    def max(self):
        return max(self.lst)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum()/self.count()

    def median(self):
        self.lst.sort()
        n = len(self.lst)
        if n % 2 == 0:
            med = (self.lst[int(n / 2 - 1)] + self.lst[int(n / 2)]) / 2
        else:
            med = self.lst[int((n - 1) / 2)]
        return med

    def mode(self):
        my_count = [
            {"mode": i, "count" : self.lst.count(i)}
            for i in set(self.lst)
        ]
        my_count_sorted = sorted(
            my_count, key = lambda x: x["count"], reverse = True)
        return my_count_sorted[0]

    from math import sqrt
    def std(self):
        return math.sqrt(self.var())
    
    def var(self):
        mean = sum(self.lst) / len(self.lst)
        diff_mean = []
        for i in self.lst:
            diff_mean.append((i - mean) ** 2)      # cumulate deviation from mean then sum in the next line
        variance = sum(diff_mean) / (len(self.lst) - 1)
        return variance
    
    def describe(self):
        print("Count:", self.count())
        print("Sum:", self.sum())
        print("Min:", self.min())
        print("Max:", self.max())
        print("Range:", self.range())
        print("Mean:", self.mean())
        print("Median:", self.median())
        print("Mode:", self.mode())
        print("Variance:", self.var())
        print("Standard Deviation:", self.std())
    

    
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(lst=ages)

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
# print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
## not sure what the last means

data.describe()

## you output should look like this
# print(data.describe())
# Count: 25
# Sum:  744
# Min:  24
# Max:  38
# Range:  14
# Mean:  30
# Median:  29
# Mode:  (26, 5)
# Variance:  17.5
# Standard Deviation:  4.2
# Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

# Exercises: Level 2

# 1. Create a class called PersonAccount. 
# It has firstname, lastname, incomes, expenses properties and
#  it has total_income, total_expense, account_info, add_income,
#  add_expense and account_balance methods. Incomes is a set of incomes
#  and its description. The same goes for expenses.

class PersonAccount():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = dict()
        self.expenses = dict()
    
    def add_income(self, description, amount):
        self.incomes[description] = amount

    def add_expense(self, description, amount):
        self.expenses[description] = amount

    def total_income(self):
        return sum(self.incomes.values())
    
    def total_expense(self):
        return sum(self.expenses.values())

    def account_balance(self):
        return self.total_income() - self.total_expense()
        
    def account_info(self):
        print(f"Account info for {self.firstname} {self.lastname}:")
        print(f"  Total income: {self.total_income()}")
        print(f"  Total expense: {self.total_expense()}")
        print(f"  Account balance: {self.account_balance()}")


person_account = PersonAccount("Abc", "Dupont")
person_account.add_income("job1", 1000)
person_account.incomes # {'job1': 1000}}
person_account.add_income("job2", 500)
person_account.incomes # {'job1': 1000, 'job2': 500}

person_account.add_expense("meal", 200)
person_account.expenses # {'meal': 200}
person_account.add_expense("transport", 100)
person_account.expenses # {'meal': 200, 'transport': 100}

person_account.total_income()
person_account.total_expense()
person_account.account_balance()
person_account.account_info()