Just a small test to demonstrate why a synchronous-worker application container (like gunicorn) [should](http://gunicorn.org/design.html) be deployed behind an async reverse proxy (like nginx). The test facilitates sending concurrent HTTP requests against a "naked" gunicorn vs. one behind nginx.

Assuming you have nginx, foreman and virtualenv, try this out by:

    virtualenv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    foreman start -f Procfile.(naked | frontend)
    ./client.py --concurrent-requests (1 | 2 | 3 | 128)
