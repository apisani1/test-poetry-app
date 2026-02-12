"""Basic tests for test-poetry-app."""


def test_import() -> None:
    """Test that the package can be imported."""
    import test_poetry_app
    assert hasattr(test_poetry_app, '__version__')


def test_version() -> None:
    """Test that version is defined."""
    from test_poetry_app import __version__
    assert __version__ is not None
    assert isinstance(__version__, str)
