# Solution
## Open the corrupted archive in a hex editor
sudo ghex corrupted_evidence.rar

## Change the first 3 bytes to restore the RAR magic bytes
Before (corrupted header):
```
52 00 52 11 1A 07 00
```
After (corrected header):
```
52 61 72 21 1A 07 00
```

## Extract the archive
```sh
unrar x recovered_archive.rar
```

## Search for the hidden flag inside the log file
```sh
strings evidence.log | grep "bbctf"
```

Output: System recovery initiated: bbctf{r3$T0r!nG_trUt#}
Flag: 
``` 
bbctf{r3$T0r!nG_trUt#}
```
