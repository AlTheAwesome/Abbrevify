# Abbrevify ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg?color=Green&label=Python&style=popout)
**Cryptography Project based on IT Abbreviations**
<br>
<br>

## B..B..But what does it do?
**This basically _Encrypts_ and _Decrypts_ text messages into a code that nobody can understand unless they possess this _Encryptor_ / _Decryptor_**
<br>
<br>


## Dependencies
**For the time being all the required dependencies are in the **python 3** standard library.**
**(_Future updates will require kivy_)**
<br>
<br>


## H..H..How do I use it Tho?
to _Encrypt_ a message simply Open **Encode.py** and type in your message that you want **Encrypted**


```
what do you want to encoded?  
peanut butter and jelly sandwiches!
03I39XX022H211J623B711W313B511O543E001J001D022H002R002N212H33XX221O001D811D102S321C321J213O51XX722N13XX202H611W13XX213I121O333O151C002S002S8
```
<br>
<br>

Simply copy the message and send it to your buddy who will then  use the _decryptor_ which he'll paste the code into like so:

<br>
<br>

```
what do you want to decode?
03I39XX022H211J623B711W313B511O543E001J001D022H002R002N212H33XX221O001D811D102S321C321J213O51XX722N13XX202H611W13XX213I121O333O151C002S002S8
peanut butter and jelly sandwiches!
```

<p align="center">
  <img src="voila.png">
</p>

<br>

## C..C..Careful Now..!
There are some characters (", ^,) that you have to surround in double quotes if you want them to make it through the encryption process
ie:

```
what do you want to encoded?  
peanut butter and jelly sandwiches!^

```
Will Encrypt the message : _peanut butter and jelly sandwiches!_
**Whereas**:
```

what do you want to encoded?  
peanut butter and jelly sandwiches!"^"
```
Will Encrypt the message:_peanut butter and jelly sandwiches!^_


## Anything else?
The encryption has nothing to do with Unicode so **English** is currently(_and probably forever_) the only supported language
<br>
<br>


 ## A special thanks!
 **To myself**! for making this spaghetti code possible
