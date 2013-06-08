/*******************************************************************************
 * Copyright (c) 2013, Minor Gordon
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 * 
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in
 *       the documentation and/or other materials provided with the
 *       distribution.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
 * CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
 * INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL  DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
 * LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
 * OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
 * OF SUCH DAMAGE.
 ******************************************************************************/

// line 1 "UrnParser.rl"
package org.thryft.native_;

public final class UrnParser {

    // line 11 "UrnParser.rl"

    public static Urn parseUrn(final String urn) {
        if (urn == null) {
            throw new NullPointerException();
        }

        // Ragel state machine variables
        final byte[] data = urn.getBytes();
        int p = 0;
        final int pe = data.length;
        final int eof = pe;
        int cs = 0;

        // Variables used by actions
        int mark = 0;
        String namespaceIdentifier = null;
        String namespaceSpecificString = null;

        // line 4 "UrnParser.java"
        {
            cs = UrnParser_start;
        }

        // line 31 "UrnParser.rl"

        // line 9 "UrnParser.java"
        {
            int _klen;
            int _trans = 0;
            int _acts;
            int _nacts;
            int _keys;
            int _goto_targ = 0;

            _goto: while (true) {
                switch (_goto_targ) {
                case 0:
                    if (p == pe) {
                        _goto_targ = 4;
                        continue _goto;
                    }
                    if (cs == 0) {
                        _goto_targ = 5;
                        continue _goto;
                    }
                case 1:
                    _match: do {
                        _keys = _UrnParser_key_offsets[cs];
                        _trans = _UrnParser_index_offsets[cs];
                        _klen = _UrnParser_single_lengths[cs];
                        if (_klen > 0) {
                            int _lower = _keys;
                            int _mid;
                            int _upper = _keys + _klen - 1;
                            while (true) {
                                if (_upper < _lower) {
                                    break;
                                }

                                _mid = _lower + ((_upper - _lower) >> 1);
                                if (data[p] < _UrnParser_trans_keys[_mid]) {
                                    _upper = _mid - 1;
                                } else if (data[p] > _UrnParser_trans_keys[_mid]) {
                                    _lower = _mid + 1;
                                } else {
                                    _trans += (_mid - _keys);
                                    break _match;
                                }
                            }
                            _keys += _klen;
                            _trans += _klen;
                        }

                        _klen = _UrnParser_range_lengths[cs];
                        if (_klen > 0) {
                            int _lower = _keys;
                            int _mid;
                            int _upper = _keys + (_klen << 1) - 2;
                            while (true) {
                                if (_upper < _lower) {
                                    break;
                                }

                                _mid = _lower + (((_upper - _lower) >> 1) & ~1);
                                if (data[p] < _UrnParser_trans_keys[_mid]) {
                                    _upper = _mid - 2;
                                } else if (data[p] > _UrnParser_trans_keys[_mid + 1]) {
                                    _lower = _mid + 2;
                                } else {
                                    _trans += ((_mid - _keys) >> 1);
                                    break _match;
                                }
                            }
                            _trans += _klen;
                        }
                    } while (false);

                    _trans = _UrnParser_indicies[_trans];
                    cs = _UrnParser_trans_targs[_trans];

                    if (_UrnParser_trans_actions[_trans] != 0) {
                        _acts = _UrnParser_trans_actions[_trans];
                        _nacts = _UrnParser_actions[_acts++];
                        while (_nacts-- > 0) {
                            switch (_UrnParser_actions[_acts++]) {
                            case 0:
                            // line 8 "UrnParser.rl"
                            {
                                mark = p;
                            }
                                break;
                            case 1:
                            // line 8 "UrnParser.rl"
                            {
                                namespaceIdentifier = new String(data, mark, p
                                        - mark);
                            }
                                break;
                            case 2:
                            // line 10 "UrnParser.rl"
                            {
                                mark = p;
                            }
                                break;
                            // line 101 "UrnParser.java"
                            }
                        }
                    }

                case 2:
                    if (cs == 0) {
                        _goto_targ = 5;
                        continue _goto;
                    }
                    if (++p != pe) {
                        _goto_targ = 1;
                        continue _goto;
                    }
                case 4:
                    if (p == eof) {
                        int __acts = _UrnParser_eof_actions[cs];
                        int __nacts = _UrnParser_actions[__acts++];
                        while (__nacts-- > 0) {
                            switch (_UrnParser_actions[__acts++]) {
                            case 3:
                            // line 10 "UrnParser.rl"
                            {
                                namespaceSpecificString = new String(data,
                                        mark, p - mark);
                            }
                                break;
                            // line 126 "UrnParser.java"
                            }
                        }
                    }

                case 5:
                }
                break;
            }
        }

        // line 32 "UrnParser.rl"

        if (namespaceIdentifier == null) {
            throw new IllegalArgumentException(urn);
        } else if (namespaceSpecificString == null) {
            throw new IllegalArgumentException(urn);
        }

        return new Urn(namespaceIdentifier, namespaceSpecificString, urn);
    }

