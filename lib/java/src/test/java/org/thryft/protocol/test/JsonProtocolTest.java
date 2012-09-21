package org.thryft.protocol.test;

import java.io.IOException;
import java.io.Reader;
import java.io.Writer;

import org.thryft.protocol.JsonProtocol;

public class JsonProtocolTest extends ProtocolTest {
    @Override
    protected JsonProtocol _newProtocol(final Reader reader) throws IOException {
        return new JsonProtocol(reader);
    }

    @Override
    protected JsonProtocol _newProtocol(final Writer writer) throws IOException {
        return new JsonProtocol(writer);
    }
}
