#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/stable")

class BoostDetailConan(base.BoostBaseConan):
    name = "boost_detail"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_detail"
    lib_short_names = ["detail"]
    header_only_libs = ["detail"]
    b2_requires = [
        "boost_config",
        "boost_core",
        "boost_mpl",
        "boost_preprocessor",
        "boost_static_assert",
        "boost_type_traits"
    ]
