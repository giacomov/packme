#!/bin/bash

# A script that detects the user that owns the /workspace directory and becomes that user.
# This is used within Docker so that the coverage files as well as the documentations are
# readable by the current user

USER_NAME="deployer"

files=(/workspace/*) && DIR=${files[-1]}
USER_ID=$(stat -c "%u" ${DIR})

echo "Using ${USER_ID} from owner of dir ${DIR}"

id "${USER_NAME?}" >/dev/null 2>&1

if [[ $? -ne 0 ]]; then
	echo Creating user ${USER_NAME} with UID ${USER_ID}
	useradd --uid ${USER_ID} --shell /bin/bash -d /deployer ${USER_NAME}
fi

mkdir -p /deployer
chown deployer:deployer /deployer

sudo -u deployer /bin/bash /workspace/ci/setup_env.sh
sudo -u deployer /bin/bash -c "source /deployer/{{ package_name}}_testing/bin/activate && /bin/bash /workspace/ci/run_tests.sh"
sudo -u deployer /bin/bash -c "source /deployer/{{ package_name}}_testing/bin/activate && /bin/bash /workspace/ci/make_docs.sh"
