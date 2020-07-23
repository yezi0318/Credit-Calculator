import math
import sys


def get_i(annual_interest):
    return (annual_interest / 100) / (12 * 1)


def get_num_months():
    credit_principal = sys.argv[2]
    monthly_pay = sys.argv[3]
    credit_interest = sys.argv[4]
    # print("we currently have these three:")
    # print("the principal is: " + credit_principal.split("=")[1])
    # print("the monthly payment is: " + monthly_pay.split("=")[1])
    # print("the credit interest in percent is: " + credit_interest.split("=")[1])
    # print("We want to calculate periods of months...")
    credit_principal = float(credit_principal.split("=")[1])
    monthly_pay = float(monthly_pay.split("=")[1])
    credit_interest = float(credit_interest.split("=")[1])

    i_nominal_interest = get_i(credit_interest)

    print(i_nominal_interest)
    n_periods = math.log(monthly_pay / (monthly_pay - i_nominal_interest * credit_principal), 1 + i_nominal_interest)
    print(n_periods)
    if n_periods % 2 != 0:
        n_periods = int(n_periods + 1)
    print(n_periods)

    year = int(n_periods / 12)
    month = int(n_periods % 12)
    over_pay = monthly_pay * n_periods - credit_principal

    print("You need " + str(year) + " years and " + str(month) + " months to repay this credit!")
    print("Overpayment = " + str(int(over_pay)))


#################################################################

def get_annuity_payment():
    credit_principal = sys.argv[2]
    count_periods = sys.argv[3]
    credit_interest = sys.argv[4]

    # print("we currently have these three:")
    # # print("the principal is: " + credit_principal.split("=")[1])
    # print("the num periods is: " + count_periods.split("=")[1])
    # print("the credit interest in percent is: " + credit_interest.split("=")[1])
    # print("We want to calculate monthly annuity payment...")

    credit_principal = float(credit_principal.split("=")[1])
    count_periods = float(count_periods.split("=")[1])
    credit_interest = float(credit_interest.split("=")[1])

    i_nominal_interest = get_i(credit_interest)
    n_periods = count_periods
    annuity_pay = credit_principal * ((i_nominal_interest * math.pow((1 + i_nominal_interest), n_periods)) / (
            math.pow((1 + i_nominal_interest), n_periods) - 1))
    if annuity_pay % 1 != 0:
        annuity_pay = int(annuity_pay) + 1
        # print(annuity_pay)
    print("Your annuity payment = " + str(annuity_pay) + "!")
    over_pay = annuity_pay * count_periods - credit_principal
    print("Overpayment = " + str(int(over_pay)))


#################################################################

def get_credit_principal():
    monthly_pay = sys.argv[2]
    count_periods = sys.argv[3]
    credit_interest = sys.argv[4]

    # print("we currently have these three:")
    # print("the monthly payment is: " + monthly_pay.split("=")[1])
    # print("the num periods is: " + count_periods.split("=")[1])
    # print("the credit interest in percent is: " + credit_interest.split("=")[1])
    # print("We want to calculate principal...")

    monthly_pay = float(monthly_pay.split("=")[1])
    count_periods = float(count_periods.split("=")[1])
    credit_interest = float(credit_interest.split("=")[1])

    i_nominal_interest = get_i(credit_interest)
    credit_principal = monthly_pay / ((i_nominal_interest * math.pow((1 + i_nominal_interest), count_periods)) / (
            math.pow((1 + i_nominal_interest), count_periods) - 1))
    if credit_principal % 1 != 0:
        credit_principal = int(credit_principal) + 1

    over_pay = monthly_pay * count_periods - credit_principal

    print("Your credit principal = " + str(credit_principal) + "!")
    print("")
    print("Overpayment = " + str(int(over_pay)))


#################################################################
def get_differentiated_pay():
    principal = sys.argv[2]
    count_periods = sys.argv[3]
    credit_interest = sys.argv[4]

    principal = float(principal.split("=")[1])
    count_periods = float(count_periods.split("=")[1])
    credit_interest = float(credit_interest.split("=")[1])

    i_nominal_interest = get_i(credit_interest)

    payment_sum = 0
    for m in range(1, int(count_periods) + 1):

        diff_pay = principal / count_periods + i_nominal_interest * (
                    principal - (principal * (int(m) - 1) / count_periods))
        if diff_pay % 1 != 0:
            diff_pay = int(diff_pay) + 1
        payment_sum += diff_pay

        print("Month " + str(m) + ": paid out " + str(int(diff_pay)))
    over_pay = payment_sum - principal
    print("")
    print("Overpayment = " + str(int(over_pay)))


#################################################################
# Program starts here!
#################################################################

# num of parameters less than 4
if len(sys.argv) <= 4:
    print("Incorrect parameters.")
    sys.exit()

# combination types errors
for arg in sys.argv:
    if arg.startswith('--type='):
        t = arg.split('=')[1]
        if t != 'diff' and t != 'annuity':
            print("Incorrect parameters.")
            sys.exit()

# negative parameters errors
for arg in sys.argv:
    if arg.startswith('--principal='):
        r = arg.split('=')[1]
        if int(r) < 0:
            print("Incorrect parameters.")
            sys.exit()

for arg in sys.argv:
    if arg.startswith('--payment='):
        r = arg.split('=')[1]
        if int(r) < 0:
            print("Incorrect parameters.")
            sys.exit()

for arg in sys.argv:
    if arg.startswith('--payment='):
        r = arg.split('=')[1]
        if int(r) < 0:
            print("Incorrect parameters.")
            sys.exit()

# get differentiated payment, if don't execute this diff, go to num of parameters less than 4
for word in sys.argv:
    if word.startswith('--type=diff'):
        get_differentiated_pay()
        sys.exit()



# use T/F to check which parameter(input) that user gave or not
has_payment = False
has_principal = False
has_periods = False
has_interest = True

# calculate for type = annuity with 3 functions
for arg in sys.argv:
    if arg.startswith('--payment='):
        has_payment = True
        break

for arg in sys.argv:
    if arg.startswith('--principal='):
        has_principal = True
        break

for arg in sys.argv:
    if arg.startswith('--periods='):
        has_periods = True
        break

if has_principal == False:
    get_credit_principal()
elif has_payment == False:
    get_annuity_payment()
else:
    get_num_months()

