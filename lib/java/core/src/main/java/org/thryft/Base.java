package org.thryft;

import java.io.Serializable;

import org.thryft.protocol.OutputProtocol;
import org.thryft.protocol.OutputProtocolException;

public interface Base<T extends Base<?>> extends Comparable<T>, Serializable {
    public void writeAsList(OutputProtocol oprot)
            throws OutputProtocolException;

    public void writeAsStruct(OutputProtocol oprot)
            throws OutputProtocolException;
}
