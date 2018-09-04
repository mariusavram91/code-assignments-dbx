import dropbox
import logging
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError
from dbx import settings


class Dropbox(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.token = settings.DROPBOX_TOKEN
        self.dbx = dropbox.Dropbox(self.token)

    def upload_file(self, file, name):
        path = settings.DROPBOX_PATH
        file_name = name + '_' + file.name

        try:
            self.dbx.users_get_current_account()
        except AuthError as error:
            self.logger.error(error)

            return False

        dropbox_file_path = None
        try:
            response = self.dbx.files_upload(
                file.read(),
                path + file_name,
                mode=WriteMode('add')
            )
            dropbox_file_path = response.path_lower
        except ApiError as error:
            self.logger.error(error)

            return False

        return dropbox_file_path

    def get_file_link(self, file_path):
        link = None
        if file_path:
            self.dbx = dropbox.Dropbox(self.token)

            try:
                self.dbx.users_get_current_account()
            except AuthError as error:
                self.logger.error(error)

                return False

            try:
                response = self.dbx.sharing_create_shared_link(
                    file_path
                )
                link = response.url
            except ApiError as error:
                self.logger.error(error)

                return False

        return link
