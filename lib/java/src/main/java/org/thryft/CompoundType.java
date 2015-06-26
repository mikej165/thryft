package org.thryft;

import org.thryft.protocol.OutputProtocol;
import org.thryft.protocol.OutputProtocolException;

public interface CompoundType {
    public void writeAsList(OutputProtocol oprot)
            throws OutputProtocolException;

    public void writeAsStruct(OutputProtocol oprot)
            throws OutputProtocolException;
}
