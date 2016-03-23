#!/usr/bin/python

import argparse
from ConfigParser import SafeConfigParser

import requests

from docker_registry_manager_operations import DockerRegistryManagerOperations


class DockerRegistryManager(object):
    CONST_SCRIPT_VERSION = '1.0.0'

    @staticmethod
    def main():
        """ Function that initializes the argument parser, so the user can give input data to the script using
        command line arguments"""
        if not DockerRegistryManager().check_configuration():
            return  # The script cannot start if the configuration file is incomplete.

        parser = argparse.ArgumentParser(
            description='Enables users to manage easier a Docker Registry, providing a simpler commands '
                        'syntax to launch each basic operation')
        sub_parsers = parser.add_subparsers()

        # create the parser for the "registry" command
        parser_registry = sub_parsers.add_parser('registry', help='Manage the instance of the Docker Registry')
        sub_sub_parsers_registry = parser_registry.add_subparsers()
        sub_parser_registry_status = sub_sub_parsers_registry.add_parser('status',
                                                                         help='Show information of the Docker '
                                                                              'Registry')
        sub_parser_registry_status.set_defaults(func=DockerRegistryManagerOperations().status_registry)
        sub_parser_registry_start = sub_sub_parsers_registry.add_parser('start',
                                                                        help='Run a new instance of the Docker '
                                                                             'Registry')
        sub_parser_registry_start.add_argument('--registry-id', dest='registry_id', required=True,
                                               help='ID of the registry container')
        sub_parser_registry_start.set_defaults(func=DockerRegistryManagerOperations().start_registry)
        sub_parser_registry_restart = sub_sub_parsers_registry.add_parser('restart',
                                                                          help='Restart the current instance '
                                                                               'of the Docker Registry')
        sub_parser_registry_restart.add_argument('--registry-id', dest='registry_id', required=True,
                                                 help='ID of the registry container')
        sub_parser_registry_restart.set_defaults(func=DockerRegistryManagerOperations().restart_registry)
        sub_parser_registry_stop = sub_sub_parsers_registry.add_parser('stop', help='Stop the current instance of '
                                                                                    'the Docker Registry')
        sub_parser_registry_stop.add_argument('--registry-id', dest='registry_id', required=True,
                                              help='ID of the registry container')
        sub_parser_registry_stop.set_defaults(func=DockerRegistryManagerOperations().stop_registry)

        # create the parser for the "accounts" command
        parser_accounts = sub_parsers.add_parser('accounts', help='Manage all accounts stored in the Docker Registry')

        # create the subparsers for the operations of "accounts" command
        sub_sub_parsers_accounts = parser_accounts.add_subparsers()
        sub_parser_accounts_list = sub_sub_parsers_accounts.add_parser('list',
                                                                       help='List all user accounts registered in '
                                                                            'the Docker Registry')
        sub_parser_accounts_list.set_defaults(func=DockerRegistryManagerOperations().list_accounts)
        sub_parser_account_add = sub_sub_parsers_accounts.add_parser('add', help='Create an user account')
        sub_parser_account_add.add_argument('--username', dest='username', required=True,
                                            help='Username for the new Docker Registry account')
        sub_parser_account_add.add_argument('--password', dest='password', required=True,
                                            help='Password for the new Docker Registry account')
        sub_parser_account_add.add_argument('--description', dest='description', required=False,
                                            help='A brief description for the new Docker Registry account')
        sub_parser_account_add.set_defaults(func=DockerRegistryManagerOperations().add_account)
        sub_parser_account_modify = sub_sub_parsers_accounts.add_parser('modify', help='Modify the password of an user '
                                                                                       'account')
        sub_parser_account_modify.add_argument('--username', dest='username', required=True,
                                               help='Username for the existing Docker Registry account')
        sub_parser_account_modify.add_argument('--new-password', dest='new_password', required=True,
                                               help='New password for the Docker Registry account')
        sub_parser_account_modify.set_defaults(func=DockerRegistryManagerOperations().modify_account)
        sub_parser_account_enable = sub_sub_parsers_accounts.add_parser('enable', help='Enable an user account')
        sub_parser_account_enable.add_argument('--username', dest='username', required=True,
                                               help='Username for the existing Docker Registry account')
        sub_parser_account_enable.set_defaults(func=DockerRegistryManagerOperations().enable_account)
        sub_parser_account_disable = sub_sub_parsers_accounts.add_parser('disable', help='Disable an user account')
        sub_parser_account_disable.add_argument('--username', dest='username', required=True,
                                                help='Username for the existing Docker Registry account')
        sub_parser_account_disable.set_defaults(func=DockerRegistryManagerOperations().disable_account)
        sub_parser_account_delete = sub_sub_parsers_accounts.add_parser('delete', help='Delete an user account')
        sub_parser_account_delete.add_argument('--username', dest='username', required=True,
                                               help='Username for the existing Docker Registry account')
        sub_parser_account_delete.set_defaults(func=DockerRegistryManagerOperations().delete_account)

        # create the parser for the "images" command
        parser_images = sub_parsers.add_parser('images', help='Manage all images stored in the Docker Registry')
        parser_images.set_defaults(func=DockerRegistryManagerOperations().list_images)

        # create the subparsers for the operations of "images" command
        sub_sub_parsers_images = parser_images.add_subparsers()
        sub_parser_images_list = sub_sub_parsers_images.add_parser('list', help='List all images stored in the Docker '
                                                                                'Registry')
        sub_parser_images_list.set_defaults(func=DockerRegistryManagerOperations().list_images)
        sub_parser_images_tags = sub_sub_parsers_images.add_parser('tags',
                                                                   help='Show all tags stored for an image in the '
                                                                        'Docker Registry')
        sub_parser_images_tags.add_argument('--remote-image', dest='remote_image', required=True,
                                            help='Image from the Docker Registry')
        sub_parser_images_tags.set_defaults(func=DockerRegistryManagerOperations().list_tags)
        sub_parser_images_digest = sub_sub_parsers_images.add_parser('digest',
                                                                     help='Get the digest of an image stored in the '
                                                                          'Docker Registry')
        sub_parser_images_digest.add_argument('--remote-image', dest='remote_image', required=True,
                                              help='Image from the Docker Registry')
        sub_parser_images_digest.add_argument('--tag', dest='tag', required=True, help='Tag for identifying the image '
                                                                                       'version')
        sub_parser_images_digest.set_defaults(func=DockerRegistryManagerOperations().get_digest)
        sub_parser_images_search = sub_sub_parsers_images.add_parser('search', help='Search a image in the  Docker '
                                                                                    'Registry')
        sub_parser_images_search.add_argument('--criteria', dest='criteria', required=True, help='Search criteria')
        sub_parser_images_search.set_defaults(func=DockerRegistryManagerOperations().search_image)
        sub_parser_images_delete = sub_sub_parsers_images.add_parser('delete', help='Remove an image reference in the '
                                                                                    'Docker Registry')
        sub_parser_images_delete.add_argument('--remote-image', dest='remote_image', required=True,
                                              help='Image to delete from the Registry')
        sub_parser_images_delete.add_argument('--tag', dest='tag', required=True, help='Tag for identifying the image '
                                                                                       'version')
        sub_parser_images_delete.set_defaults(func=DockerRegistryManagerOperations().delete_image)
        parser.add_argument('--version', action='version',
                            version='Docker Registry Manager Script version ' +
                                    DockerRegistryManager().CONST_SCRIPT_VERSION)
        args = parser.parse_args()
        args.func(args)

    @staticmethod
    def check_configuration():
        """ Checks if the settings written in 'docker_registry_manager.conf' are valid or not.
        :return: true if the settings are OK, otherwise returns false.
        """
        parser = SafeConfigParser()
        parser.read('docker_registry_manager.conf')
        registry_address = parser.get('docker_registry_manager', 'RegistryAddress')
        registry_protocol = parser.get('docker_registry_manager', 'RegistryProtocol')
        registry_port = parser.get('docker_registry_manager', 'RegistryPort')
        registry_username = parser.get('docker_registry_manager', 'RegistryUsername')
        registry_password = parser.get('docker_registry_manager', 'RegistryPassword')
        registry_email = parser.get('docker_registry_manager', 'RegistryEmail')
        certificate_path = parser.get('docker_registry_manager', 'CertificatePath')
        registry_users_file = parser.get('docker_registry_manager', 'RegistryUsersFile')
        ssh_address = parser.get('docker_registry_manager', 'SSHAddress')
        ssh_port = parser.get('docker_registry_manager', 'SSHPort')
        ssh_username = parser.get('docker_registry_manager', 'SSHUsername')
        ssh_password = parser.get('docker_registry_manager', 'SSHPassword')

        if not registry_address:
            print '[ERROR] RegistryAddress variable is empty in the configuration file. The script will not run until' \
                  ' you configure the script properly'
            return False
        if not registry_protocol:
            print '[ERROR] RegistryProtocol variable is empty in the configuration file. The script will not run until' \
                  ' you configure the script properly'
            return False
        if not registry_port:
            print '[ERROR] RegistryPort variable is empty in the configuration file. The script will not run until' \
                  ' you configure the script properly'
            return False
        if not registry_username:
            print '[ERROR] RegistryUsername variable is empty in the configuration file. The script will not run until' \
                  ' you configure the script properly'
            return False
        if not registry_password:
            print '[ERROR] RegistryPassword variable is empty in the configuration file. The script will not run until' \
                  ' you configure the script properly'
            return False
        if not registry_email:
            print '[ERROR] RegistryEmail variable is empty in the configuration file. The script will not run until' \
                  ' you configure the script properly'
            return False
        if not certificate_path:
            print '[ERROR] CertificatePath variable is empty in the configuration file. The script will not run until' \
                  ' you configure the script properly'
            return False
        if not registry_users_file:
            print '[ERROR] RegistryUsersFile variable is empty in the configuration file. The script will not run until' \
                  ' you configure the script properly'
            return False
        if not ssh_address:
            print '[ERROR] SSHAddress variable is empty in the configuration file. The script will not run until' \
                  ' you configure the script properly'
            return False
        if not ssh_port:
            print '[ERROR] SSHPort variable is empty in the configuration file. The script will not run until' \
                  ' you configure the script properly'
            return False
        if not ssh_username:
            print '[ERROR] SSHUsername variable is empty in the configuration file. The script will not run until' \
                  ' you configure the script properly'
            return False
        if not ssh_password:
            print '[ERROR] SSHPassword variable is empty in the configuration file. The script will not run until' \
                  ' you configure the script properly'
            return False

        return True


if __name__ == "__main__":
    requests.packages.urllib3.disable_warnings()
    DockerRegistryManager().main()
