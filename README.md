# Welcome to Hlover HTML development tool
Hlover offers a simpler and easy syntax for HTML development. Instead of the complex design HTML has, Hlover provides a cleaner and efficient HTML code. 
## How to use
To use Hlover tool, you have to create your .hl file first. Then you have to download the 'hlover.py' file into your computer to translate .hl files into .html files. To translate your. hl files run the following command in your command line:

    python hlover.py yourfile.hl
Currently, your HTML code will be printed to stdout, but in future versions your code will be written in a new file.

## Syntax
Hlover syntax is simple. All HTML tags are preserved so it is much easier for HTML developers to use. There are two elements levels. 
1. HTML level.
2. Element level.
All HTML level elements are written like this

    tag_name[attributes]{body} 

and all element level elements must have '!' before the tag_name

    !tag_name[attributes]{body}
> Note: element level tags are elements inside an element.

Some tags don't need a body part, such as `meta` and `img`

    meta[...]
    !img[...]
  ### Attributes
  Attributes are the same as HTML, they are just inside '[]'. You can leave it empty, or don't put it at all.
  

    p{...}
## Not working yet
* Currently, Hlover is still in its alpha phase and some HTML tags don't work properly such as `script` body. However, I will be working on imporiving Hlover to be the perfect HTML tool.
* some characters like !, {, }, [, ], need to be escaped.
