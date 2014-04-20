package org.thryft;

import java.io.Serializable;

import org.thryft.protocol.OutputProtocol;
import org.thryft.protocol.OutputProtocolException;

public interface Base<T extends Base<?>> extends Comparable<T>, Serializable {
    public void write(OutputProtocol oprot) throws OutputProtocolException;
}
