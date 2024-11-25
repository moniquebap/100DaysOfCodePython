# Project 01: Band Name Generator

logo = '''

_                     _ 
| |                   | |
| |__   __ _ _ __   __| |
| '_ \ / _` | '_ \ / _` |
| |_) | (_| | | | | (_| |
|_.__/ \__,_|_| |_|\__,_|
                                ,---.      .--.
                               (  .  )    (  . )
                                `/--___  __`--`.
                            ,. _'| |___||___| _|`.
                           (-./_,|-,,'     `.' |\ `
                          __`-`-'|//     `:. \,|'
          --     -   --- |\    | |||       ` | |
             --          | \  _|_|\\         / |
      -            _     \  \  ,-'-.`._____,',-'-.
   ______________      `[]\ .\____________________
  |`.____________`.     || \`| .::'        ._
  | |_''_o_o__o =.|     ||  \|_________________
  | | ,--.   ,--. :   _ ||
  | |( () ) ( () )|:  \`::')   ---        __
  `.|_`-_'___`-_'_|`. / :: \\
  -           _  -  : \___:/    _   -    -
                    `--..___)
'''

print(logo)
# 1. Create a greeting for your program.
print("Welcome to the Band Name Generator!")
# 2. Ask the user for the city that they grew up in.
city = input("What's the name of the city you grew up in? \n")
# 3. Ask the user for the name of a pet.
pet = input("What's the name of your pet? \n")
# 4. Combine the name of their city and pet and show them their band name.
print("Your Band Name is: " + city + " " + pet + "!")