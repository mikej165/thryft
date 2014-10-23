if (typeof thryft_test === "undefined") {
    thryft_test = new Object();
}
if (typeof thryft_test.protocol === "undefined") {
    thryft_test.protocol = new Object();
}
if (typeof thryft_test.protocol.test === "undefined") {
    thryft_test.protocol.test = new Object();
}

thryft_test.protocol.test.NestedProtocolTestStruct = Backbone.Model.extend(
    {
        schema: {
            "stringListField": {
                "type": "List",
                "itemType": "Text"
            },
            "byteField": {
                "type": "Number"
            },
            "i16Field": {
                "type": "Number"
            },
            "binaryField": {
                "type": "Text"
            },
            "requiredI32Field": {
                "type": "Number",
                "validators": [
                    "required"
                ]
            },
            "stringField": {
                "type": "Text"
            },
            "requiredStringField": {
                "type": "Text",
                "validators": [
                    "required"
                ]
            },
            "emailAddressField": {
                "type": "Text",
                "validators": [
                    "email"
                ]
            },
            "boolField": {
                "type": "Checkboxes",
                "options": [
                    ""
                ]
            },
            "dateTimeField": {
                "type": "DateTime"
            },
            "urlField": {
                "type": "Text",
                "validators": [
                    "url"
                ]
            },
            "i32Field": {
                "type": "Number"
            },
            "i64Field": {
                "type": "Number"
            },
            "enumField": {
                "type": "Select",
                "options": [
                    "ENUMERATOR1",
                    "ENUMERATOR2"
                ]
            },
            "stringSetField": {
                "type": "List",
                "itemType": "Text"
            },
            "stringStringMapField": {
                "type": "Object",
                "subSchema": {
                    "type": "Text"
                }
            },
            "decimalField": {
                "type": "Number"
            }
        },

        validation: {
            binaryField: {
                "fn": function(value, attr, computedState) {
                    if (typeof attr !== "undefined" && attr !== "null") {
                        if (typeof value !== "string") {
                            return "expected thryft_test.protocol.test.NestedProtocolTestStruct.binaryField to be a string";
                        }
                    }
                },
                "required": false
            },

            boolField: {
                "fn": function(value, attr, computedState) {
                    if (typeof attr !== "undefined" && attr !== "null") {
                        if (typeof value !== "boolean") {
                            return "expected thryft_test.protocol.test.NestedProtocolTestStruct.boolField to be a boolean";
                        }
                    }
                },
                "oneOf": [true, false], "required": false
            },

            byteField: {
                "fn": function(value, attr, computedState) {
                    if (typeof attr !== "undefined" && attr !== "null") {
                        if (typeof value !== "number") {
                            return "expected thryft_test.protocol.test.NestedProtocolTestStruct.byteField to be a number";
                        }
                    }
                },
                "required": false
            },

            dateTimeField: {
                "fn": function(value, attr, computedState) {
                    if (typeof attr !== "undefined" && attr !== "null") {
                        if (!(value instanceof Date)) {
                            return "expected thryft_test.protocol.test.NestedProtocolTestStruct.dateTimeField to be a Date";
                        }
                    }
                },
                "required": false
            },

            decimalField: {
                "fn": function(value, attr, computedState) {
                    if (typeof attr !== "undefined" && attr !== "null") {
                        if (typeof value !== "string") {
                            return "expected thryft_test.protocol.test.NestedProtocolTestStruct.decimalField to be a string";
                        }
                    }
                },
                "pattern": "number", "required": false
            },

            emailAddressField: {
                "fn": function(value, attr, computedState) {
                    if (typeof attr !== "undefined" && attr !== "null") {
                        if (typeof value !== "string") {
                            return "expected thryft_test.protocol.test.NestedProtocolTestStruct.emailAddressField to be a string";
                        }
                    }
                },
                "minLength": 6, "required": false, "pattern": "email"
            },

            enumField: {
                "fn": function(value, attr, computedState) {
                    if (typeof attr !== "undefined" && attr !== "null") {
                        if (typeof value !== "number") {
                            return "expected thryft_test.protocol.test.NestedProtocolTestStruct.enumField to be a number";
                        }
                        if (value !== 1 && value !== 2) {
                            return "thryft_test.protocol.test.NestedProtocolTestStruct.enumField is not a valid enumerator of thryft_test.protocol.test.ProtocolTestEnum";
                        }
                    }
                },
                "required": false
            },

            i16Field: {
                "fn": function(value, attr, computedState) {
                    if (typeof attr !== "undefined" && attr !== "null") {
                        if (typeof value !== "number") {
                            return "expected thryft_test.protocol.test.NestedProtocolTestStruct.i16Field to be a number";
                        }
                    }
                },
                "required": false
            },

            i32Field: {
                "fn": function(value, attr, computedState) {
                    if (typeof attr !== "undefined" && attr !== "null") {
                        if (typeof value !== "number") {
                            return "expected thryft_test.protocol.test.NestedProtocolTestStruct.i32Field to be a number";
                        }
                    }
                },
                "required": false
            },

            i64Field: {
                "fn": function(value, attr, computedState) {
                    if (typeof attr !== "undefined" && attr !== "null") {
                        if (typeof value !== "number") {
                            return "expected thryft_test.protocol.test.NestedProtocolTestStruct.i64Field to be a number";
                        }
                    }
                },
                "required": false
            },

            stringListField: {
                "fn": function(value, attr, computedState) {
                    if (typeof attr !== "undefined" && attr !== "null") {
                        if (!Array.isArray(value)) {
                            return "expected thryft_test.protocol.test.NestedProtocolTestStruct.stringListField to be an Array";
                        }
                        for (var __i0 = 0; __i0 < value.length; __i0++) {
                            if (typeof value[__i0] !== "string") {
                                return "expected thryft_test.protocol.test.NestedProtocolTestStruct.stringListField[i] to be a string";
                            }
                        }
                    }
                },
                "required": false
            },

            stringStringMapField: {
                "fn": function(value, attr, computedState) {
                    if (typeof attr !== "undefined" && attr !== "null") {
                        if (typeof value !== "object") {
                            return "expected thryft_test.protocol.test.NestedProtocolTestStruct.stringStringMapField to be an object";
                        }
                        for (var __key0 in value) {
                            var __value0 = value[__key0];
                            if (typeof __key0 !== "string") {
                                return "expected thryft_test.protocol.test.NestedProtocolTestStruct.stringStringMapField key to be a string";
                            }
                            if (typeof __value0 !== "string") {
                                return "expected thryft_test.protocol.test.NestedProtocolTestStruct.stringStringMapField value to be a string";
                            }
                        }
                    }
                },
                "required": false
            },

            requiredI32Field: {
                "fn": function(value, attr, computedState) {
                    if (typeof value !== "number") {
                        return "expected thryft_test.protocol.test.NestedProtocolTestStruct.requiredI32Field to be a number";
                    }
                },
                "required": true
            },

            requiredStringField: {
                "fn": function(value, attr, computedState) {
                    if (typeof value !== "string") {
                        return "expected thryft_test.protocol.test.NestedProtocolTestStruct.requiredStringField to be a string";
                    }
                },
                "minLength": 1, "required": true
            },

            stringSetField: {
                "fn": function(value, attr, computedState) {
                    if (typeof attr !== "undefined" && attr !== "null") {
                        if (!Array.isArray(value)) {
                            return "expected thryft_test.protocol.test.NestedProtocolTestStruct.stringSetField to be an Array";
                        }
                        for (var __i0 = 0; __i0 < value.length; __i0++) {
                            if (typeof value[__i0] !== "string") {
                                return "expected thryft_test.protocol.test.NestedProtocolTestStruct.stringSetField[i] to be a string";
                            }
                        }
                    }
                },
                "required": false
            },

            stringField: {
                "fn": function(value, attr, computedState) {
                    if (typeof attr !== "undefined" && attr !== "null") {
                        if (typeof value !== "string") {
                            return "expected thryft_test.protocol.test.NestedProtocolTestStruct.stringField to be a string";
                        }
                    }
                },
                "minLength": 1, "required": false
            },

            urlField: {
                "fn": function(value, attr, computedState) {
                    if (typeof attr !== "undefined" && attr !== "null") {
                        if (typeof value !== "string") {
                            return "expected thryft_test.protocol.test.NestedProtocolTestStruct.urlField to be a string";
                        }
                    }
                },
                "pattern": "url", "required": false
            }
        },

        write: function(oprot) {
            oprot.writeStructBegin("NestedProtocolTestStruct");
            if (this.has("binaryField")) {
                oprot.writeFieldBegin("binary_field");
                oprot.writeBinary(this.get("binaryField"));
                oprot.writeFieldEnd();
            }
            if (this.has("boolField")) {
                oprot.writeFieldBegin("bool_field");
                oprot.writeBool(this.get("boolField"));
                oprot.writeFieldEnd();
            }
            if (this.has("byteField")) {
                oprot.writeFieldBegin("byte_field");
                oprot.writeByte(this.get("byteField"));
                oprot.writeFieldEnd();
            }
            if (this.has("dateTimeField")) {
                oprot.writeFieldBegin("date_time_field");
                oprot.writeDateTime(this.get("dateTimeField"));
                oprot.writeFieldEnd();
            }
            if (this.has("decimalField")) {
                oprot.writeFieldBegin("decimal_field");
                oprot.writeDecimal(this.get("decimalField"));
                oprot.writeFieldEnd();
            }
            if (this.has("emailAddressField")) {
                oprot.writeFieldBegin("email_address_field");
                oprot.writeString(this.get("emailAddressField"));
                oprot.writeFieldEnd();
            }
            if (this.has("enumField")) {
                oprot.writeFieldBegin("enum_field");
                oprot.writeString(function(enumerator_value) { for (var enumerator_name in thryft_test.protocol.test.ProtocolTestEnum) { if (thryft_test.protocol.test.ProtocolTestEnum[enumerator_name] == enumerator_value) { return enumerator_name; } } }(this.get("enumField")));
                oprot.writeFieldEnd();
            }
            if (this.has("i16Field")) {
                oprot.writeFieldBegin("i16_field");
                oprot.writeI16(this.get("i16Field"));
                oprot.writeFieldEnd();
            }
            if (this.has("i32Field")) {
                oprot.writeFieldBegin("i32_field");
                oprot.writeI32(this.get("i32Field"));
                oprot.writeFieldEnd();
            }
            if (this.has("i64Field")) {
                oprot.writeFieldBegin("i64_field");
                oprot.writeI64(this.get("i64Field"));
                oprot.writeFieldEnd();
            }
            if (this.has("stringListField")) {
                oprot.writeFieldBegin("string_list_field");
                var __sequence0 = this.get("stringListField");
                oprot.writeListBegin(11, __sequence0.length);
                for (var __i0 = 0; __i0 < __sequence0.length; __i0++) {
                    oprot.writeString(__sequence0[__i0]);
                }
                oprot.writeListEnd();
                oprot.writeFieldEnd();
            }
            if (this.has("stringStringMapField")) {
                oprot.writeFieldBegin("string_string_map_field");
                var __map0 = this.get("stringStringMapField");
                var __mapSize0 = 0;
                for (var __key0 in __map0) {
                    __mapSize0++;
                }
                oprot.writeMapBegin(11, 11, __mapSize0);
                for (var __key0 in __map0) {
                    oprot.writeString(__key0);
                    oprot.writeString(__map0[__key0]);
                }
                oprot.writeMapEnd();
                oprot.writeFieldEnd();
            }
            oprot.writeFieldBegin("required_i32_field");
            oprot.writeI32(this.get("requiredI32Field"));
            oprot.writeFieldEnd();
            oprot.writeFieldBegin("required_string_field");
            oprot.writeString(this.get("requiredStringField"));
            oprot.writeFieldEnd();
            if (this.has("stringSetField")) {
                oprot.writeFieldBegin("string_set_field");
                var __sequence0 = this.get("stringSetField");
                oprot.writeSetBegin(11, __sequence0.length);
                for (var __i0 = 0; __i0 < __sequence0.length; __i0++) {
                    oprot.writeString(__sequence0[__i0]);
                }
                oprot.writeSetEnd();
                oprot.writeFieldEnd();
            }
            if (this.has("stringField")) {
                oprot.writeFieldBegin("string_field");
                oprot.writeString(this.get("stringField"));
                oprot.writeFieldEnd();
            }
            if (this.has("urlField")) {
                oprot.writeFieldBegin("url_field");
                oprot.writeString(this.get("urlField"));
                oprot.writeFieldEnd();
            }
            oprot.writeStructEnd();
            return oprot;
        }
    },
    {
        read: function(iprot) {
            var fields = {};
            iprot.readStructBegin();
            while (true) {
                var field = iprot.readFieldBegin();
                if (field.fname.length == 0) {
                    break;
                } else         if (field.fname == "binary_field") {
                    fields["binaryField"] = iprot.readBinary();
                } else if (field.fname == "bool_field") {
                    fields["boolField"] = iprot.readBool();
                } else if (field.fname == "byte_field") {
                    fields["byteField"] = iprot.readByte();
                } else if (field.fname == "date_time_field") {
                    fields["dateTimeField"] = iprot.readDateTime();
                } else if (field.fname == "decimal_field") {
                    fields["decimalField"] = iprot.readDecimal();
                } else if (field.fname == "email_address_field") {
                    fields["emailAddressField"] = iprot.readString();
                } else if (field.fname == "enum_field") {
                    fields["enumField"] = thryft_test.protocol.test.ProtocolTestEnum[iprot.readString()];
                } else if (field.fname == "i16_field") {
                    fields["i16Field"] = iprot.readI16();
                } else if (field.fname == "i32_field") {
                    fields["i32Field"] = iprot.readI32();
                } else if (field.fname == "i64_field") {
                    fields["i64Field"] = iprot.readI64();
                } else if (field.fname == "string_list_field") {
                    fields["stringListField"] = function(iprot) { var sequenceBegin = iprot.readListBegin(); var sequence = new Array(); for (var i = 0; i < sequenceBegin.size; i++) { sequence.push(iprot.readString()); } iprot.readListEnd(); return sequence; }(iprot);
                } else if (field.fname == "string_string_map_field") {
                    fields["stringStringMapField"] = function(iprot) { var map = {}; var mapBegin = iprot.readMapBegin(); for (var i = 0; i < mapBegin.size; i++) { var key = iprot.readString(); var value = iprot.readString(); map[key] = value; } iprot.readMapEnd(); return map; }(iprot);
                } else if (field.fname == "required_i32_field") {
                    fields["requiredI32Field"] = iprot.readI32();
                } else if (field.fname == "required_string_field") {
                    fields["requiredStringField"] = iprot.readString();
                } else if (field.fname == "string_set_field") {
                    fields["stringSetField"] = function(iprot) { var sequenceBegin = iprot.readSetBegin(); var sequence = new Array(); for (var i = 0; i < sequenceBegin.size; i++) { sequence.push(iprot.readString()); } iprot.readSetEnd(); return sequence; }(iprot);
                } else if (field.fname == "string_field") {
                    fields["stringField"] = iprot.readString();
                } else if (field.fname == "url_field") {
                    fields["urlField"] = iprot.readString();
                }
                iprot.readFieldEnd();
            }
            iprot.readStructEnd();
            return new thryft_test.protocol.test.NestedProtocolTestStruct(fields);
        }
    }
);
