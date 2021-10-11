from nbconvert.exporters.script import ScriptExporter
from notebook.utils import to_api_path
import os
import re
import io

def script_post_save(model, os_path, contents_manager, **kwargs):
    # only process for notebooks
    if model["type"] != "notebook":
        return

    script_exporter = ScriptExporter(parent=contents_manager)
    base, __ = os.path.splitext(os_path)

    # do nothing if the notebook name ends with `Untitled[0-9]*`
    regex = re.compile(r"Untitled[0-9]*$")
    if regex.search(base):
        return

    script, resources = script_exporter.from_filename(os_path)
    script_fname = base + resources.get('output_extension', '.txt')

    log = contents_manager.log
    log.info("Saving script at /%s",
             to_api_path(script_fname, contents_manager.root_dir))

    script = script.split("# END #")[0]

    script = re.compile(r"^get_ipython\(\).*|^# In\[.*?\]:",re.MULTILINE).sub("",script)

    script = re.compile(r"^# *\/\*.*?[\r\n]# *\*\/",re.MULTILINE | re.DOTALL).sub("",script)

    script = re.compile(r"[\r\n][\r\n][\r\n]+",re.MULTILINE | re.DOTALL).sub("\n\n\n",script)

    with io.open(script_fname, "w", encoding="utf-8") as f:
        f.write(script)

c.FileContentsManager.post_save_hook = script_post_save
