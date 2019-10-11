import os
from conans import ConanFile, tools, CMake


class WebsocketPPConan(ConanFile):
    name = "websocketpp"
    topics = ("conan", "websocketpp", "websocket", "network", "web", "rfc6455")
    version = "0.8.1"
    url = "https://github.com/bincrafters/conan-websocketpp"
    homepage = "https://github.com/zaphoyd/websocketpp"
    description = "Header only C++ library that implements RFC6455 The WebSocket Protocol"
    license = "	BSD-3-Clause"
    author = "Bincrafters <bincrafters@gmail.com>"
    _source_subfolder = "source_subfolder"
    exports_sources = ["CMakeLists.txt"]
    generators = ["cmake"]
    settings = "os", "arch", "compiler", "build_type"
    options = {'asio': ['boost', 'standalone']}
    default_options = {'asio': 'boost'}

    def requirements(self):
        self.requires.add('openssl/1.1.1d')
        self.requires.add('zlib/1.2.11')
        if self.options.asio == 'standalone':
            self.requires.add('asio/1.12.0@bincrafters/stable')
        else:
            # 1.70 doesn't work: https://github.com/zaphoyd/websocketpp/issues/794
            self.requires.add('boost/1.69.0@conan/stable')

    def source(self):
        archive_name = "{0}-{1}".format(self.name, self.version)
        tools.get("{0}/archive/{1}.tar.gz".format(self.homepage, self.version),
                  sha256="178899de48c02853b55b1ea8681599641cedcdfce59e56beaff3dd0874bf0286")
        os.rename(archive_name, self._source_subfolder)

    def build(self):
        cmake = CMake(self)
        cmake.definitions['BUILD_TESTS'] = False
        cmake.definitions['BUILD_EXAMPLES'] = False
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        self.copy(pattern="COPYING", dst="license", src=self._source_subfolder)
        # We have to copy the headers manually, since the current install() step
        # in the 0.8.1 release doesn't work with the cmake wrapper.
        self.copy(pattern="*.hpp", dst="include/websocketpp", src=self._source_subfolder + '/websocketpp')

    def package_info(self):
        self.cpp_info.builddirs.append(os.path.join(self.package_folder, 'cmake'))
        if self.options.asio == 'standalone':
            self.cpp_info.defines.extend(['ASIO_STANDALONE', '_WEBSOCKETPP_CPP11_STL_'])

    def package_id(self):
        self.info.header_only()
