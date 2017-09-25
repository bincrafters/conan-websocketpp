from conans import ConanFile, tools, os

class WebsocketPPConan(ConanFile):
    name = "websocketpp"
    version = "0.7.0"
    url = "https://github.com/zaphoyd/websocketpp"
    description = "Header only C++ library that implements RFC6455 The WebSocket Protocol"
    license = "https://github.com/zaphoyd/websocketpp/blob/master/COPYING"
    requires =  "OpenSSL/1.0.2l@conan/stable", \
            "zlib/1.2.8@conan/stable", \
            "Boost.Random/1.64.0@bincrafters/stable", \
            "Boost.System/1.64.0@bincrafters/stable", \
            "Boost.Thread/1.64.0@bincrafters/stable", \
            "Boost.Asio/1.64.0@bincrafters/testing", \
                      
    def source(self):
        source_url = "https://github.com/zaphoyd/websocketpp"
        tools.get("{0}/{1}/archive/v{2}.tar.gz".format(source_url, self.name, self.version))

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()