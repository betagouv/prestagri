## Using Python 

### Create library 

```bash
mkdir import
uv init --lib my-project-catala
"from . import catala_runtime" > import/my-project-catala/src/my-project-catala/__init__.py 
```

add all generated files in `import/my-project-catala/src/my-project-catala`

### Import editable package in main python package



```bash
uv add --editable ./import/prestagri-catala/
```


```bash
uv add gmpy2
```

copy _build 