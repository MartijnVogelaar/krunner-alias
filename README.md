# KRunnerAlias
KRunnerAlias allows you to use aliases defined in ~/.bashrc. Arguments can also be passed to the aliases.

# Examples

If the following alias is defined in ~/.bashrc :

`alias test_Alias=kate`

KRunnerAlias allows the following things to be entered in krunner

```
test_Alias 
```

Which obviously opens kate. Arguments can however also be passed to aliases which allows for the following: 

```
test_Alias ~/test.txt
```

Which effectively means that the following is executed: `kate ~/test.txt`.


# Defining aliases
Aliases have to be defined as they are supposed to be in a `.bashrc`-file. Aliases have the following formats:

```
alias ${name}=${command}
```

```
alias ${name}="${command}"
```

```
alias ${name}='${command}' 
```

Comments can be added after the command using `#`:
```
alias ${name}='${command}' #${comment}
```

# Limitations

Chaining aliases is not (yet) supported, if the following aliases are defined

`alias test_Alias='kate '`\
`alias file1="test.txt"`

Entering the following in krunner:
```
test_Alias file1
```

results in:

```
kate file1
```

and not in

```
kate test.txt
```
