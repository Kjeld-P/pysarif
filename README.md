# PySarif

This package provides a simple way to load, save, and interact with SARIF files. 

The SARIF file, once loaded, can be interacted with like a normal Python object.

Nearly all of the code has been automatically generated from the [SARIF JSON Schema](https://github.com/oasis-tcs/sarif-spec/raw/main/Documents/CommitteeSpecifications/2.1.0/sarif-schema-2.1.0.json) using a modified version of Microsoft's [jschema-to-python](https://github.com/microsoft/jschema-to-python) package. The modified version can be found in [generator](./generator/). 

## Quickstart
`pip install pysarif`

```py
from pysarif import load_from_file, save_to_file

sarif = load_from_file("/path/to/sarif.sarif")
for rule in sarif.runs[0].tool.driver.rules:
    print(rule.name)

save_to_file(sarif, "/path/to/new/sarif.sarif")
```
## What about existing packages?
Microsoft offers the [sarif-om](https://github.com/microsoft/sarif-python-om) package. Sadly, they do not provide any way to load an existing SARIF file into their object model, nor do they provide a way to serialize the object model into a SARIF file. As such, I believe there is currently no (easy) way to work with SARIF files in Python, other than working with it as a dict.
