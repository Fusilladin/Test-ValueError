### ValueError handling

# try(go thru)/except(catch error)/else-break ValueError
# CATCHING AN ERROR

while True:
    try:
        num_1 = (str(input("Pick a number.  ")))
        num_str = num_1.split(" ")[0]
        num_2 = int(float(num_str))
    except ValueError:
        print("\nERROR; please type a number!")
        continue
    else:
        break

############################
# while/if not/name./isupper(is upper, many others)
# EXAMPLE ALLCAPS SPECIFIC

# while True:
#     name = input('Please provide me your name in all caps:  ')
#     if not name.isupper():
#         print('ERROR; name is not in ALL CAPS.')
#     else:
#         break

############################
# while/if/not in/selection./lower (many others)
# EXAMPLE SELECTION MUST IN THIS LIST []

# while True:
#     selection = input('select from A to E:  ')
#     if selection.lower() not in ['a', 'b', 'c', 'd', 'e']:
#         print('Invalid Option')
#         continue
#     else:
#         print('This is valid')
#         break
