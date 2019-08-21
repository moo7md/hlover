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
### Paragraph tag tips:
Since some special characters in Hlover has some functionality, users must escape them usnig '\\'. For example, if you want to write '!' in the body of the paragraph, the user have to include '\\' before '!' to escape it from its fictionality.
    
    p{Hello World\!}
> Note: failing to escape any special character may cause unwanted results
## Example
    html5
    html{
        !head{
            !meta[lang="en"]
            !title{Page title}
        }
        !body{
            !p{This is a paragraph element\!}
        }
    }
Output =>

    <!DOCTYPE html>
    <html>
        <head>
            <meta lang="en">
            <title>Page title</title>
        </head>
        <body>
            <p>This is a paragraph element!</p>
        </body>
    </html>
## Inheritance
One of the big problems most HTML developers face are writing the same attributes for almost every element in the page. Thus, I was motivated to solve this problem by including inheritance to Hlover. By simply adding inherited attributes to an element, all its children elements will inherit those attributes.
### Syntax
To add attributes to the inheritance part of an element, user simply put those attributes inside parentheses and place them right after the tag name. It can not be placed anywhere else. This is how it should look like:

    tag_name(inherited attributes){...}
In addition, sub-tags can override their parents' inherited attributes by placing those attributes inside brackets and placed right after the inherited attributes. This is how it should look like:

    tag_name(inherited attributes)[overrode attributes]{...}
### Example

    html5
    html{
        !body(style="font-family: monospace;" name="none" class="box")[id="main"]{
            !p(class="what" readonly="")[id="p1"]{TEST\!}
            !p[id="p2" style  = "font-family: Serif;"]{TEST\!}
            !p[id="p3" style="font-size: 50px;"]{TEST\! !em{STRONG}}
            !p(class="special")[id="p3" style="font-size: 50px;"]{TEST\! !em{STRONG}}
        }
    }
Output =>

    <!DOCTYPE html>
    <html >
        <body id="main" style="font-family: monospace;" name="none" class="box" >
            <p id="p1" class="what" readonly="" style="font-family: monospace;" name="none" >TEST!</p>
            <p id="p2" style="font-family: Serif;" name="none" class="box" >TEST!</p>
            <p id="p3" style="font-size: 50px;" name="none" class="box" >TEST! <em style="font-family: monospace;" name="none" class="box">STRONG</em></p>
            <p id="p3" style="font-size: 50px;" class="special" name="none" >TEST! <em class="special" style="font-family: monospace;" name="none" >STRONG</em></p>
        </body>
    </html>
    
> Note: boolean attributes must be assigned with a value. It can not be alone. It will be fixed in future versions.
> Also, I'm working on making sub-tags able to completely ignore their parents' inherited attributes and have their own attributes or none.
## Bugs
* ~~Currently, Hlover is still in its alpha phase and some HTML tags don't work properly such as `script` body. However, I will be working on imporiving Hlover to be the perfect HTML tool.~~ FIXED
* ~~some characters like !, {, }, [, ], need to be escaped.~~ FIXED
* ~~style element is not working yet.~~
* ~~comments are not working properly.~~
* Boolean attributes (with name only) not supported yet.
