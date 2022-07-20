
ordinal_number_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth', 'thirteenth']
tab_date = []
tab_time = []

#function to read the date and time
def read_input():
  print('Please enter a date:')
  tab_date.append(input())
  print('Please enter the time:')
  tab_time.append(input())

#function to print the dates and times
def print_output(i,time_numbers):
  if(i<time_numbers-1):
    print('The '+ ordinal_number_list[i] + ' date has been reached! (' + tab_date[i]+' - ' + tab_time[i] + ')')
  else: 
    print('The '+ ordinal_number_list[i] + ' date was reached! (' + tab_date[i]+' - ' + tab_time[i] + ')')

#main function of the program
def main():
  print('How much data do you want to enter?')
  time_numbers = int(input())
  i = 0
  while (i<time_numbers):
    read_input()
    i=i+1

  print('Thank you very much. I will notify them!')

  i=0
  while (i<time_numbers):
    print_output(i,time_numbers)
    i=i+1

main()