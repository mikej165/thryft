package org.thryft;

import org.thryft.protocol.OutputProtocol;
import org.thryft.protocol.OutputProtocolException;

public interface CompoundType {
    public interface FieldMetadata {
        public com.google.common.reflect.TypeToken<?> getJavaType();

        public int getThriftId();

        public String getThriftName();

        public String getThriftProtocolKey();

        public org.thryft.protocol.Type getThriftProtocolType();

        public boolean hasThriftId();

        public boolean isRequired();
    }

    public Object get(final String fieldName);

    public void writeAsList(OutputProtocol oprot) throws OutputProtocolException;

    public void writeAsStruct(OutputProtocol oprot) throws OutputProtocolException;

    public void writeFields(OutputProtocol oprot) throws OutputProtocolException;
}
