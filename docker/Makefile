#make-docker helper

build:
	docker-compose -f docker-compose.yml build --parallel
up:
	docker-compose -f docker-compose.yml up -d $(c)
ssh:
	docker exec -it blog /bin/bash
server:
	docker exec -it blog "python /var/www/be/manage.py runserver"
down:
	docker-compose -f docker-compose.yml down
flake8:
	docker exec -it blog "flake8 /var/www/be"
test:
	docker exec -it blog "python /var/www/be/blog_app/tests.py"