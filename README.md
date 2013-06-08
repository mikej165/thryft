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
    * Model stores: file system; JDBC; memory; Redis; S3; SimpleDB; DynamoDB

## Installation

        git clone git://github.com/minorg/thryft.git

## Usage

The command line interface is similar to Apache Thrift's:

        python thryft/compiler/bin/thryft -h

However, it's generally easier to write a simple Python script that uses the generators as a library.
An example script that generates test code can be found in

        thryft/lib/thrift/devbin/generate_src.py

## License
2-clause BSD
