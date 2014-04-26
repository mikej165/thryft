package org.thryft.protocol.test;

import static org.junit.Assert.assertEquals;

import java.io.IOException;
import java.io.StringWriter;
import java.io.Writer;

import org.junit.Test;
import org.thryft.protocol.InputProtocol;
import org.thryft.protocol.JacksonJsonInputProtocol;
import org.thryft.protocol.JacksonJsonOutputProtocol;
import org.thryft.protocol.JsonRpcErrorResponse;
import org.thryft.protocol.JsonRpcInputProtocol;
import org.thryft.protocol.JsonRpcOutputProtocol;
import org.thryft.protocol.LoggingOutputProtocol;
import org.thryft.protocol.MessageBegin;
import org.thryft.protocol.MessageType;
import org.thryft.protocol.OutputProtocol;
import org.thryft.protocol.ProtocolException;
import org.thryft.protocol.SetBegin;

import com.google.common.collect.ImmutableSet;

public final class JsonRpcProtocolTest {
    @Test
    public void testCall() throws ProtocolException, IOException {
        final StringWriter writer = new StringWriter();
        final OutputProtocol oprot = __newJsonRpcOutputProtocol(writer);
        oprot.writeMessageBegin("call", MessageType.CALL, ID);
        final ImmutableSet<String> expectedParams = ImmutableSet.of("test1",
                "test2");
        oprot.writeMixed(expectedParams);
        oprot.writeMessageEnd();
        oprot.flush();
        final String json = writer.toString();

        final InputProtocol iprot = __newJsonRpcInputProtocol(json);
        final MessageBegin messageBegin = iprot.readMessageBegin();
        assertEquals(ID, messageBegin.getId());
        assertEquals("call", messageBegin.getName());
        assertEquals(MessageType.CALL, messageBegin.getType());
        final SetBegin paramsBegin = iprot.readSetBegin();
        assertEquals(paramsBegin.getSize(), 2);
        assertEquals("test1", iprot.readString());
        assertEquals("test2", iprot.readString());
        iprot.readSetEnd();
        iprot.readMessageEnd();
    }

    @Test
    public void testException() throws ProtocolException, IOException {
        final StringWriter writer = new StringWriter();
        final OutputProtocol oprot = __newJsonRpcOutputProtocol(writer);
        oprot.writeMessageBegin("exception", MessageType.EXCEPTION, ID);
        final JsonRpcErrorResponse expectedError = new JsonRpcErrorResponse(
                -32600, "some message");
        expectedError.write(oprot);
        oprot.writeMessageEnd();
        oprot.flush();
        final String json = writer.toString();

        final InputProtocol iprot = __newJsonRpcInputProtocol(json);
        final MessageBegin messageBegin = iprot.readMessageBegin();
        assertEquals(ID, messageBegin.getId());
        assertEquals(MessageType.EXCEPTION, messageBegin.getType());
        final JsonRpcErrorResponse actualError = JsonRpcErrorResponse
                .read(iprot);
        iprot.readMessageEnd();
        assertEquals(expectedError, actualError);
    }

    @Test
    public void testReply() throws ProtocolException, IOException {
        final StringWriter writer = new StringWriter();
        final OutputProtocol oprot = __newJsonRpcOutputProtocol(writer);
        oprot.writeMessageBegin("reply", MessageType.REPLY, ID);
        final ImmutableSet<String> expectedResults = ImmutableSet.of("test1",
                "test2");
        oprot.writeMixed(expectedResults);
        oprot.writeMessageEnd();
        oprot.flush();
        final String json = writer.toString();

        final InputProtocol iprot = __newJsonRpcInputProtocol(json);
        final MessageBegin messageBegin = iprot.readMessageBegin();
        assertEquals(ID, messageBegin.getId());
        assertEquals(MessageType.REPLY, messageBegin.getType());
        final SetBegin resultsBegin = iprot.readSetBegin();
        assertEquals(resultsBegin.getSize(), 2);
        assertEquals("test1", iprot.readString());
        assertEquals("test2", iprot.readString());
        iprot.readSetEnd();
        iprot.readMessageEnd();
    }

    private InputProtocol __newJsonRpcInputProtocol(final String json)
            throws IOException {
        return new JsonRpcInputProtocol(new JacksonJsonInputProtocol(json));
    }

    private OutputProtocol __newJsonRpcOutputProtocol(final Writer writer)
            throws IOException {
        return new LoggingOutputProtocol(
                new JsonRpcOutputProtocol(new LoggingOutputProtocol(
                        new JacksonJsonOutputProtocol(writer))));
    }

    private final static Object ID = 1;
}
