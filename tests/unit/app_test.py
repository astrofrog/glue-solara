import solara
from glue.core import Data
from glue_jupyter.app import JupyterApplication

from glue_solara.app import GlueApp


def _create_app_with_viewers():
    app = JupyterApplication()
    data = Data(x=[1, 2, 3], y=[4, 5, 6], label='test')
    app.data_collection.append(data)
    app.scatter2d(data=data, show=False)
    app.histogram1d(data=data, show=False)
    return app


def test_glue_app_with_existing_viewers():
    app = _create_app_with_viewers()
    assert len(app.viewers) == 2

    @solara.component
    def TestComponent():
        GlueApp(app)

    box, rc = solara.render(TestComponent(), handle_error=False)
    box.close()


def test_glue_app_with_no_viewers():
    app = JupyterApplication()

    @solara.component
    def TestComponent():
        GlueApp(app)

    box, rc = solara.render(TestComponent(), handle_error=False)
    box.close()
