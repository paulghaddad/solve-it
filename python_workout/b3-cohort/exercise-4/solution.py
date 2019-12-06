import tarfile
from zipfile import ZipFile, ZIP_DEFLATED


def tar_to_zip(*tarfiles, zippath):
    zipfile = zippath.joinpath("output.zip")

    for archive in tarfiles:
        with ZipFile(zipfile, "w", compression=ZIP_DEFLATED) as zf:
            try:
                with tarfile.open(archive, "r") as tf:
                    for info in tf:
                        tf.extract(info, path="/tmp/")
                        zf.write(f"/tmp/{info.name}", arcname=info.name)
            except tarfile.ReadError as e:
                print(f"There was an error reading the file {archive}")
