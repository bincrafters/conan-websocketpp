#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools


class WebsocketPPConan(ConanFile):
    name = "websocketpp"
    version = "0.7.0"
    url = "https://github.com/bincrafters/conan-websocketpp"
    description = "Header only C++ library that implements RFC6455 The WebSocket Protocol"
    license = "BSD 3-Clause"
    source_subfolder = "sources"
    requires =  (
        "OpenSSL/[>=1.0.2l]@conan/stable", 
        "zlib/[>=1.2.8]@conan/stable", 
        "Boost.Random/[>=1.64.0]@bincrafters/stable", 
        "Boost.System/[>=1.64.0]@bincrafters/stable", 
        "Boost.Thread/[>=1.64.0]@bincrafters/stable", 
        "Boost.Asio/[>=1.64.0]@bincrafters/stable"
    )
                      
    def source(self):
        archive_name = "{0}-{1}".format(self.name, self.version)
        source_url = "https://github.com/zaphoyd/websocketpp"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.version))
        os.rename(archive_name, self.source_subfolder)

    def package(self):
        include_dir = os.path.join(self.source_subfolder, "websocketpp")
        self.copy(pattern="*", dst="websocketpp", src=include_dir)

    def package_id(self):
        self.info.header_only()
