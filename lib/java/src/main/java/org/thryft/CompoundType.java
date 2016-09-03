package org.thryft;

import org.thryft.protocol.FieldBegin;
import org.thryft.protocol.InputProtocol;
import org.thryft.protocol.InputProtocolException;
import org.thryft.protocol.OutputProtocol;
import org.thryft.protocol.OutputProtocolException;
import org.thryft.protocol.Type;

import com.google.common.base.Optional;

public interface CompoundType {
    public interface Factory<CompoundTypeT extends CompoundType> {
        public CompoundTypeT readAs(final InputProtocol iprot, final Type type) throws InputProtocolException;

        public CompoundTypeT readAs(final InputProtocol iprot, final Type type,
                final Optional<UnknownFieldCallback> unknownFieldCallback) throws InputProtocolException;

        public CompoundTypeT readAsList(final InputProtocol iprot) throws InputProtocolException;

        public CompoundTypeT readAsStruct(final InputProtocol iprot) throws InputProtocolException;

        public CompoundTypeT readAsStruct(final InputProtocol iprot,
                final Optional<UnknownFieldCallback> unknownFieldCallback) throws InputProtocolException;
    }

    public interface FieldMetadata {
        public String getJavaName();

        public com.google.common.reflect.TypeToken<?> getJavaType();

        public int getThriftId();

        public String getThriftName();

        public String getThriftProtocolKey();

        public org.thryft.protocol.Type getThriftProtocolType();

        public boolean hasThriftId();

        public boolean isRequired();
    }

    public interface UnknownFieldCallback {
        public void apply(final FieldBegin field) throws InputProtocolException;
    }

    public Object get(final FieldMetadata fieldMetadata);

    public Object get(final String fieldThriftName);

    public void writeAsList(OutputProtocol oprot) throws OutputProtocolException;

    public void writeAsStruct(OutputProtocol oprot) throws OutputProtocolException;

    public void writeFields(OutputProtocol oprot) throws OutputProtocolException;
}
