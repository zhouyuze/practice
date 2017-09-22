set -xeu

ifconfig

docker run -it --name MySQL -p 127.0.0.1:3306:3306 \
				-e MYSQL_ROOT_PASSWORD=123456 \
				-d mysql:latest \
				--server-id=1 --log-bin=master --binlog_format=row

python connect.py