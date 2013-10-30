def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_bar():
    print '+ - - - -',

def print_post():
    print '|        ',

def print_bars():
    do_twice(print_bar)
    print '+'

def print_posts():
    do_twice(print_post)
    print '|'

def print_row():
    print_bars()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_bars()

print_grid()
