# Importing glob module
import glob


# Prompt for directory name and location
Directory = input("Enter directory name: ")
Location = input("Enter directory location: ")


# Correct indentations
indents = (
    ('(', ' ('),
    ('  (', ' ('),
    (')', ') '),
    (')  ', ') '),
    ('{',' {'),
    ('  {',' {'),
    ('}', '} '),
    ('}  ', '} '),
    ('}', ' }'),
    ('  }', ' }'),
    ('{', '{ '),
    ('{  ', '{ '),
    ('} ) ', '})'),
    ('( {', '({'),
    ('() .', '().'),
    (',', ', '),
    (',  ', ', '),
    (') ;', ');'),
    ('} ;', '};')
)


# Add proper indentation to each line of file
def replaceData(old, new):
    # Read text in file and replace old with new
    currentFile = open(file, "rt")
    fileData = currentFile.read()
    newData = fileData.replace(old, new)
    currentFile.close()

    # Write replaced data to the file
    currentFile = open(file, 'wt')
    currentFile.write(newData)
    currentFile.close()


# Recursively find every JS files and store them
Files = glob.glob(Location + Directory +'/**/*.js', recursive = True) 

for file in Files: 
    num = 0
    while num < len(indents):
        replaceData(indents[num][0], indents[num][1])
        num += 1
    
