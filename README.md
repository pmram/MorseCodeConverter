# MorseCodeConverter
## Get Morse Code
### Route
Use /convert/ route passing "text" parameter to return a string converted to Morse Code.

### Params
**text** - Pass a string to be converted (mandatory)

**separator** - Pass a string to separate the Morse Code characters (default = " ")

**error_char** - Pass an alternative string to replace characters that could not be converted. (default = "$")

### Results
```
{
  "result": {
    "morse": "__ ___ ._. ... .",
    "original": "morse"
  }
}
```
