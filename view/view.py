import output.output as view
import output.colours as colours
from typing import Type
from typing import List

def print_banner(text="", font='slant', colour=colours.colour_white):
    view.print_banner(text, font, colour)


def print_text(text_object: List[Type[view.Text]], indent=0, quote="", num_columns=5, column_spacing=30):
    view.print_text(text_object, indentation=indent, prefix_quote=quote, num_columns=num_columns, column_spacing=column_spacing)

print_banner("Open-Source Intelligence Tool", colour=colours.colour_blue)

print_text([view.Text(colour=colours.colour_blue, text="THIs is some sample text "),
            view.Text(colour=colours.colour_blue, text="THIs is some sample text "),
            view.Text(colour=colours.colour_blue, text="THIs is some sample text "),
            view.Text(colour=colours.colour_blue, text="THIs is some sample text "),
            view.Text(colour=colours.colour_blue, text="THIs is some sample text "),
            view.Text(colour=colours.colour_blue, text="THIs is some sample text "),
            view.Text(colour=colours.colour_blue, text="THIs is some sample text "),
            view.Text(colour=colours.colour_blue, text="THIs is some sample text "),
            view.Text(colour=colours.colour_blue, text="THIs is some sample text "),
           view.Text(colour=colours.colour_blue, text="THIs is some sample text ")], 0, ">")


#print_text(indent=4, quote="", num_columns=2, column_spacing=20, colour=colours.colour_blue, text="THIs is some sample text")

# cli.py
from pprint import pprint

from PyInquirer import style_from_dict, Token, prompt, Separator

from examples import custom_style_2


#https://opensource.com/article/17/5/4-practical-python-libraries
#https://click.palletsprojects.com/en/7.x/utils/

import click
#message = click.edit()

from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import Completer, Completion
import click
from fuzzyfinder import fuzzyfinder

SQLKeywords = ['select', 'from', 'insert', 'update', 'delete', 'drop']

#suggestions = fuzzyfinder('abc', ['abcd', 'defabca', 'aagbec', 'xyz', 'qux'])
#print(list(suggestions))
class SQLCompleter(Completer):
    def get_completions(self, document, complete_event):
        word_before_cursor = document.get_word_before_cursor(WORD=True)
        matches = fuzzyfinder(word_before_cursor, SQLKeywords)
        print(matches)
        for m in matches:
            yield Completion(m, start_position=-len(word_before_cursor))

while 1:
    user_input = prompt(u'SQL>',
                        history=FileHistory('history.txt'),
                        auto_suggest=AutoSuggestFromHistory(),
                        completer=SQLCompleter(),
                        )
    click.echo_via_pager(user_input)


