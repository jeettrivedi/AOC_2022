def pretty_print_header(day_no: int):
    """Prints out a pretty header of the form
    ******************************
              Day {day_no}
    ******************************
    """
    print('*'*30)
    print(' ' * 12 + 'Day ' + (str(day_no) if day_no >
          9 else f'0{day_no}'))
    print('*'*30)
