from fsspec.implementations.local import LocalFileSystem
from pangeo_forge_recipes.storage import MetadataTarget, CacheFSSpecTarget


def setup_logging():
    import logging
    import sys
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger("pangeo_forge_recipes")
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler(stream=sys.stdout)
    sh.setFormatter(formatter)
    logger.addHandler(sh)


def setup_targets(rec, name):
    
    fs_local = LocalFileSystem()

    rec.input_cache = CacheFSSpecTarget(fs_local, f"input_cache/{name.replace('/', '-')}")
    rec.metadata_cache = MetadataTarget(fs_local, f"metadata/{name.replace('/', '-')}")
    # rec.target = MetadataTarget(fs_local, f"zarr_build/{name.replace('/', '-')}.zarr")

    print(f"""Targets for recipe "{name}" set to:
    input_cache: {rec.input_cache.root_path}
    metadata_cache: {rec.metadata_cache.root_path}
    target: N/A, not needed for caching example
    """)

    return rec
