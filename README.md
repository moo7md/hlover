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

    tag_name[attributes]{!tag_name[attributes]{body}}
> Note: element level tags are elements inside an element.

Some tags don't need a body part, such as `meta` and `img`

    meta[...]
    img[...]
  ### Attributes
  Attributes are the same as HTML, they are just inside '[]'. You can leave it empty, or don't put it at all.
  

    p{...}
or
    
    p[]{...}
both are the same.
### !Doctype
Hlover makes declaring doctypes much easier. If you want to add a doctype, just choose one of the following and put it at the top:

* `html5` for `<!DOCTYPE html>`
* `html4s` for `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">`
* `html4t` for `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">`
* `html4f` for `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" "http://www.w3.org/TR/html4/frameset.dtd">`
* `xhtml1s` for `<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" '
                       '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">`
* `xhtml1t` for `<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" '
                       '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> `
* `xhtml1f` for `<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN" '
                       '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd">`
* `xhtml1.1` for `<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"`
## Not working yet
* ~~Currently, Hlover is still in its alpha phase and some HTML tags don't work properly such as `script` body. However, I will be working on imporiving Hlover to be the perfect HTML tool.~~ FIXED
* ~~some characters like !, {, }, [, ], need to be escaped.~~ FIXED
