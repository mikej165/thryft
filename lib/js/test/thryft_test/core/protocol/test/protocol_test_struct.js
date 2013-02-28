if (typeof thryft_test === "undefined") {
    thryft_test = new Object();
}
if (typeof thryft_test.core === "undefined") {
    thryft_test.core = new Object();
}
if (typeof thryft_test.core.protocol === "undefined") {
    thryft_test.core.protocol = new Object();
}
if (typeof thryft_test.core.protocol.test === "undefined") {
    thryft_test.core.protocol.test = new Object();
}

thryft_test.core.protocol.test.ProtocolTestStruct = Backbone.Model.extend(
    {
        binary_field:undefined,
        bool_field:undefined,
        byte_field:undefined,
        date_field:undefined,
        date_time_field:undefined,
        decimal_field:undefined,
        enum_field:undefined,
        i16_field:undefined,
        i32_field:undefined,
        i64_field:undefined,
        list_string_field:undefined,
        map_string_string_field:undefined,
        set_string_field:undefined,
        string_field:undefined,
        struct_field:undefined,

        write: function(oprot) {
            oprot.writeStructBegin("ProtocolTestStruct");
            if (this.has("binary_field")) {
                oprot.writeFieldBegin("binary_field");
                oprot.writeBinary(this.get("binary_field"));
                oprot.writeFieldEnd();
            }
            if (this.has("bool_field")) {
                oprot.writeFieldBegin("bool_field");
                oprot.writeBool(this.get("bool_field"));
                oprot.writeFieldEnd();
            }
            if (this.has("byte_field")) {
                oprot.writeFieldBegin("byte_field");
                oprot.writeByte(this.get("byte_field"));
                oprot.writeFieldEnd();
            }
            if (this.has("date_field")) {
                oprot.writeFieldBegin("date_field");
                this.get("date_field").write(oprot);
                oprot.writeFieldEnd();
            }
            if (this.has("date_time_field")) {
                oprot.writeFieldBegin("date_time_field");
                this.get("date_time_field").write(oprot);
                oprot.writeFieldEnd();
            }
            if (this.has("decimal_field")) {
                oprot.writeFieldBegin("decimal_field");
                this.get("decimal_field").write(oprot);
                oprot.writeFieldEnd();
            }
            if (this.has("enum_field")) {
                oprot.writeFieldBegin("enum_field");
                oprot.writeString(function(enumerator_value) { for (var enumerator_name in thryft_test.core.protocol.test.ProtocolTestEnum) { if (thryft_test.core.protocol.test.ProtocolTestEnum[enumerator_name] == enumerator_value) { return enumerator_name; } } }(this.get("enum_field")));
                oprot.writeFieldEnd();
            }
            if (this.has("i16_field")) {
                oprot.writeFieldBegin("i16_field");
                oprot.writeI16(this.get("i16_field"));
                oprot.writeFieldEnd();
            }
            if (this.has("i32_field")) {
                oprot.writeFieldBegin("i32_field");
                oprot.writeI32(this.get("i32_field"));
                oprot.writeFieldEnd();
            }
            if (this.has("i64_field")) {
                oprot.writeFieldBegin("i64_field");
                oprot.writeI64(this.get("i64_field"));
                oprot.writeFieldEnd();
            }
            if (this.has("list_string_field")) {
                oprot.writeFieldBegin("list_string_field");
                var __sequence0 = this.get("list_string_field");
                oprot.writeListBegin(11, __sequence0.length);
                for (var __i0 = 0; __i0 < __sequence0.length; __i0++) {
                    oprot.writeString(__sequence0[__i0]);
                }
                oprot.writeListEnd();
                oprot.writeFieldEnd();
            }
            if (this.has("map_string_string_field")) {
                oprot.writeFieldBegin("map_string_string_field");
                var __map0 = this.get("map_string_string_field");
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
            if (this.has("set_string_field")) {
                oprot.writeFieldBegin("set_string_field");
                var __sequence0 = this.get("set_string_field");
                oprot.writeSetBegin(11, __sequence0.length);
                for (var __i0 = 0; __i0 < __sequence0.length; __i0++) {
                    oprot.writeString(__sequence0[__i0]);
                }
                oprot.writeSetEnd();
                oprot.writeFieldEnd();
            }
            if (this.has("string_field")) {
                oprot.writeFieldBegin("string_field");
                oprot.writeString(this.get("string_field"));
                oprot.writeFieldEnd();
            }
            if (this.has("struct_field")) {
                oprot.writeFieldBegin("struct_field");
                this.get("struct_field").write(oprot);
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
                    fields["binary_field"] = iprot.readBinary();
                } else if (field.fname == "bool_field") {
                    fields["bool_field"] = iprot.readBool();
                } else if (field.fname == "byte_field") {
                    fields["byte_field"] = iprot.readByte();
                } else if (field.fname == "date_field") {
                    fields["date_field"] = thryft.util.Date.read(iprot);
                } else if (field.fname == "date_time_field") {
                    fields["date_time_field"] = thryft.util.DateTime.read(iprot);
                } else if (field.fname == "decimal_field") {
                    fields["decimal_field"] = thryft.util.Decimal.read(iprot);
                } else if (field.fname == "enum_field") {
                    fields["enum_field"] = thryft_test.core.protocol.test.ProtocolTestEnum[iprot.readString()];
                } else if (field.fname == "i16_field") {
                    fields["i16_field"] = iprot.readI16();
                } else if (field.fname == "i32_field") {
                    fields["i32_field"] = iprot.readI32();
                } else if (field.fname == "i64_field") {
                    fields["i64_field"] = iprot.readI64();
                } else if (field.fname == "list_string_field") {
                    fields["list_string_field"] = function(iprot) { var sequenceBegin = iprot.readListBegin(); var sequence = new Array(); for (var i = 0; i < sequenceBegin.size; i++) { sequence.push(iprot.readString()); } iprot.readListEnd(); return sequence; }(iprot);
                } else if (field.fname == "map_string_string_field") {
                    fields["map_string_string_field"] = function(iprot) { var map = {}; var mapBegin = iprot.readMapBegin(); for (var i = 0; i < mapBegin.size; i++) { var key = iprot.readString(); var value = iprot.readString(); map[key] = value; } iprot.readMapEnd(); return map; }(iprot);
                } else if (field.fname == "set_string_field") {
                    fields["set_string_field"] = function(iprot) { var sequenceBegin = iprot.readSetBegin(); var sequence = new Array(); for (var i = 0; i < sequenceBegin.size; i++) { sequence.push(iprot.readString()); } iprot.readSetEnd(); return sequence; }(iprot);
                } else if (field.fname == "string_field") {
                    fields["string_field"] = iprot.readString();
                } else if (field.fname == "struct_field") {
                    fields["struct_field"] = thryft_test.core.protocol.test.ProtocolTestStruct.read(iprot);
                }
                iprot.readFieldEnd();
            }
            iprot.readStructEnd();
            return new thryft_test.core.protocol.test.ProtocolTestStruct(fields);
        }
    }
);

