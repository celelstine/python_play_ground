# python_play_ground
learn, practice and try out concepts and solutions with python. This codebase would be organized into packages and modules. Related concepts or soultions would be grouped into a package while orphan solutions would be store in the root directory.


## Extras
- ### Make python script globally executable (`case study: mac os`)
    - make the script executable `chmod +x <script>.py`
    - create a bin directory in your User directory (preferrably current loggin user) `mkdir ~/bin`
    - copy the script into the bin directory `cp <script>.py ~/bin`
    - update the $PATh in your bash:
        - open `~/.bash_profile` in any editor
        - add this line `export PATH=$PATH":$HOME/bin"`
        - save the changes
        - source the bash_profile file `source ~/.bash_profile` (this would make the update immediately active)
    - access your script from anywhere `<script>.py`
    - you can create an alias if you want to access the script by a simple name
        - open `~/.bash_profile` in any editor
        - add this line `alias <simple name> ="<script>.py"`
        - save the changes
        - source the bash_profile file `source ~/.bash_profile` (this would make the update immediately active)

