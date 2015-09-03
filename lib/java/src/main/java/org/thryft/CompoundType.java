package org.thryft;

import org.thryft.protocol.OutputProtocol;
import org.thryft.protocol.OutputProtocolException;

public interface CompoundType {
    public interface Field {
        public int getId();

        public String getProtocolKey();

        public org.thryft.protocol.Type getProtocolType();

        public String getThriftName();

        public boolean hasId();

        public boolean isRequired();

    }

    public Object get(final String fieldName);

    public void writeAsList(OutputProtocol oprot) throws OutputProtocolException;

    public void writeAsStruct(OutputProtocol oprot) throws OutputProtocolException;
}
