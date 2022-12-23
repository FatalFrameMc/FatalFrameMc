# Micheal Cudd
# Module 04 Programming Assignment
# Part B

# Cara's Cool Coffee pays employees differently depending on their job title and experience. ' \
# 'In a program called payroll.py, use separate prompts to collect the following input:
# Job title ("B" for barista, "M" for maintenance, "G" for general staff)
# Number of hours worked
# Number of years employed at the restaurant

# Then, output their gross pay amount (i.e., the amount they earn before taxes and other deductions)
# for one week based on the following:
# Baristas earn $5/hour until they've worked 1 year, then earn $6/hour
# maintenance workers earn $12/hour for the first 2 years, then go up to $13.50/hour
# General staff make $15/hour for the first year, then go to $18/hour

# job title
job_title = input("what is your job title; barista, maintenance, general? ")
if job_title == "barista":
    job_title = 'B'
if job_title == "maintenance":
    job_title = 'M'
if job_title == "general":
    job_title = 'G'

# hours
hours = int(input("How many hours have you worked this week? "))

# years employed
years = int(input('How many years? '))

# pay
b_pay1 = 5
b_pay2 = 6
m_pay1 = 12
m_pay2 = 13.50
g_pay1 = 15
g_pay2 = 18

# barista pay options
if job_title == 'B' and years <= 1:
    rate = b_pay1
if job_title == 'B' and years > 1:
    rate = b_pay2

# maintenance pay option
if job_title == 'M' and years <= 2:
    rate = m_pay1
if job_title == 'M' and years > 2:
    rate = m_pay2

# general staff pay option
if job_title == 'G' and years <= 1:
    rate = g_pay1
if job_title == 'G' and years > 1:
    rate = g_pay2

# pay before taxes
pay = rate * hours
print(pay)
