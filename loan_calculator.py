import argparse
import math

error_allert = 'Incorrect parameters'
allelrt = False

def diff_payment(principal, periods, interest):


    i = interest / (12 * 100)
    overpayment = 0 - principal

    for m in range(1,periods+1):

       month = (principal/periods) + i * (principal-(principal * (m - 1)/periods))
       month = math.ceil(month)
       print('Month {}: payment is {}'.format(m, month))
       overpayment += month

    print('Overpayment = {}'.format(math.ceil(overpayment)))


def principal_calc(periods, interest, payment):
    i = interest / (12 * 100)

    principal = payment / (i * ((1 + i) ** periods) / (((1 + i) ** periods) - 1))
    principal = round(principal)
    return principal

def periods_calc(principal, interest, payment):
    i = interest / (12 * 100)

    periods = math.log((payment / (payment - i * principal)), 1 + i)
    periods = math.ceil(periods)
    overpayment = (payment * periods) - principal
    return [periods, overpayment]

def payment_calc(principal, interest, periods):
    i = interest / (12 * 100)

    payment = principal * (i * ((1 + i) ** periods) / (((1 + i) ** periods) - 1))
    payment = math.ceil(payment)
    return payment


parser = argparse.ArgumentParser(description='This is a loan calculator')

parser.add_argument('-t', '--type', choices=['annuity', 'diff'],
                    help='indicates the type of payment: [annu]-annuity or [diff]-differentiated')

parser.add_argument('-p', '--principal', type=float,
                    help='Enter the loan principal')
parser.add_argument('-m', '--periods', type=int,
                    help='Enter the number of periods')
parser.add_argument('-i', '--interest', type=float,
                    help='Enter the loan interest in percentage')
parser.add_argument('-pay', '--payment', type=float,
                    help='Enter the loan monthly payment')


args = parser.parse_args()

try:
    if args.type == 'annuity':
        if args.principal == None:

            loan_principal = principal_calc(args.periods, args.interest, args.payment)
            print('Your loan principal = {}!'.format(loan_principal))
            print('overpayment:{}'.format(args.payment * args.periods - loan_principal))

        if args.periods == None:

            months_over = periods_calc(args.principal, args.interest, args.payment)
            months = months_over[0]
            overpayment = months_over[1]

            years = months // 12
            months_year = months % 12

            if years == 1:
                year_str = '{} year'.format(years)
            else:
                year_str = '{} years'.format(years)

            if months_year == 1:
                months_str = 'and {} month'.format(months_year)
            elif months_year == 0:
                months_str = ''
            else:
                months_str = 'and {} months'.format(months_year)

            print('It will take {} {} to repay this loan!'.format(year_str, months_str))
            print('Overpayment = {}'.format(overpayment))

        if args.payment == None:


            annu_payment = payment_calc(args.principal, args.interest, args.periods)
            print('''Your annuity payment = {}
Overpayment = {}'''.format(annu_payment, (annu_payment * args.periods) - args.principal ))


    elif args.type == 'diff':
        diff_payment(args.principal, args.periods, args.interest)

except:
    allelrt = True

if allelrt:
    print(error_allert)
