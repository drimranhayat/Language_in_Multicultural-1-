from pathlib import Path
import runpy
p=Path(__file__).resolve().parent
for name in ['upgrade_content.py','slide_audit.py','finalize_content.py','deepen_essays.py']:
 runpy.run_path(str(p/name),run_name='__main__')
