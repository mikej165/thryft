/*******************************************************************************
 * Copyright (c) 2013, Minor Gordon
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in
 *       the documentation and/or other materials provided with the
 *       distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
 * CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
 * INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL  DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
 * LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
 * OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
 * OF SUCH DAMAGE.
 ******************************************************************************/

package org.thryft.protocol;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class LoggingOutputProtocol extends AbstractOutputProtocol {
    public LoggingOutputProtocol(final OutputProtocol wrappedProtocol) {
        logger = LoggerFactory.getLogger(wrappedProtocol.getClass());
        this.wrappedProtocol = wrappedProtocol;
    }

    @Override
    public void writeBinary(final byte[] buf) throws OutputProtocolException {
        final String message = "writeBinary(" + __toString(buf) + " bytes)";
        try {
            wrappedProtocol.writeBinary(buf);
            logger.info(message);
        } catch (final OutputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
            throw e;
        }
    }

    @Override
    public void writeBool(final boolean b) throws OutputProtocolException {
        final String message = "writeBool(" + b + ")";
        try {
            wrappedProtocol.writeBool(b);
            logger.info(message);
        } catch (final OutputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeByte(final byte b) throws OutputProtocolException {
        final String message = "writeByte(" + b + ")";
        try {
            wrappedProtocol.writeByte(b);
            logger.info(message);
        } catch (final OutputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeDouble(final double dub) throws OutputProtocolException {
        final String message = "writeDouble(" + dub + ")";
        try {
            wrappedProtocol.writeDouble(dub);
            logger.info(message);
        } catch (final OutputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeFieldBegin(final FieldBegin field)
            throws OutputProtocolException {
        final String message = "writeFieldBegin(" + field.toString() + ")";
        try {
            wrappedProtocol.writeFieldBegin(field);
            logger.info(message);
        } catch (final OutputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeFieldEnd() throws OutputProtocolException {
        final String message = "writeFieldEnd()";
        try {
            wrappedProtocol.writeFieldEnd();
            logger.info(message);
        } catch (final OutputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeFieldStop() throws OutputProtocolException {
        final String message = "writeFieldStop()";
        try {
            wrappedProtocol.writeFieldStop();
            logger.info(message);
        } catch (final OutputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeI16(final short i16) throws OutputProtocolException {
        final String message = "writeI16(" + i16 + ")";
        try {
            wrappedProtocol.writeI16(i16);
            logger.info(message);
        } catch (final OutputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeI32(final int i32) throws OutputProtocolException {
        final String message = "writeI32(" + i32 + ")";
        try {
            wrappedProtocol.writeI32(i32);
            logger.info(message);
        } catch (final OutputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeI64(final long i64) throws OutputProtocolException {
        final String message = "writeI64(" + i64 + ")";
        try {
            wrappedProtocol.writeI64(i64);
            logger.info(message);
        } catch (final OutputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeListBegin(final ListBegin list)
            throws OutputProtocolException {
        final String message = "writeListBegin(" + __toString(list) + ")";
        try {
            wrappedProtocol.writeListBegin(list);
            logger.info(message);
        } catch (final OutputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
            throw e;
        }
    }

    @Override
    public void writeListEnd() throws OutputProtocolException {
        final String message = "writeListEnd()";
        try {
            wrappedProtocol.writeListEnd();
            logger.info(message);
        } catch (final OutputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeMapBegin(final MapBegin map)
            throws OutputProtocolException {
        final String message = "writeMapBegin(" + __toString(map) + ")";
        try {
            wrappedProtocol.writeMapBegin(map);
            logger.info(message);
        } catch (final OutputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeMapEnd() throws OutputProtocolException {
        final String message = "writeMapEnd()";
        try {
            wrappedProtocol.writeMapEnd();
            logger.info(message);
        } catch (final OutputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeSetBegin(final SetBegin set)
            throws OutputProtocolException {
        final String message = "writeSetBegin(" + __toString(set) + ")";
        try {
            wrappedProtocol.writeSetBegin(set);
            logger.info(message);
        } catch (final OutputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
            throw e;
        }
    }

    @Override
    public void writeSetEnd() throws OutputProtocolException {
        final String message = "writeSetEnd()";
        try {
            wrappedProtocol.writeSetEnd();
            logger.info(message);
        } catch (final OutputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeString(final String str) throws OutputProtocolException {
        final String message = "writeString(" + str + ")";
        try {
            wrappedProtocol.writeString(str);
            logger.info(message);
        } catch (final OutputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeStructBegin(final StructBegin struct)
            throws OutputProtocolException {
        final String message = "writeStructBegin(" + __toString(struct) + ")";
        try {
            wrappedProtocol.writeStructBegin(struct);
            logger.info(message);
        } catch (final OutputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    @Override
    public void writeStructEnd() throws OutputProtocolException {
        final String message = "writeStructEnd()";
        try {
            wrappedProtocol.writeStructEnd();
            logger.info(message);
        } catch (final OutputProtocolException e) {
            logger.info(message + " -> " + __toString(e));
        }
    }

    private final String __toString(final byte[] bytes) {
        return "bytes[length=" + Integer.toString(bytes.length) + "]";
    }

    private final String __toString(final Exception e) {
        return "exception: " + e.getMessage();
    }

    private final String __toString(final ListBegin list) {
        return "TList(" + Byte.toString(list.elemType) + ", "
                + Integer.toString(list.size) + ")";
    }

    private final String __toString(final MapBegin map) {
        return "TMap(" + Byte.toString(map.keyType) + ", "
                + Byte.toString(map.valueType) + ", "
                + Integer.toString(map.size) + ")";
    }

    private final String __toString(final SetBegin set) {
        return "TSet(" + Byte.toString(set.elemType) + ", "
                + Integer.toString(set.size) + ")";
    }

    private final String __toString(final StructBegin struct) {
        return "TStruct(" + struct.name + ")";
    }

    private final Logger logger;
    private final OutputProtocol wrappedProtocol;
}