'''
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import WordCompleter
import click

SQLCompleter = WordCompleter(['select', 'from', 'insert', 'update', 'delete', 'drop'],
                             ignore_case=True)


user_input = prompt(u'SQL>',
                    history=FileHistory('history.txt'),
                    auto_suggest=AutoSuggestFromHistory(),
                    completer=SQLCompleter,
                    )
click.echo_via_pager(user_input)

click.echo('Continue? [yn] ', nl=False)
c = click.getchar()
click.echo()
if c == 'y':
    click.echo('We will go on')
elif c == 'n':
    click.echo('Abort!')
else:
    click.echo('Invalid input :(')
'''
#click.clear()
#print(message)
'''VERY GOOD RAW CHOICES
from examples import custom_style_2

from PyInquirer import style_from_dict, Token, prompt, print_json, Separator
questions = [
    {
        'type': 'rawlist',
        'name': 'theme',
        'message': 'What do you want to do?',
        'choices': [
            'Order a pizza',
            'Make a reservation',
            Separator(),
            'Ask opening hours',
            'Talk to the receptionist'
        ]
    },
    {
        'type': 'rawlist',
        'name': 'size',
        'message': 'What size do you need',
        'choices': ['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
        'filter': lambda val: val.lower()
    }
]

answers = prompt(questions, style=custom_style_2)
print_json(answers)
'''
'''


def get_delivery_options(answers):
    options = ['bike', 'car', 'truck']
    if answers['size'] == 'jumbo':
        options.append('helicopter')
    return options


questions = [
{
        'type': 'expand',
        'name': 'toppings',
        'message': 'What about the toppings?',
        'choices': [
            {
                'key': 'p',
                'name': 'Pepperoni and cheese',
                'value': 'PepperoniCheese'
            },
            {
                'key': 'a',
                'name': 'All dressed',
                'value': 'alldressed'
            },
            {
                'key': 'w',
                'name': 'Hawaiian',
                'value': 'hawaiian'
            }
        ]
    },
    {
        'type': 'list',
        'name': 'theme',
        'message': '  Select a menu option?',
        'choices': [
            '  Check Moloch Health',
            {
                'name': 'Molch-Health',
                'disabled': '  Check the health all/specified molochs'
            },
            '  Moloch Queries/Hunting',
            {
                'name': 'moloch_queries',
                'disabled': '  Search multiple molochs by loading or inputting queries'
            },
            '  Open Source Intelligence Tool',
            {
                'name': 'osint',
                'disabled': '  Scan a collection of OSINT sources'
            },
        ]
    },
]

answers = prompt(questions, style=custom_style_2)
pprint(answers)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''


''' Interactive command line - PyLnquirer
https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df
'''

'''
import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from clint.textui import puts, colored, indent
from clint.textui import columns


col_spacing = 30
index_amount = 4
with indent(index_amount, quote=''):
    puts(columns([(colored.red('  Column 1')), col_spacing], [(colored.green('  Column Two')), col_spacing],
                 [(colored.magenta(' Column III')), col_spacing]))
    puts(columns(['  hi there my name is kenneth and this is a columns', col_spacing], ["  TE", col_spacing], ['  kenneths', col_spacing]))




a = 1
b = 2

list = []
list.append(a)
print(str(list[0]))

a = a + 1
list.append(a)
print(str(list[0]))
print(str(list[1]))

a = a + 1

dic = {}
for x in range(100):
    print(x)
'''

''' FILE CRUD
import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from clint import resources

resources.init('kennethreitz', 'clint')

lorem = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'


print('%s created.' % resources.user.path)

resources.user.write('lorem.txt', lorem)
print('lorem.txt created')

assert resources.user.read('lorem.txt') == lorem
print('lorem.txt has correct contents')

resources.user.delete('lorem.txt')
print('lorem.txt deleted')

assert resources.user.read('lorem.txt') == None
print('lorem.txt deletion confirmed')

from time import sleep
from clint.textui import progress
def create_progress_bar(label="", expected_size=0):
    return progress.Bar(label=label, expected_size=expected_size)

def show_progress(progress_bar=progress.Bar, label="", current_index=0):
    progress_bar.label = label
    progress_bar.show(current_index)

moloch = ["a1", "a2", "b2", "b3", "b4", "c1", "c2"]
prog_bar = create_progress_bar(label="", expected_size=7)
#print_text([view.Text(indentation=4, quote="~", colour=colours.colour_green, text="Scanning Molochs")])
for count, elem in enumerate(moloch):
    count = count + 1
    show_progress(prog_bar, "Scanning Moloch: "+elem, count)
    sleep(0.5)
'''


''' TEXT COLOUR EXAMPLES
import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from clint.textui import colored

text = 'THIS TEXT IS COLORED %s!'

if __name__ == '__main__':

	for color in colored.COLORS:
		print(getattr(colored, color)(text % color.upper()))
'''


''' INDNTING MULTI LINES
lorem = \'''
Lorem ipsum dolor sit amet, consectetur adipisicing elit
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
culpa qui officia deserunt mollit anim id est laborum.
    \'''

with indent(4):
    puts(lorem)

'''