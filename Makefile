.PHONY: make clean freshstart

clean:
	-find . -type f -a \( -name "*.pyc" -o -name "*$$py.class" \) | xargs rm
	-find . -type d -name "__pycache__" | xargs rm -r

make:
	if [ -d "~/venv" ];then	\
		rm -rf ~/venv;	\
	fi
		easy_install pip
		pip install virtualenv
		virtualenv venv
		test -d venv
		venv/bin/pip install -Ur requirements.txt
		touch venv/bin/activate

freshstart: clean	make