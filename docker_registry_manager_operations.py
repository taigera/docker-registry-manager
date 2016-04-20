import re
from ConfigParser import SafeConfigParser

import paramiko
import requests

import os
import sys

from requests.auth import HTTPBasicAuth


class DockerRegistryManagerOperations(object):
    @staticmethod
    def show_info(args):
        """Gets technical information about an image stored in the Docker Registry.
        :param args: the values passed by the user
        """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_manager.conf')
        parser.read(config_path)
        registry_address = parser.get('docker_registry_manager', 'RegistryProtocol') + parser.get(
            'docker_registry_manager',
            'RegistryAddress') + ':' + parser.get(
            'docker_registry_manager', 'RegistryPort')
        registry_username = parser.get('docker_registry_manager', 'RegistryUsername')
        registry_password = parser.get('docker_registry_manager', 'RegistryPassword')
        certificate_path = parser.get('docker_registry_manager', 'CertificatePath')
        request = requests.get(
            registry_address + '/v2/' + args.remote_image + '/manifests/' + args.tag,
            verify=certificate_path, auth=HTTPBasicAuth(registry_username, registry_password))
        print request.text

    @staticmethod
    def list_images(self):
        """Lists all images stored in the Docker Registry. """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_manager.conf')
        parser.read(config_path)
        registry_address = parser.get('docker_registry_manager', 'RegistryProtocol') + parser.get(
            'docker_registry_manager',
            'RegistryAddress') + ':' + parser.get(
            'docker_registry_manager', 'RegistryPort')
        registry_username = parser.get('docker_registry_manager', 'RegistryUsername')
        registry_password = parser.get('docker_registry_manager', 'RegistryPassword')
        certificate_path = parser.get('docker_registry_manager', 'CertificatePath')
        request = requests.get(registry_address + '/v2/_catalog/',
                               verify=certificate_path,
                               auth=HTTPBasicAuth(registry_username, registry_password))
        print request.text

    @staticmethod
    def list_tags(args):
        """Lists all tags stored in the Docker Registry.
        :param args: the values passed by the user
        """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_manager.conf')
        parser.read(config_path)
        registry_address = parser.get('docker_registry_manager', 'RegistryProtocol') + parser.get(
            'docker_registry_manager',
            'RegistryAddress') + ':' + parser.get(
            'docker_registry_manager', 'RegistryPort')
        registry_username = parser.get('docker_registry_manager', 'RegistryUsername')
        registry_password = parser.get('docker_registry_manager', 'RegistryPassword')
        certificate_path = parser.get('docker_registry_manager', 'CertificatePath')
        request = requests.get(registry_address + '/v2/' + args.remote_image + '/tags/list',
                               verify=certificate_path,
                               auth=HTTPBasicAuth(registry_username, registry_password))
        print request.text

    @staticmethod
    def search_image(args):
        """Tries to find an image stored in the Docker Registry using
        a search criteria.
        :param args: the values passed by the user
        """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_manager.conf')
        parser.read(config_path)
        registry_address = parser.get('docker_registry_manager', 'RegistryProtocol') + parser.get(
            'docker_registry_manager',
            'RegistryAddress') + ':' + parser.get(
            'docker_registry_manager', 'RegistryPort')
        registry_username = parser.get('docker_registry_manager', 'RegistryUsername')
        registry_password = parser.get('docker_registry_manager', 'RegistryPassword')
        certificate_path = parser.get('docker_registry_manager', 'CertificatePath')
        request = requests.get(registry_address + '/v2/_catalog',
                               verify=certificate_path,
                               auth=HTTPBasicAuth(registry_username, registry_password))
        images = request.json()['repositories']
        regex = re.compile('.*' + args.criteria + '.*')
        results = [m.group(0) for l in images for m in [regex.search(l)] if m]
        print 'Found images in the Docker Registry catalog:'
        print [result.encode('utf-8') for result in results]

    @staticmethod
    def get_digest(args):
        """Shows the digest of an image stored in the Docker Registry.
        :param args: the values passed by the user
        """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_manager.conf')
        parser.read(config_path)
        registry_address = parser.get('docker_registry_manager', 'RegistryProtocol') + parser.get(
            'docker_registry_manager',
            'RegistryAddress') + ':' + parser.get(
            'docker_registry_manager', 'RegistryPort')
        registry_username = parser.get('docker_registry_manager', 'RegistryUsername')
        registry_password = parser.get('docker_registry_manager', 'RegistryPassword')
        certificate_path = parser.get('docker_registry_manager', 'CertificatePath')
        request = requests.get(
            registry_address + '/v2/' + args.remote_image + '/manifests/' + args.tag,
            verify=certificate_path, auth=HTTPBasicAuth(registry_username, registry_password))
        if 'Docker-Content-Digest' in request.headers:
            print request.headers['Docker-Content-Digest']

    @staticmethod
    def delete_image(args):
        """Deletes an existing image from the Docker Registry.
        :param args: the values passed by the user
        """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_manager.conf')
        parser.read(config_path)
        registry_address = parser.get('docker_registry_manager', 'RegistryProtocol') + parser.get(
            'docker_registry_manager',
            'RegistryAddress') + ':' + parser.get(
            'docker_registry_manager', 'RegistryPort')
        registry_username = parser.get('docker_registry_manager', 'RegistryUsername')
        registry_password = parser.get('docker_registry_manager', 'RegistryPassword')
        certificate_path = parser.get('docker_registry_manager', 'CertificatePath')
        get_digest_request = requests.get(
            registry_address + '/v2/' + args.remote_image + '/manifests/' + args.tag,
            verify=certificate_path, auth=HTTPBasicAuth(registry_username, registry_password))
        if 'Docker-Content-Digest' in get_digest_request.headers:
            requests.delete(
                registry_address + '/v2/' + args.remote_image + '/manifests/' +
                get_digest_request.headers['Docker-Content-Digest'], verify=certificate_path,
                auth=HTTPBasicAuth(registry_username, registry_password))
            print 'Deleted image reference ' + registry_address + '/' + args.remote_image + ':' + args.tag + \
                  ' with digest ' + \
                  get_digest_request.headers['Docker-Content-Digest']
        else:
            print '[ERROR] Image or tag not found in the Docker Registry'

    @staticmethod
    def status_registry(args):
        """ Shows the status of the Registry
        :param args: the values passed by the user
        """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_manager.conf')
        parser.read(config_path)
        ssh_address = parser.get(
            'docker_registry_manager',
            'SSHAddress')
        ssh_port = parser.get('docker_registry_manager', 'SSHPort')
        ssh_username = parser.get('docker_registry_manager', 'SSHUsername')
        ssh_password = parser.get('docker_registry_manager', 'SSHPassword')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ssh_address, port=int(ssh_port), username=ssh_username, password=ssh_password)
        stdin, stdout, stderr = ssh.exec_command("docker ps -a")
        for line in stdout.read().splitlines():
            print line
        ssh.close()

    @staticmethod
    def start_registry(args):
        """ Starts the container of the Registry
        :param args: the values passed by the user
        """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_manager.conf')
        parser.read(config_path)
        ssh_address = parser.get(
            'docker_registry_manager',
            'SSHAddress')
        ssh_port = parser.get('docker_registry_manager', 'SSHPort')
        ssh_username = parser.get('docker_registry_manager', 'SSHUsername')
        ssh_password = parser.get('docker_registry_manager', 'SSHPassword')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ssh_address, port=int(ssh_port), username=ssh_username, password=ssh_password)
        stdin, stdout, stderr = ssh.exec_command("docker start " + args.registry_id)
        for line in stdout.read().splitlines():
            print line
        ssh.close()

    @staticmethod
    def restart_registry(args):
        """ Restarts the container of the Registry
        :param args: the values passed by the user
        """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_manager.conf')
        parser.read(config_path)
        ssh_address = parser.get(
            'docker_registry_manager',
            'SSHAddress')
        ssh_port = parser.get('docker_registry_manager', 'SSHPort')
        ssh_username = parser.get('docker_registry_manager', 'SSHUsername')
        ssh_password = parser.get('docker_registry_manager', 'SSHPassword')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ssh_address, port=int(ssh_port), username=ssh_username, password=ssh_password)
        stdin, stdout, stderr = ssh.exec_command("docker restart " + args.registry_id)
        for line in stdout.read().splitlines():
            print line
        ssh.close()

    @staticmethod
    def stop_registry(args):
        """ Stops the container of the Registry
        :param args: the values passed by the user
        """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_manager.conf')
        parser.read(config_path)
        ssh_address = parser.get(
            'docker_registry_manager',
            'SSHAddress')
        ssh_port = parser.get('docker_registry_manager', 'SSHPort')
        ssh_username = parser.get('docker_registry_manager', 'SSHUsername')
        ssh_password = parser.get('docker_registry_manager', 'SSHPassword')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ssh_address, port=int(ssh_port), username=ssh_username, password=ssh_password)
        stdin, stdout, stderr = ssh.exec_command("docker stop " + args.registry_id)
        for line in stdout.read().splitlines():
            print line
        ssh.close()

    @staticmethod
    def list_accounts(args):
        """ Lists all accounts stored in the Registry
        :param args: the values passed by the user
        """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_manager.conf')
        parser.read(config_path)
        ssh_address = parser.get(
            'docker_registry_manager',
            'SSHAddress')
        ssh_port = parser.get('docker_registry_manager', 'SSHPort')
        ssh_username = parser.get('docker_registry_manager', 'SSHUsername')
        ssh_password = parser.get('docker_registry_manager', 'SSHPassword')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ssh_address, port=int(ssh_port), username=ssh_username, password=ssh_password)
        stdin, stdout, stderr = ssh.exec_command("cat /docker-registry/nginx/registry.password")
        for line in stdout.read().splitlines():
            print line
        ssh.close()

    @staticmethod
    def add_account(args):
        """ Create an account that can be used in the Registry
        :param args: the values passed by the user
        """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_manager.conf')
        parser.read(config_path)
        ssh_address = parser.get(
            'docker_registry_manager',
            'SSHAddress')
        ssh_port = parser.get('docker_registry_manager', 'SSHPort')
        ssh_username = parser.get('docker_registry_manager', 'SSHUsername')
        ssh_password = parser.get('docker_registry_manager', 'SSHPassword')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ssh_address, port=int(ssh_port), username=ssh_username, password=ssh_password)
        ssh.exec_command("htpasswd -b /docker-registry/nginx/registry.password " + args.username + " " + args.password)
        stdin, stdout, stderr = ssh.exec_command("sed -i '/^" + args.username + ":/ s/$/ #'" + args.description + "'/' "
                                                                                                                  "/docker-registry/nginx/registry.password")

        for line in stdout.read().splitlines():
            print line
        ssh.close()

    @staticmethod
    def modify_account(args):
        """ Modify the password of an existing account in the Registry
        :param args: the values passed by the user
        """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_manager.conf')
        parser.read(config_path)
        ssh_address = parser.get(
            'docker_registry_manager',
            'SSHAddress')
        ssh_port = parser.get('docker_registry_manager', 'SSHPort')
        ssh_username = parser.get('docker_registry_manager', 'SSHUsername')
        ssh_password = parser.get('docker_registry_manager', 'SSHPassword')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ssh_address, port=int(ssh_port), username=ssh_username, password=ssh_password)
        stdin, stdout, stderr = ssh.exec_command("htpasswd -b /docker-registry/nginx/registry.password " +
                                                 args.username + " " + args.new_password)
        for line in stdout.read().splitlines():
            print line
        ssh.close()

    @staticmethod
    def enable_account(args):
        """ Allow account to be used as a login method to the Registry
        :param args: the values passed by the user
        """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_manager.conf')
        parser.read(config_path)
        ssh_address = parser.get(
            'docker_registry_manager',
            'SSHAddress')
        ssh_port = parser.get('docker_registry_manager', 'SSHPort')
        ssh_username = parser.get('docker_registry_manager', 'SSHUsername')
        ssh_password = parser.get('docker_registry_manager', 'SSHPassword')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ssh_address, port=int(ssh_port), username=ssh_username, password=ssh_password)
        stdin, stdout, stderr = ssh.exec_command("sed -i '/" + args.username +
                                                 "/s/^#//g' /docker-registry/nginx/registry.password")
        for line in stdout.read().splitlines():
            print line
        ssh.close()

    @staticmethod
    def disable_account(args):
        """ Disable account to be used as a login method to the Registry
        :param args: the values passed by the user
        """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_manager.conf')
        parser.read(config_path)
        ssh_address = parser.get(
            'docker_registry_manager',
            'SSHAddress')
        ssh_port = parser.get('docker_registry_manager', 'SSHPort')
        ssh_username = parser.get('docker_registry_manager', 'SSHUsername')
        ssh_password = parser.get('docker_registry_manager', 'SSHPassword')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ssh_address, port=int(ssh_port), username=ssh_username, password=ssh_password)
        stdin, stdout, stderr = ssh.exec_command("sed -i '/" + args.username +
                                                 "/s/^/#/g' /docker-registry/nginx/registry.password")
        for line in stdout.read().splitlines():
            print line
        ssh.close()

    @staticmethod
    def delete_account(args):
        """ Delete account stored in the Registry
        :param args: the values passed by the user
        """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_manager.conf')
        parser.read(config_path)
        ssh_address = parser.get(
            'docker_registry_manager',
            'SSHAddress')
        ssh_port = parser.get('docker_registry_manager', 'SSHPort')
        ssh_username = parser.get('docker_registry_manager', 'SSHUsername')
        ssh_password = parser.get('docker_registry_manager', 'SSHPassword')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ssh_address, port=int(ssh_port), username=ssh_username, password=ssh_password)
        stdin, stdout, stderr = ssh.exec_command("htpasswd -D /docker-registry/nginx/registry.password " +
                                                 args.username)
        for line in stdout.read().splitlines():
            print line
        ssh.close()
