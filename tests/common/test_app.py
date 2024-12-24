import pytest
from click.testing import CliRunner

from patchwork.app import cli, find_patchflow


@pytest.fixture
def config_dir(tmp_path):
    config_dir = tmp_path / "config"
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir


@pytest.fixture
def patchflow_dir(config_dir):
    patchflow_dir = config_dir / "noop"
    patchflow_dir.mkdir(parents=True, exist_ok=True)
    return patchflow_dir


@pytest.fixture
def patchflow_file(patchflow_dir):
    patchflow_file = patchflow_dir / "noop.py"
    patchflow_file.touch(exist_ok=True)
    return patchflow_file


@pytest.fixture
def config_file(patchflow_dir):
    config_file = patchflow_dir / "config.yaml"
    config_file.touch(exist_ok=True)
    return config_file


@pytest.fixture
def runner():
    runner = CliRunner()
    with runner.isolated_filesystem():
        yield runner
    return


def test_default_list_option_callback(runner):
    result = runner.invoke(cli, ["--list"])
    assert result.exit_code == 0
    assert (
        result.output.strip()
        == """\
AutoFix
DependencyUpgrade
GenerateCodeUsageExample
GenerateDiagram
GenerateDocstring
GenerateREADME
GenerateUnitTests
PRReview
ResolveIssue
SonarFix"""
    )


def test_config_list_option_callback(runner, config_dir, patchflow_file):
    filename = patchflow_file.name
    name_without_ext = filename.replace(patchflow_file.suffix, "")
    result = runner.invoke(cli, ["--list", "--config", str(config_dir)])
    assert result.exit_code == 0
    assert (
        result.output.strip()
        == f"""\
AutoFix
DependencyUpgrade
GenerateCodeUsageExample
GenerateDiagram
GenerateDocstring
GenerateREADME
GenerateUnitTests
PRReview
ResolveIssue
SonarFix
{name_without_ext}"""
    )


def test_cli_success(runner, config_dir, patchflow_file):
    code = """\
class noop:
    def __init__(self, inputs):
        pass
    def run(self):
        return dict(test='test')
"""
    patchflow_file.write_text(code)

    result = runner.invoke(cli, ["noop", "--config", str(config_dir)])

    assert result.exit_code == 0


def test_cli_failure(runner):
    result = runner.invoke(cli, ["noop", "--config", "nonexistent"])
    assert result.exit_code == 2


def test_default_find_module():
    # Try to import the module
    patchflow = find_patchflow(["patchwork.patchflows"], "AutoFix")

    # Check the output
    assert isinstance(patchflow, type)
    assert patchflow.__name__ == "AutoFix"


def test_config_find_module(patchflow_file):
    code = """\
class noop:
    def __init__(self, inputs):
        pass
    def run(self):
        return dict(test='test')
"""
    patchflow_file.write_text(code)
    patchflow = find_patchflow([str(patchflow_file.resolve()), "patchwork.patchflows"], "noop")

    # Check the output
    assert isinstance(patchflow, type)
    assert patchflow.__name__ == "noop"
