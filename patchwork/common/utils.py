from chardet.universaldetector import UniversalDetector


def open_with_chardet(file, mode="r", buffering=-1, errors=None, newline=None, closefd=True, opener=None):
    detector = UniversalDetector()
    with open(
        file=file, mode="rb", buffering=buffering, errors=errors, newline=newline, closefd=closefd, opener=opener
    ) as f:
        while True:
            line = f.read(1024)
            if not line:
                break
            detector.feed(line)
            if detector.done:
                break

    detector.close()

    encoding = detector.result.get("encoding", "utf-8")
    return open(
        file=file,
        mode=mode,
        buffering=buffering,
        encoding=encoding,
        errors=errors,
        newline=newline,
        closefd=closefd,
        opener=opener,
    )