    // line 136 "UrnParser.java"
    private static byte[] init__UrnParser_actions_0() {
        return new byte[] { 0, 1, 0, 1, 1, 1, 2, 1, 3 };
    }

    private static byte[] init__UrnParser_eof_actions_0() {
        return new byte[] { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7 };
    }

    private static byte[] init__UrnParser_index_offsets_0() {
        return new byte[] { 0, 0, 2, 4, 6, 8, 19, 30, 34, 38, 48, 52, 56 };
    }

    private static byte[] init__UrnParser_indicies_0() {
        return new byte[] { 0, 1, 2, 1, 3, 1, 4, 1, 5, 6, 5, 5, 5, 5, 5, 5, 5,
                5, 1, 7, 8, 9, 7, 7, 7, 7, 7, 7, 7, 1, 10, 10, 10, 1, 7, 7, 7,
                1, 11, 12, 11, 11, 11, 11, 11, 11, 11, 1, 13, 13, 13, 1, 14,
                14, 14, 1, 14, 15, 14, 14, 14, 14, 14, 14, 14, 1, 0 };
    }

    private static byte[] init__UrnParser_key_offsets_0() {
        return new byte[] { 0, 0, 1, 2, 3, 4, 18, 32, 38, 44, 57, 63, 69 };
    }

    private static byte[] init__UrnParser_range_lengths_0() {
        return new byte[] { 0, 0, 0, 0, 0, 4, 4, 3, 3, 4, 3, 3, 4 };
    }

    private static byte[] init__UrnParser_single_lengths_0() {
        return new byte[] { 0, 1, 1, 1, 1, 6, 6, 0, 0, 5, 0, 0, 5 };
    }

    private static byte[] init__UrnParser_trans_actions_0() {
        return new byte[] { 0, 0, 0, 0, 0, 1, 1, 0, 0, 3, 0, 5, 5, 0, 0, 0 };
    }

    private static char[] init__UrnParser_trans_keys_0() {
        return new char[] { 117, 114, 110, 58, 33, 37, 59, 61, 95, 126, 36, 46,
                48, 57, 64, 90, 97, 122, 33, 37, 58, 61, 95, 126, 36, 46, 48,
                59, 64, 90, 97, 122, 48, 57, 65, 70, 97, 102, 48, 57, 65, 70,
                97, 102, 33, 37, 61, 95, 126, 36, 46, 48, 59, 64, 90, 97, 122,
                48, 57, 65, 70, 97, 102, 48, 57, 65, 70, 97, 102, 33, 37, 61,
                95, 126, 36, 46, 48, 59, 64, 90, 97, 122, 0 };
    }

    private static byte[] init__UrnParser_trans_targs_0() {
        return new byte[] { 2, 0, 3, 4, 5, 6, 7, 6, 7, 9, 8, 12, 10, 11, 12, 10 };
    }

    private static final byte _UrnParser_actions[] = init__UrnParser_actions_0();

    private static final byte _UrnParser_key_offsets[] = init__UrnParser_key_offsets_0();

    private static final char _UrnParser_trans_keys[] = init__UrnParser_trans_keys_0();

    private static final byte _UrnParser_single_lengths[] = init__UrnParser_single_lengths_0();

    private static final byte _UrnParser_range_lengths[] = init__UrnParser_range_lengths_0();

    private static final byte _UrnParser_index_offsets[] = init__UrnParser_index_offsets_0();

    private static final byte _UrnParser_indicies[] = init__UrnParser_indicies_0();

    private static final byte _UrnParser_trans_targs[] = init__UrnParser_trans_targs_0();

    private static final byte _UrnParser_trans_actions[] = init__UrnParser_trans_actions_0();

    private static final byte _UrnParser_eof_actions[] = init__UrnParser_eof_actions_0();

    static final int UrnParser_start = 1;
    static final int UrnParser_first_final = 12;
    static final int UrnParser_error = 0;

    static final int UrnParser_en_main = 1;

    // line 43 "UrnParser.rl"
}
