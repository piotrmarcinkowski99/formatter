import argparse
from text_file_manager import TextFileManager

path = "text_files"
tab = 4
space = 1

TextFileManager.path = path
TextFileManager.tab = tab
TextFileManager.space = space

parser = argparse.ArgumentParser(description='The program which converts text indentation (space to tabs and reverse).')

helper_from = "select the type of character that will be converted"
helper_replace = "if there is a param, the script does not make a save copy"
helper_tab_chars = "optional param which determines the number of space which replace a single tab character"

parser.add_argument('--from', '-f', choices=['tabs', 'spaces'], help=helper_from, required=False, type=str)
parser.add_argument('--replace', '-r', help=helper_replace, required=False, action='store_true', default=False)
parser.add_argument('--tab-chars', '-t', help=helper_tab_chars, nargs='?', default=4, const=4, type=int)

args = parser.parse_args()

from_ = args.__dict__.get('from')
replace = args.__dict__.get('replace')
tab_chars = args.__dict__.get('tab_chars')

print(f"Params: --from {from_}, --replace {replace}, --tab-chars {tab_chars}")

text_file_editor = TextFileManager(from_, replace, tab_chars)
