# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

def test_cd(spack_command):
    """Sanity check the cd command to make sure it works."""

    cd = spack_command("cd")
    out = cd()

    assert "To set up shell support" in out
