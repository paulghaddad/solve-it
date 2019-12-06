from zipfile import ZipFile


def tar_to_zip(tarpath, zippath):
    zipfile = zippath.joinpath("output.zip")

    with ZipFile(zipfile, "w") as zf:
        zf.write(tarpath)
