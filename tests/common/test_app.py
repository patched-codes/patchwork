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
LogAnalysis
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
LogAnalysis
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


def test_find_missing_patchflow_returns_none():
    patchflow = find_patchflow(["patchwork.patchflows"], "ThisPatchflowDoesNotExist")
    assert patchflow is None


def test_find_fails_on_broken_patchflow_file(tmp_path):
    flow_dir = tmp_path / "brokenflow"
    flow_dir.mkdir(parents=True, exist_ok=True)
    flow_file = flow_dir / "brokenflow.py"
    flow_file.write_text("import missing_transitive_dependency_xyz\nclass BrokenFlow:\n    pass\n")

    with pytest.raises(ModuleNotFoundError, match="missing_transitive_dependency_xyz"):
        find_patchflow([str(flow_file.resolve())], "BrokenFlow")


def test_find_fails_on_broken_transitive_dependency(mocker):
    def broken_import(name, *args, **kwargs):
        raise ModuleNotFoundError("No module named 'opentelemetry._events'", name="opentelemetry._events")

    mocker.patch("patchwork.app.importlib.import_module", side_effect=broken_import)

    with pytest.raises(ModuleNotFoundError, match="opentelemetry._events"):
        find_patchflow(["patchwork.patchflows"], "GenerateDocstring")


def test_cli_surfaces_broken_import(mocker, runner):
    def broken_import(name, *args, **kwargs):
        raise ModuleNotFoundError("No module named 'opentelemetry._events'", name="opentelemetry._events")

    mocker.patch("patchwork.app.importlib.import_module", side_effect=broken_import)

    result = runner.invoke(cli, ["GenerateDocstring"])
    assert result.exit_code == 1
    assert "opentelemetry._events" in result.output


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
