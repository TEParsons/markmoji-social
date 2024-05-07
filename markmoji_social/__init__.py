import importlib.metadata

# get version from pyproject.toml
try:
    __version__ = importlib.metadata.version("markmoji-social")
except importlib.metadata.PackageNotFoundError:
    # if running from local, use 0.dev
    __version__ = "0.dev"