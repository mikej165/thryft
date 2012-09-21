package org.thryft.protocol.test;

import java.io.IOException;
import java.io.Reader;
import java.io.Writer;

import org.thryft.protocol.CsvProtocol;

public class CsvProtocolTest extends ProtocolTest {
    @Override
    protected CsvProtocol _newProtocol(final Reader reader) throws IOException {
        return new CsvProtocol(reader);
    }

    @Override
    protected CsvProtocol _newProtocol(final Writer writer) throws IOException {
        throw new UnsupportedOperationException();
        // return new CsvProtocol(writer);
    }
}
