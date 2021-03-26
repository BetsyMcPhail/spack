import pytest

from spack.main import SpackCommand

@pytest.fixture()
def spack_command(capsys):
    def _impl(name):
        return SpackCommand(name, capsys)
    return _impl
