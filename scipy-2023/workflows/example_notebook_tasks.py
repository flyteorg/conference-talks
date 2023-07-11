"""An example of how to use Jupyter Notebooks in your workflows."""

from pathlib import Path

from flytekit import workflow, kwtypes
from flytekit.types.structured import StructuredDataset
from flytekitplugins.papermill import NotebookTask


from workflows.example_intro import get_data


data_analysis_task = NotebookTask(
    name="workflows.data_analysis_task",
    notebook_path=str(
        Path(__file__).parent.parent.absolute()
        / "notebooks"
        / "data_analysis_task.ipynb"
    ),
    render_deck=True,
    disable_deck=False,
    inputs=kwtypes(structured_dataset=StructuredDataset),
    outputs=kwtypes(success=bool),
)

@workflow
def data_analysis_wf():
    data = get_data()
    data_analysis_task(structured_dataset=data)
