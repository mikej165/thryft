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

package org.thryft.store.test;

import java.io.File;
import java.io.IOException;

import org.junit.Before;
import org.thryft.store.FileUtils;
import org.thryft.store.FsStore;

public class FsStoreTest extends StoreTest {
    public static FsStore.Configuration getFsStoreConfiguration()
            throws IOException {
        if (fsStoreConfiguration == null) {
            final File rootDirectoryPath = FileUtils.createTempDirectory(
                    FsStoreTest.class.getSimpleName(), null);
            fsStoreConfiguration = new FsStore.Configuration(rootDirectoryPath);
        }

        return fsStoreConfiguration;
    }

    @Before
    public void setUp() throws IOException {
        org.apache.commons.io.FileUtils
                .deleteDirectory(getFsStoreConfiguration()
                        .getRootDirectoryPath());
        super._setUp(new FsStore<StoreTestStruct>(getFsStoreConfiguration(),
                StoreTestStruct.class));
    }

    private static FsStore.Configuration fsStoreConfiguration = null;
}
