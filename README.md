# pyss

easily compile sass

I would recommend making an alias and adding it to your `.bashrc`
```sh
alias pyss='python3 /home/jlieberg/Documents/pyss/pyss.py'
```

### Dependencies

```sh
pip3 install libsass
```

Commands:
* `pyss <source file> [target file] [output style]` - compile scss file into css
* `pyss <source folder> [target folder] [output style]` - compile scss file into css

Examples:

I included a few example scss files to test the script on. You can run them with the following:

```sh
pyss in
pyss in out
pyss in out expanded
pyss in.scss
pyss in.scss out
pyss in.scss out expanded
```
