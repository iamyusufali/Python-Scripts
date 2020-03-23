# Importing glob and RegEx
import glob as FileManager
import re


# Prompt for Directory name and location
Directory = input("Enter directory name: ")
Location = input("Enter directory location: ")


# Patterns and Replacements
pattern = [
  r'([\w]+)(\(([\w, \w]+)?\){)',
  r'([\w]+)( \(([\w, \w]+)?\){)',
  r'([\w]+)(\(([\w, \w]+)?\) {)',
  r'({)([\w:"\', ]+)(})',
  r'(\w)(:)([\'"])',
  r'([\w"\']+)(,)([\'"\w]+)',
  r'(={)',
  r'(=\[)'
]

replacement = [
  r'\1 (\3) {',
  r'\1 (\3) {',
  r'\1 (\3) {',
  r'{ \2 }',
  r'\1: \3',
  r'\1, \3',
  r'= {',
  r'= ['
]


# Open file and replace each matching pattern with the replacement 
def addCorrectIndents(file):
  num = 0
  while num < len(pattern):
    # Reads the file and replaces the matching pattern 
    with open(file, 'r') as rf:
      content = rf.read()
      RegEx = re.compile(pattern[num])
      data = RegEx.sub(replacement[num], content)
      # Writes the new data to the file
      with open(file, 'w') as wf:
        wf.write(data)
      num += 1
      

# Recursively find every JS file and store it
Files = FileManager.glob(Location + Directory + '/**/*.js', recursive = True)


# Add indents to every file
for file in Files:
  addCorrectIndents(file)