# Thryft: a code generation framework for multilingual web application development

## Summary

Thryft accepts Apache Thrift interface definitions and generates:

* Java immutable models, service interfaces, abstract service stubs, unit test templates, logging service wrappers, and REST and JSON-RPC servlet bridges to services
* Python models and JSON-RPC service clients
* Backbone.js models and jQuery .ajax service clients

Thryft is written in Python using a SPARK parser and syntax-directed translation.

Thryft does not share any code with Apache Thrift, and it is not intended to be a complete rewrite of the latter.
Among other things, Thryft does not currently a number of secondary IDL features such as senums. Thryft's runtime library is also quite different from Apache Thrift's and e.g., does not support field numbering.

Thryft does have a number of features that are not present in Apache Thrift:

* Support for additional "native" types using custom, dynamically-loaded code generators:
    * URLs
    * email addresses
    * BigDecimals
    * datetimes
* Annotations in Javadoc-style comments that can generate:
    * Javadoc on Java models and services
    * Shiro @Requires annotations
    * Faker.js-compatible calls
    * Jsdoc
    * Backbone.Forms and Backbone.Validation properties
* A Java runtime library that provides:
    * Model marshalling protocols: CSV; JSON; string maps

## Installation

        git clone git://github.com/minorg/thryft.git

## Usage

The command line interface is similar to Apache Thrift's:

        python thryft/compiler/bin/thryft -h

However, it's generally easier to write a simple Python script that uses the generators as a library.
An example script that generates test code can be found in

        thryft/lib/thrift/devbin/generate_src.py

## Software architecture / source overview

The compiler (`compiler.py`) is the heart of Thryft. The compiler:
* accepts files in .thrift at its entry point (`compile`), along with an instance of `Generator` (`generator.py`), such as `JavaGenerator` (`java_generator.py`)
* lexes and parses them with SPARK (`parser.py`)
* creates an Abstract Syntax Tree (AST, classes in `ast.py`) representing the constructs in the .thrift, such as the root document, struct types, fields, et al.
* for every node in the AST, creates a corresponding instance of the class in the Generator e.g., JavaGenerator.Document
* tells the root of the generator instance tree (`JavaGenerator.Document`, in this case) to save itself to files using the `Document.save` method

## Coding conventions

PEP8, with a few additions:
* All of the logic is part of a class method; there are no freestanding functions, except the ancient utility functions in `yutil.py`.
* There is one class per file, and the file is the underscore_separated version of the CamelCase class name.
* Protected methods are prefixed with `_`. Private methods are prefixed with `__`.
* Methods, members, and parameters are listed in alphabetical order where feasible (i.e., not interdependent nested classes), ignoring leading underscores. The exception is `__init__`, which is always the first method listed. Nested classes and class constants come before all methods.

The repository uses the [nvie.com branching model](http://nvie.com/posts/a-successful-git-branching-model/).

## License
2-clause BSD
