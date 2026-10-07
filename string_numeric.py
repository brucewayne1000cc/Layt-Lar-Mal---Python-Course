
first = 'Eric'

last = 'Berg'

name = f"{first} {last}"

print('Pure name:', name) # pure name

lowercase = name.lower() # change to lowercase

print('Lowercase:', lowercase)

uppercase = lowercase.upper() # change to uppercase

print('Uppercase:', uppercase)

titlecase = uppercase.title() # change to title case

print('Title Case:', titlecase)

greeting = 'Hello, '

prefix = 'Dr. '

message = greeting + prefix + name + ', how was your holiday?' # this is call string concatenating

print(message)

quote = 'Albert Einstein once said, "A person who never made a mistake never tried anything new."'

print(quote)

addition = 4 + 4

print('Addition: 4 + 4 =', addition)

subtraction = 12 - 4

print('Subtraction: 12 - 4 =', subtraction)

multiplication = 2 * 2 * 2

print('Multiplication: 2 x 2 x 2 =', multiplication)

division = 16 / 2

print('Division: 16 / 2 =', int(division)) # remove decimal

fav = '10,000'

lyric = f"Hello, everyone this is my favorite song:\n \tI'd spend {fav} hours and {fav} more. Oh, if that's what it takes to learn that sweet heart of yours"

print(lyric)