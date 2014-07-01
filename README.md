# piston

A simple static site generator *(currently supporting Jinja2 templates)*

### Setup

Install [Jinja2](http://jinja.pocoo.org/)

I use pip: `pip intall jinja2`

More installation options are available in Jinja's docs.

### Usage

Build a site directory, and use Jinja2 HTML templates with the extension
`.jinja`.

Simply run the `piston.py` file inside the directory, and piston will create
a `build` directory, with your entire main directory copied, and `.jinja` files
built into `.html` files.

### Advanced

Files starting with `.` will be ignored by piston. This allows you to create
base templates that you can furthervextend, but not have show up with its own
`.html` file.

For example, I use `.base.jinja` and extend `index.jinja` from the base. Piston
will simply ignore this file and only generate `index.html` in `build`
directory.