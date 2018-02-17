#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools, CMake


class WebsocketPPConan(ConanFile):
    name = "websocketpp"
    version = "0.7.0"
    url = "https://github.com/bincrafters/conan-websocketpp"
    description = "Header only C++ library that implements RFC6455 The WebSocket Protocol"
    license = "BSD 3-Clause"
    source_subfolder = "source_subfolder"
    exports_sources = ["CMakeLists.txt"]
    generators = ['cmake']
    settings = "os", "arch", "compiler", "build_type"

    def requirements(self):
        self.requires.add('OpenSSL/1.0.2l@conan/stable')
        self.requires.add('zlib/1.2.11@conan/stable')
        self.requires.add('boost_random/1.66.0@bincrafters/stable')
        self.requires.add('boost_system/1.66.0@bincrafters/stable')
        self.requires.add('boost_thread/1.66.0@bincrafters/stable')
        self.requires.add('boost_asio/1.66.0@bincrafters/stable')
                      
    def source(self):
        archive_name = "{0}-{1}".format(self.name, self.version)
        source_url = "https://github.com/zaphoyd/websocketpp"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.version))
        os.rename(archive_name, self.source_subfolder)

    def build(self):
        cmake = CMake(self)
        cmake.definitions['BUILD_TESTS'] = False
        cmake.definitions['BUILD_EXAMPLES'] = False
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        self.copy(pattern="COPYING", dst="license", src=self.source_subfolder)

    def package_info(self):
        self.cpp_info.builddirs.append(os.path.join(self.package_folder, 'cmake'))

    def package_id(self):
        self.info.header_only()
