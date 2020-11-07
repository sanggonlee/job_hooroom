. venv/bin/activate;
. env.sh;
datetime=$(date '+%Y%m%d%H%M%S')
# TODO: Make it cross environment
cd ~/projects/job_hooroom && /usr/local/opt/python/libexec/bin/python -m etl >~/projects/job_hooroom/cronlog/${datetime}.log 2>~/projects/job_hooroom/cronlog/${datetime}.err.log
