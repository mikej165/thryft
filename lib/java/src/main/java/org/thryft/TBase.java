package org.thryft;

import java.io.IOException;
import java.io.Serializable;

import org.thryft.protocol.TProtocol;

public interface TBase<T extends TBase<?>> extends Comparable<T>, Serializable {
    public void write(TProtocol oprot) throws IOException;
}
