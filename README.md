```
  __ _| |__   ___ _ __ _ __ __ _ _ __ | |_ ___ 
 / _` | '_ \ / _ \ '__| '__/ _` | '_ \| __/ _ \
| (_| | |_) |  __/ |  | | | (_| | | | | ||  __/
 \__,_|_.__/ \___|_|  |_|  \__,_|_| |_|\__\___|
```

# [aberrante.art](https://www.aberrante.art)

Minimal website inspired by net art experiments and durable, resilient web 1.0 implementations.

## Requirements
- Web site should display relevant information in a quick and expedient fashion.
- Web site should aid in the sales processes.
- It should be efficient in development time and resources.
- Ability to deal with information and raw data is of vital importance.
- Minimal weight and maximum simplicity.
- Information should be extremely clear.

## Design inspiration and research
Current js frameworks are slow to work on and slow to load, but html is quick and easy - we took a bit of a gamble with this minimal theme, but the basic usability really emphasizes usability. I think this approach is reminischent of brutalist architecture. Function over form.

- https://whydontyoulove.me/
- https://sive.rs
- http://textfiles.com
- https://motherfuckingwebsite.com
- https://www.wikipedia.org
- https://www.craigslist.org

## Specs
- Django monolith with postgresql
- Minimal js use, pure js and perhaps jquery in the future.
- Use of Django Admin Panel for internal use.
- Ascii art instead of images for minimum bloat.
- Really big potential to grow - especially with email automation.

### About the author
This is me. You can read about me on my github profile or in [climb.mx](https://www.climb.mx/)
```
    . -.=: =# ::+%%%##:..    . ::                           :...=*+=*=..-.:     
       .+..%%%%#=:.:::..  .    --                            :--:::::-#.: =.  : 
 ::%%%%%%%+=-:..:.. . .        ==                            -+:::: ::=::.::    
%@%.##*.%%  ...                :+ ..-  : :--             ::. -+ ..   .--:.--    
*:      #%- .-.                 -+++.*+ .:-++=    :-..       :+...... .+..-*:   
   .     %+. - :.              **********+  +:.:              =*-:=--=-*#:-#-   
      .  %+.   :       -      *******++******#===             =+-:.. . .=:-*=:  
.:       %%  . -           --.###****+=-=+*****#+             -......  :-=-*+:  
=--:-=-::%@   :     .:-=-. ::-###***=-=--:.-=***+-             ..    .=++*-=+- :
..:-: ...-@--:--.:.::-:::   :####**==--:::..   ++             ::......:++*::#-..
=..:. :. .@*...=--:::....  :*++#**++=+=:.. :  . :.            *-......:=+=:.*=- 
:.-=.:.  %@* :.-.:--..... ::+++#*++==**==:...  +   ....:...   +::.....-==+-:*--:
- -:. :.::@@.:.::::         *++#++====+++::*#-:...            . .....---+=+#*+--
:: :.::::.@@           -     ***++=---=++.:-:-          :=-. -- :.....:::==###-=
=--       +%=         =:.-:.:#***+==--=++: .        ::.     -:  -.........:=#%=-
        #  %+        = :..:..****+===+##=:      .  .:.  :*:..::.:.....:. .-***#-
        #: %=       . -::.+*#****+=++++== :   **+ .:::=:::::...:--:... ....:==*=
        #. %=    =::-:-=#***+*****+++++-... :.......:=:::..=................-==#
     @#.# =@@..:.::.**@@%#===++++**+==:. ==*: ........-:::.......:..........-*++
    +*+.+++=**:*-.%%#%%%%%%@=++==++#+==:#*-*#%:+.-.....:.:....:.:==: . ......+=-
  . .==.=: %%%+=@%@%%%%%%%%%%%+++=-:.=.=%+#-#=*#** .:=:....:::::::-:::. ......:-
@@@@###%*%%%#:@@@%%%%%#%%%%%%%%%@#%#*-:#+%*=**%##@+*-..:::::=::--:::.  -::.....:
@@@@#####%%##%@@@%%%%###%##%%%%%%@#**==*-###.*%##%%%=:# .:::=*++=---:. -*-+...:.
@@##@####%%##@%%%%%#%%%*#%#-###+*+-*=+-#+#%**##+#%%%*=+#*+ #***++===-==**--... .
-*#+-*+###%+@@%%%@%%%##%-.%#:*###**:++-##*%##:%*@@%%%##*#%#@  ****   ...::--....
***#=#+ ..=%@@%@%%%@@#+-%-#%%:*###+==++##+###*%%@@@%%####+:::*****  =    ..:....
---------#-:@@@%@%%%%@@%=#=%@%:=#+#***-#%+#%#%-#@@@@#    :+:.+++=-.       .:...:
=====*==*%--@@@@%%%%%@@@@+*%%@#=***#++*##**%%#+#@@@@#*=..=-=---=-==       .:....
%#==-----*+-@@@%@%##@@@@%#-%%%@#:-==++*%##%%%%#%@%%#--    -------==       .-+-..
%===%#=-+-:-@@@@@%%%%@@@@@##@%%%*.=**=#%%##%%@%#@%%------ --------=        .-...
+==------#%-%@@@@@%%%%%@@@@=#@%%%#=--+#%%*#%@@@%@%#:.:.- : -------=        .-:..
==--%%#=:..    @@@%%%%%%@@@%#@@@%%*=*+%#%%%%@@@%%%#*:::=:*.   ----==       .:-..
```

# Nerdy stuff

Local environment runs in vagrant. Execution as follows, once you install vagrant, vmware etc.

```vagrant up```

```vagrant ssh```

```python3 manage.py runserver [::]:8000```

```python3 manage.py makemigrations```
```python3 manage.py migrate```

### Deep-ploy

There is a script to aid with migrations on deploy.

```bash ./bin/deploy_migrate.sh ```
