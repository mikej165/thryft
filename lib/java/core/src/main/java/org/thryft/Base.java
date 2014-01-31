package org.thryft;

import java.io.IOException;
import java.io.Serializable;

import org.thryft.protocol.Protocol;

public interface Base<T extends Base<?>> extends Comparable<T>, Serializable {
    public void write(Protocol oprot) throws IOException;
}
