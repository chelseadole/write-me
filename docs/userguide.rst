User Guide
***********

Description
==============

Generate a README, with the following sections:

- Project Overview (Description, Version, Highlight Features ^, Authors ^)
- Documentation ~ ^ 
- Getting Started (Prerequisites, Dependencies, Installation, Local Serving ^)
- Testing (Running Tests, Testing Modules)
- URLs (URL Modules)
- Modules ~
- Development Tools
- Contributions ~
- License
- Acknowledgements ^

    KEY:
        - ^ Section cannot be fully automated. User editing necessary after README creation. 
        - ~ Section generated only with use of verbose ``-v`` flag.

Commandline Tools
==================

.. note:: The ``genreadme`` command must be executed from the root of the application: the highest possible level of the directory. 

``genreadme``
-------------

    The ``genreadme`` command is the core functionality of write-me. Upon execution at the root level of a directory, it generates the a README for the current project. This command can be use as a standalone tool (without flagged options selected) or with up to two "options" flags.

    If the command is used without an additional flag, it generates a simple README *without* web framework-specific sections. The "URLs" and "Local Serving" sections are eliminated. This option is best for non-web application respositories, such as: data science projects, data structures, and PyPI packages.

``-d, --django``
----------------------
    
    The ``-d`` or ``--django`` flag is used to specify that the current repositiory is a web application created using the Django web framework. With this flag, the README is generated with Django-specific serving instructions, and references Django's default port 8000 for local hosting. 

    .. seealso:: https://www.djangoproject.com/

``-p, --pyramid``
----------------------
    
    The ``-p`` or ``--pyramid`` flag is used to specify that the current repositiory is a web application created using the Pyramid web framework. With this flag, the README is generated with Pyramid-specific serving instructions, and references Pyramid's default port 6543 for local hosting. 

    .. seealso:: https://trypyramid.com/

``-f, --flask``
----------------------
    
    The ``-f`` or ``--flask`` flag is used to specify that the current repositiory is a web application created using the Flask web framework. With this flag, the README is generated with Flask-specific serving instructions, and references Flask's default port 5000 for local hosting. 

    .. seealso:: http://flask.pocoo.org/

``-v, --verbose``
----------------------

    The ``-v`` or ``--verbose`` flag is used to create a longer and more verbose version of the default generated README. If used without any other web framework flag, this tag only adds the following section: 

    - Documentation (links to other documentation sources)
    - Contributions (provides contact information for open source contributors)

    When used *with* one of the web framework flags, it adds the two sections above, as well as the following section: 

    - Modules (lists all Python modules used in the project)


``-h, --help``
----------------------

    The ``-h`` or ``--help`` flag is used to show all write-me commandline options at the Terminal. When used, it displays a short description of the ``-d``, ``-p``, ``-f``, and ``-v`` flags, and exits out of the write-me commandline tool. 









