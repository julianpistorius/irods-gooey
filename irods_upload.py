import os

from gooey import Gooey, GooeyParser
from irods.session import iRODSSession


@Gooey(dump_build_config=False, program_name="IRODS Uploader")
def main():
    desc = "Upload a file to IRODS Data Store"
    file_help_msg = "Name of the file you want to process"

    my_cool_parser = GooeyParser(description=desc)

    my_cool_parser.add_argument("UserName", type=str,
                                help='Your CyVerse username')
    my_cool_parser.add_argument(
        "FileChooser", help=file_help_msg, widget="FileChooser")

    args = my_cool_parser.parse_args()

    # Do stuff with parsed parameters
    full_local_path = args.FileChooser
    just_file_name = args.FileChooser.split('/')[-1:][0]
    username = args.UserName

    upload_file(username=username,
                local_path=full_local_path,
                remote_name=just_file_name)


def upload_file(username, local_path, remote_name):
    print(
        f'Uploading "{local_path}" to "/iplant/home/{username}/{remote_name}"')
    try:
        env_file = os.environ['IRODS_ENVIRONMENT_FILE']
    except KeyError:
        env_file = os.path.expanduser('~/.irods/irods_environment.json')

    with iRODSSession(irods_env_file=env_file) as session:
        remote_path = f'/iplant/home/{username}/{remote_name}'
        session.data_objects.put(local_path, remote_path)
        placed_object = session.data_objects.get(remote_path)
        print(f'placed_object.id: {placed_object.id}')


if __name__ == '__main__':
    main()
