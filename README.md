# Syft Documentation Guide

## Set up environment
Clone repository
```
git clone <repo_url>
```

Change directory
```
cd docs
```

Install dependencies
```
pip install -r requirements.txt

```

## For Linux/Mac
Change directory
```
cd ../docs
```
Make script executable

```bash
chmod +x serve_docs.py
```

Run the script:

```bash
./serve_docs.py
```

## For windows
Serve the Documentation:

Change directory
```
cd docs
```

Run the following command to build
```
jupyter-book build .
```

Serve the documentation
```
cd _build/html
python -m http.server
```

Remember to rebuild whenever a change is made to content
```
jupyter-book build .

```