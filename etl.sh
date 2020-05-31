. venv/bin/activate;
. env.sh;
datetime=$(date '+%Y%m%d%H%M%S')
# TODO: Make it cross environment
cd ~/prjs/job_hooroom && /usr/local/opt/python/libexec/bin/python -m etl >~/prjs/job_hooroom/cronlog/log/${datetime}.log 2>~/prjs/job_hooroom/cronlog/err/${datetime}.log
