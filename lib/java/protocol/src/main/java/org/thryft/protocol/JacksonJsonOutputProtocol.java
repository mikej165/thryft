/*******************************************************************************
 * Copyright (c) 2015, Minor Gordon
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

import java.io.IOException;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.Writer;

import com.fasterxml.jackson.core.JsonFactory;
import com.google.common.annotations.GwtIncompatible;

@GwtIncompatible("")
public class JacksonJsonOutputProtocol extends JsonOutputProtocol {
    private final static class JacksonJsonGenerator implements JsonGenerator {
        private JacksonJsonGenerator(
                final com.fasterxml.jackson.core.JsonGenerator delegate) {
            this.delegate = delegate;
        }

        @Override
        public void flush() throws OutputProtocolException {
            try {
                delegate.flush();
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeBoolean(final boolean value)
                throws OutputProtocolException {
            try {
                delegate.writeBoolean(value);
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeEndArray() throws OutputProtocolException {
            try {
                delegate.writeEndArray();
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeEndObject() throws OutputProtocolException {
            try {
                delegate.writeEndObject();
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeFieldName(final String value)
                throws OutputProtocolException {
            try {
                delegate.writeFieldName(value);
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeNull() throws OutputProtocolException {
            try {
                delegate.writeNull();
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeNumber(final double value)
                throws OutputProtocolException {
            try {
                delegate.writeNumber(value);
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeNumber(final int value) throws OutputProtocolException {
            try {
                delegate.writeNumber(value);
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeNumber(final long value)
                throws OutputProtocolException {
            try {
                delegate.writeNumber(value);
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeStartArray() throws OutputProtocolException {
            try {
                delegate.writeStartArray();
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeStartObject() throws OutputProtocolException {
            try {
                delegate.writeStartObject();
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        @Override
        public void writeString(final String value)
                throws OutputProtocolException {
            try {
                delegate.writeString(value);
            } catch (final IOException e) {
                throw new OutputProtocolException(e);
            }
        }

        private final com.fasterxml.jackson.core.JsonGenerator delegate;
    }

    private static JsonGenerator __createJsonGenerator(final Writer writer)
            throws OutputProtocolException {
        try {
            return new JacksonJsonGenerator(
                    new JsonFactory().createGenerator(writer));
        } catch (final IOException e) {
            throw new OutputProtocolException(e);
        }
    }

    public JacksonJsonOutputProtocol(final JsonGenerator generator) {
        super(generator);
    }

    public JacksonJsonOutputProtocol(final OutputStream outputStream)
            throws OutputProtocolException {
        this(new OutputStreamWriter(outputStream));
    }

    public JacksonJsonOutputProtocol(final Writer writer)
            throws OutputProtocolException {
        this(__createJsonGenerator(writer));
    }
}
