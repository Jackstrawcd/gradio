import sys
import unittest

import pytest

import gradio as gr


class TestDocumentation(unittest.TestCase):
    @pytest.mark.skipif(
        sys.version_info < (3, 8),
        reason="Docs use features in inspect module not available in py 3.7",
    )
    def test_documentation(self):
        documentation = gr.documentation.generate_documentation()
        assert len(documentation) > 0


if __name__ == "__main__":
    unittest.main()
