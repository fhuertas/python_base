PYTHON_VERSION=
PYTHON_ENV_TEST=env-test\$(PYTHON_VERSION)
all: clean env test package

env: env/bin/activate

env/bin/activate:
	bash sbin/env.sh

test:
	bash sbin/tests.sh \$(PYTHON_VERSION)

test-clean:
	rm -Rf env-*

clean:
	bash sbin/clean.sh

package: env
	bash sbin/package.sh

fat-zip: env
	bash sbin/fat-zip.sh

continuous-test:
	bash sbin/exec-continuous-test.sh
