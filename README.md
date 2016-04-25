# docker-registry-manager
Command-line tool for managing a Docker Registry

## Introduction
The docker-registry-manager is a multi-platform command line tool made with Python that abstracts the complexity of administrating a Docker Registry. You will not have to connect directly or access physically to the server to create new accounts, modify the existing ones or print the Registry status, for example. With this tool, these tasks will be easier to perform.

## Dependencies
You need to satisfy the following dependencies in order to compile and run the project 

* Python 2.7 with [pip](https://pip.pypa.io/en/stable/) tool installed.
* Python modules installed: [requests](http://docs.python-requests.org/en/master/) and [paramiko](http://www.paramiko.org)  
* [PyInstaller](http://www.pyinstaller.org) 3.1.1 or greater
* A server where the Docker Registry is stored. The server must use a GNU/Linux distro installed and with a SSH daemon up and working. 

## Install
Follow these instructions to compile and install docker-registry-tool.

1. Clone this repository.
2. Check that you have satisfied all dependencies by executing the command `python docker_registry_manager.py` . If the previous command does not return any error, then proceed to the next step.
3. Install PyInstaller as explained [here](http://pythonhosted.org/PyInstaller/)
4. Use PyInstaller to get a binary from the source files. `pyinstaller --onefile docker_registry_manager.py`
5. You will get the binary file in the dist folder. 

## Configuration
The script configuration is made in the `docker_registry_manager.conf` file. You can open and modify it with a plain text editor. This file must be in the same path where the Docker Registry Manager is stored. 

## Run
### Manipulate the Docker Registry itself
#### Print the Docker Registry status
If you want to know the Docker Registry status, then you must type `docker_registry_manager registry status`.
#### Start the Docker Registry
If you want to start the Docker Registry, then you must type `docker_registry_manager registry start --registry-id {CONTAINER ID}`. Replace `{CONTAINER ID}` with the proper container ID that is storing the Registry. For example, `docker_registry_manager registry start --registry-id e3d12b9720b3` 
#### Restart the Docker Registry
If you want to restart the Docker Registry, then you must type `docker_registry_manager registry restart --registry-id {CONTAINER ID}`. Replace `{CONTAINER ID}` with the proper container ID that is storing the Registry. For example, `docker_registry_manager registry restart --registry-id e3d12b9720b3` 
#### Stop the Docker Registry
If you want to stop the Docker Registry, then you must type `docker_registry_manager registry stop --registry-id {CONTAINER ID}`. Replace `{CONTAINER ID}` with the proper container ID that is storing the Registry. For example, `docker_registry_manager registry stop --registry-id e3d12b9720b3` 

### Manipulate accounts
#### List accounts
If you want to get all registered accounts in the Registry, then you must type `docker_registry_manager accounts list`.
#### Create accounts
If you want to create a new account, then you must type `docker_registry_manager accounts add --username {USERNAME} --password {PASSWORD} --description {DESCRIPTION}`. Replace `{USERNAME}`,`{PASSWORD}`,`{DESCRIPTION}` with the username, password and a brief description of the new account.
#### Modify the password of an account
If you want to modify the password of an existing account, then you must type `docker_registry_manager accounts modify --username {USERNAME} --new-password {PASSWORD}`. Replace `{USERNAME}` with the username of the account and `{PASSWORD}` with the new password of the account.
#### Delete accounts
If you want to delete an existing account, then you must type `docker_registry_manager accounts delete --username {USERNAME}`. Replace `{USERNAME}` with the username of the account that you want to delete.
#### Disable accounts
If you want to disable an existing account without deleting it, then you must type `docker_registry_manager accounts disable --username {USERNAME}`. Replace `{USERNAME}` with the username of the account that you want to disable.
#### Enable accounts
If you want to enable an existing account, then you must type `docker_registry_manager accounts enable --username {USERNAME}`. Replace `{USERNAME}` with the username of the account that you want to enable.

### Manipulate images
### List all images stored in the Docker Registry
If you want to get all images stored in the server, then you must type `docker_registry_manager images list`.
### List all tags stored in the Docker Registry
If you want to get all tags of an image, then you must type `docker_registry_manager images tags --remote-image {IMAGE TO CHECK}`. Replace `{IMAGE TO CHECK}` with the proper image name. For example, `docker_registry_tool tags --remote-image ubuntu`
#### Search for an image stored in the Docker Registry
Issue the following command to search for an image: `docker_registry_manager images search --criteria {SEARCH CRITERIA}`. Replace `{SEARCH CRITERIA}` with the proper search criteria. The command will return a list with the names of the images that satisfy the search condition. For example, `docker_registry_manager images search --criteria ub` will retrieve all names that contains "ub".
#### Deleting an image stored with the Docker Registry Tool
Issue the following command to delete an image: `docker_registry_manager images delete --remote-image {IMAGE NAME} --tag {TAG}`. Replace `{IMAGE TO CHECK}` and `{TAG}` with the proper image name and tag. For example, `docker_registry_manager images delete --remote-image ubuntu --tag old`

## Users
 * The company [Taiger](http://www.taiger.com) uses this tool in their development processes and infrastructures.

## Greetings
Performed as part of the LPS-BIGGER project, funded by the [Centre for the Development of Industrial Technology (CDTI)](http://www.cienlpsbigger.es)
![CDTI](http://www.cienlpsbigger.es/images/cdti.png)

## Reporting issues
Issues can be reported via the [Github issue tracker](https://github.com/taigers/docker-registry-manager/issues).

Please take the time to review existing issues before submitting your own to prevent duplicates. Incorrect or poorly formed reports are wasteful and are subject to deletion.

## Submitting fixes and improvements
Fixes and improvements are submitted as pull requests via Github. 

## Related projects
 * [docker-registry-garbage-collector](https://github.com/taigers/docker-registry-garbage-collector)
 * [docker-registry-tool](https://github.com/taigers/docker-registry-tool)
