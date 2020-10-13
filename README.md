# ranDum

ranDum is a simple python based cli keyfile(s) generator that uses crypographically secure number generation to make bruteforcing a keyfile extremely tedious (in formatting) and time consuming (in length and randomness). rD allows you to create potentially hundreds or thousands of text files containing thousands of lines of any length of secure numbers.

## why use ranDum
The issue with the *random* python library is that its easily mimicked with statistical property analysis

Similar PRNG's such as the marsenne twister have a tendency to be deterministic, meaning if you set them to the same state, they will always create identical results. This is extremely dangerous for crypographically secure applications since an attacker with the ability to determine your initial state is capable of generating random numbers with the same "seed".

## features

  - uses pythons *secrets* library module to quickly generate cryptographically secure psuedorandom hex numbers
  - suitable for generating passwords, auth tokens, and just random numbers
  - many options allow for complex, difficult to replicate formatting and number options
  - completely offline design makes it impossible to be intercepted by web-based man-in-the-middle-attacks
  - robust, cross-platform design has been tested on *Unix* based systems like *macOS* and *Kali Linux* as well as *Windows*

## uses
- secure tokens
- account authentification
- passwords
- bulk secure password lists for initial/permanent user account passwords
## options
#### file settings
How many files would you like to generate?
>The value here with correspond to the amount of .txt files created.
#### text settings

How many lines of numbers would you like to generate per txt file?
>This value will determine how many lines of secure numbers to generate (starting from 0)

How many bytes should each line contain (1 byte = 2 digits)
>This will determine (in bytes) how long each string of secure numbers should be
#### Verbose and Log settings
Show file creation status and log? y/n
>Select y or n to view or omit the [Log | Generate] Generating random file name + (title) + .txt message

Show text-in-file creation status and log? y/n
>Select y or n to view or omit the [Log | Write] Generating line (line) in file (file)

