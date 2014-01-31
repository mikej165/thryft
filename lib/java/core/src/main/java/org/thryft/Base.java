package org.thryft;

import java.io.IOException;
import java.io.Serializable;

import org.thryft.protocol.OutputProtocol;

public interface Base<T extends Base<?>> extends Comparable<T>, Serializable {
    public void write(OutputProtocol oprot) throws IOException;
}
