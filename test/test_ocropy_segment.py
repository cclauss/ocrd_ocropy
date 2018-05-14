# pylint: disable=import-error

import os
import shutil

from test.base import TestCase, assets, main

from ocrd.resolver import Resolver
from ocrd_ocropy.segment import OcropySegment
PARAM_JSON = assets.url_of('param-segment.json')

WORKSPACE_DIR = '/tmp/ocrd-ocropy-segment-test'

class TestOcropySegment(TestCase):

    def setUp(self):
        if os.path.exists(WORKSPACE_DIR):
            shutil.rmtree(WORKSPACE_DIR)
        os.makedirs(WORKSPACE_DIR)

    def test_run1(self):
        resolver = Resolver(cache_enabled=True)
        workspace = resolver.workspace_from_url(assets.url_of('kant_aufklaerung_1784-binarized/mets.xml'), directory=WORKSPACE_DIR)
        proc = OcropySegment(
            workspace,
            input_file_grp="OCR-D-IMG-BIN",
            output_file_grp="OCR-D-SEG-LINE-OCROPY",
            parameter={'level-of-operation': 'line'}
        )
        proc.process()
        workspace.save_mets()

if __name__ == "__main__":
    main()