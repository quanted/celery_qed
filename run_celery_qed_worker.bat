start celery -A tasks worker -Q sam --loglevel=info --concurrency=1 -n sam_worker