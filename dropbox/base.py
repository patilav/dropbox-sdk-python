# Auto-generated by BabelAPI, do not modify.

from abc import ABCMeta, abstractmethod

from . import babel_validators as bv

from . import (
    files,
    sharing,
    users,
)

class DropboxBase(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def request(self):
        pass

    # ------------------------------------------
    # Routes in files namespace

    def files_get_metadata(self,
                           path):
        """
        Returns the metadata for a file or folder.

        :param str path: The path or ID of a file or folder on Dropbox
        :rtype: :class:`dropbox.files.Metadata`
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.files.GetMetadataError`
        """
        o = files.GetMetadataArg(path)
        r = self.request(self.HOST_API,
                         'files/get_metadata',
                         self.ROUTE_STYLE_RPC,
                         bv.Struct(files.GetMetadataArg),
                         bv.StructTree(files.Metadata),
                         bv.Union(files.GetMetadataError),
                         o,
                         None)
        return r

    def files_list_folder(self,
                          path,
                          recursive=False):
        """
        Returns the contents of a folder. NOTE: We're definitely going to
        streamline this interface.

        :param str path: The path to the folder you want to see the contents of.
        :param bool recursive: If true, list folder operation will be applied
            recursively to all subfolders. And the response will contain
            contents of all subfolders
        :rtype: :class:`dropbox.files.ListFolderResult`
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.files.ListFolderError`
        """
        o = files.ListFolderArg(path,
                                recursive)
        r = self.request(self.HOST_API,
                         'files/list_folder',
                         self.ROUTE_STYLE_RPC,
                         bv.Struct(files.ListFolderArg),
                         bv.Struct(files.ListFolderResult),
                         bv.Union(files.ListFolderError),
                         o,
                         None)
        return r

    def files_list_folder_continue(self,
                                   cursor):
        """
        Once a cursor has been retrieved from :meth:`list_folder`, use this to
        paginate through all files and retrieve updates to the folder. NOTE:
        We're definitely going to streamline this interface.

        :param str cursor: The cursor returned by :meth:`list_folder` or
            :meth:`list_folder_continue`.
        :rtype: :class:`dropbox.files.ListFolderResult`
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.files.ListFolderContinueError`
        """
        o = files.ListFolderContinueArg(cursor)
        r = self.request(self.HOST_API,
                         'files/list_folder/continue',
                         self.ROUTE_STYLE_RPC,
                         bv.Struct(files.ListFolderContinueArg),
                         bv.Struct(files.ListFolderResult),
                         bv.Union(files.ListFolderContinueError),
                         o,
                         None)
        return r

    def files_list_folder_get_latest_cursor(self,
                                            path,
                                            recursive=False):
        """
        A way to quickly get a cursor for the folder's state. Unlike
        :meth:`list_folder`, :meth:`list_folder_get_latest_cursor` doesn't
        return any entries. This endpoint is for app which only needs to know
        about new files and modifications and doesn't need to know about files
        that already exist in Dropbox.

        :param str path: The path to the folder you want to see the contents of.
        :param bool recursive: If true, list folder operation will be applied
            recursively to all subfolders. And the response will contain
            contents of all subfolders
        :rtype: :class:`dropbox.files.ListFolderGetLatestCursorResult`
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.files.ListFolderError`
        """
        o = files.ListFolderArg(path,
                                recursive)
        r = self.request(self.HOST_API,
                         'files/list_folder/get_latest_cursor',
                         self.ROUTE_STYLE_RPC,
                         bv.Struct(files.ListFolderArg),
                         bv.Struct(files.ListFolderGetLatestCursorResult),
                         bv.Union(files.ListFolderError),
                         o,
                         None)
        return r

    def files_download(self,
                       path,
                       rev=None):
        """
        Download a file from a user's Dropbox.

        :param str path: The path of the file to download.
        :param Nullable rev: Optional revision, taken from the corresponding
            :class:`Metadata` field.
        :rtype: (:class:`dropbox.files.FileMetadata`,
                 :class:`requests.models.Response`)
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.files.DownloadError`

        You must call close on the Response object when you are done with it,
        otherwise you will max out your available connections.
        """
        o = files.DownloadArg(path,
                              rev)
        r = self.request(self.HOST_CONTENT,
                         'files/download',
                         self.ROUTE_STYLE_DOWNLOAD,
                         bv.Struct(files.DownloadArg),
                         bv.Struct(files.FileMetadata),
                         bv.Union(files.DownloadError),
                         o,
                         None)
        return r

    def files_download_to_file(self,
                               download_path,
                               path,
                               rev=None):
        """
        Download a file from a user's Dropbox.

        :param str download_path: Path on local machine to save file.
        :param str path: The path of the file to download.
        :param Nullable rev: Optional revision, taken from the corresponding
            :class:`Metadata` field.
        :rtype: (:class:`dropbox.files.FileMetadata`,
                 :class:`requests.models.Response`)
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.files.DownloadError`
        """
        o = files.DownloadArg(path,
                              rev)
        r = self.request(self.HOST_CONTENT,
                         'files/download',
                         self.ROUTE_STYLE_DOWNLOAD,
                         bv.Struct(files.DownloadArg),
                         bv.Struct(files.FileMetadata),
                         bv.Union(files.DownloadError),
                         o,
                         None)
        self._save_body_to_file(download_path, r[1])
        return r[0]

    def files_upload_session_start(self,
                                   f):
        """
        Start a new upload session. This is used to upload a single file with
        multiple calls.

        :param f: A string or file-like obj of data.
        :rtype: :class:`dropbox.files.UploadSessionStartResult`
        """
        o = None
        r = self.request(self.HOST_CONTENT,
                         'files/upload_session/start',
                         self.ROUTE_STYLE_UPLOAD,
                         bv.Void(),
                         bv.Struct(files.UploadSessionStartResult),
                         bv.Void(),
                         o,
                         f)
        return r

    def files_upload_session_append(self,
                                    f,
                                    session_id,
                                    offset):
        """
        Append more data to an upload session.

        :param f: A string or file-like obj of data.
        :param str session_id: The upload session ID (returned by
            :meth:`upload_session_start`).
        :param long offset: The amount of data that has been uploaded so far. We
            use this to make sure upload data isn't lost or duplicated in the
            event of a network error.
        :rtype: None
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.files.UploadSessionLookupError`
        """
        o = files.UploadSessionCursor(session_id,
                                      offset)
        r = self.request(self.HOST_CONTENT,
                         'files/upload_session/append',
                         self.ROUTE_STYLE_UPLOAD,
                         bv.Struct(files.UploadSessionCursor),
                         bv.Void(),
                         bv.Union(files.UploadSessionLookupError),
                         o,
                         f)
        return None

    def files_upload_session_finish(self,
                                    f,
                                    cursor,
                                    commit):
        """
        Finish an upload session and save the uploaded data to the given file
        path.

        :param f: A string or file-like obj of data.
        :param cursor: Contains the upload session ID and the offset.
        :type cursor: :class:`dropbox.files.UploadSessionCursor`
        :param commit: Contains the path and other optional modifiers for the
            commit.
        :type commit: :class:`dropbox.files.CommitInfo`
        :rtype: :class:`dropbox.files.FileMetadata`
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.files.UploadSessionFinishError`
        """
        o = files.UploadSessionFinishArg(cursor,
                                         commit)
        r = self.request(self.HOST_CONTENT,
                         'files/upload_session/finish',
                         self.ROUTE_STYLE_UPLOAD,
                         bv.Struct(files.UploadSessionFinishArg),
                         bv.Struct(files.FileMetadata),
                         bv.Union(files.UploadSessionFinishError),
                         o,
                         f)
        return r

    def files_upload(self,
                     f,
                     path,
                     mode=files.WriteMode.add,
                     autorename=False,
                     client_modified=None,
                     mute=False):
        """
        Create a new file with the contents provided in the request.

        :param f: A string or file-like obj of data.
        :param str path: Path in the user's Dropbox to save the file.
        :param mode: Selects what to do if the file already exists.
        :type mode: :class:`dropbox.files.WriteMode`
        :param bool autorename: If there's a conflict, as determined by
            ``mode``, have the Dropbox server try to autorename the file to
            avoid conflict.
        :param Nullable client_modified: The value to store as the
            ``client_modified`` timestamp. Dropbox automatically records the
            time at which the file was written to the Dropbox servers. It can
            also record an additional timestamp, provided by Dropbox desktop
            clients, mobile clients, and API apps of when the file was actually
            created or modified.
        :param bool mute: Normally, users are made aware of any file
            modifications in their Dropbox account via notifications in the
            client software. If u'true', this tells the clients that this
            modification shouldn't result in a user notification.
        :rtype: :class:`dropbox.files.FileMetadata`
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.files.UploadError`
        """
        o = files.CommitInfo(path,
                             mode,
                             autorename,
                             client_modified,
                             mute)
        r = self.request(self.HOST_CONTENT,
                         'files/upload',
                         self.ROUTE_STYLE_UPLOAD,
                         bv.Struct(files.CommitInfo),
                         bv.Struct(files.FileMetadata),
                         bv.Union(files.UploadError),
                         o,
                         f)
        return r

    def files_search(self,
                     path,
                     query,
                     start=0,
                     max_results=100,
                     mode=files.SearchMode.filename):
        """
        Searches for files and folders.

        :param str path: The path in the user's Dropbox to search. Should
            probably be a folder.
        :param str query: The string to search for. The search string is split
            on spaces into multiple tokens. For file name searching, the last
            token is used for prefix matching (i.e. "bat c" matches "bat cave"
            but not "batman car").
        :param long start: The starting index within the search results (used
            for paging).
        :param long max_results: The maximum number of search results to return.
        :param mode: The search mode (filename, filename_and_content, or
            deleted_filename).
        :type mode: :class:`dropbox.files.SearchMode`
        :rtype: :class:`dropbox.files.SearchResults`
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.files.SearchError`
        """
        o = files.SearchQuery(path,
                              query,
                              start,
                              max_results,
                              mode)
        r = self.request(self.HOST_API,
                         'files/search',
                         self.ROUTE_STYLE_RPC,
                         bv.Struct(files.SearchQuery),
                         bv.Struct(files.SearchResults),
                         bv.Union(files.SearchError),
                         o,
                         None)
        return r

    def files_create_folder(self,
                            path):
        """
        Create a folder at a given path. No file or folder may exist at the
        path. The parent folder will be created if it does not already exist
        (and so on). If the parent exists it must be a folder (and the same for
        any ancestor). If an ancestor is a shared folder it must have write
        access.

        :param str path: Path in the user's Dropbox to create.
        :rtype: :class:`dropbox.files.FolderMetadata`
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.files.CreateFolderError`
        """
        o = files.CreateFolderArg(path)
        r = self.request(self.HOST_API,
                         'files/create_folder',
                         self.ROUTE_STYLE_RPC,
                         bv.Struct(files.CreateFolderArg),
                         bv.Struct(files.FolderMetadata),
                         bv.Union(files.CreateFolderError),
                         o,
                         None)
        return r

    def files_delete(self,
                     path):
        """
        Delete the file or folder at a given path. If the path is a folder all
        its contents will be deleted too.

        :param str path: Path in the user's Dropbox to delete.
        :rtype: :class:`dropbox.files.Metadata`
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.files.DeleteError`
        """
        o = files.DeleteArg(path)
        r = self.request(self.HOST_API,
                         'files/delete',
                         self.ROUTE_STYLE_RPC,
                         bv.Struct(files.DeleteArg),
                         bv.StructTree(files.Metadata),
                         bv.Union(files.DeleteError),
                         o,
                         None)
        return r

    def files_copy(self,
                   from_path,
                   to_path):
        """
        Copy a file or folder to a different destination in the user's Dropbox.
        If the source path is a folder all its contents will be copied. The
        destination path must not yet exist.

        :param str from_path: Path in the user's Dropbox to be copied or moved.
        :param str to_path: Path in the user's Dropbox that is the destination.
        :rtype: :class:`dropbox.files.Metadata`
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.files.RelocationError`
        """
        o = files.RelocationArg(from_path,
                                to_path)
        r = self.request(self.HOST_API,
                         'files/copy',
                         self.ROUTE_STYLE_RPC,
                         bv.Struct(files.RelocationArg),
                         bv.StructTree(files.Metadata),
                         bv.Union(files.RelocationError),
                         o,
                         None)
        return r

    def files_move(self,
                   from_path,
                   to_path):
        """
        Move a file or folder to a different destination in the user's Dropbox.
        If the source path is a folder all its contents will be moved. The
        destination path must not yet exist.

        :param str from_path: Path in the user's Dropbox to be copied or moved.
        :param str to_path: Path in the user's Dropbox that is the destination.
        :rtype: :class:`dropbox.files.Metadata`
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.files.RelocationError`
        """
        o = files.RelocationArg(from_path,
                                to_path)
        r = self.request(self.HOST_API,
                         'files/move',
                         self.ROUTE_STYLE_RPC,
                         bv.Struct(files.RelocationArg),
                         bv.StructTree(files.Metadata),
                         bv.Union(files.RelocationError),
                         o,
                         None)
        return r

    def files_get_thumbnail(self,
                            path,
                            format=files.ThumbnailFormat.jpeg,
                            size=files.ThumbnailSize.s):
        """
        Get a thumbnail for an image.

        :param str path: The path to the image file you want to thumbnail.
        :param format: The format for the thumbnail image, jpeg (default) or
            png. For  images that are photos, jpeg should be preferred, while
            png is  better for screenshots and digital arts.
        :type format: :class:`dropbox.files.ThumbnailFormat`
        :param size: The size for the thumbnail image (default s).
        :type size: :class:`dropbox.files.ThumbnailSize`
        :rtype: (:class:`dropbox.files.FileMetadata`,
                 :class:`requests.models.Response`)
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.files.ThumbnailError`

        You must call close on the Response object when you are done with it,
        otherwise you will max out your available connections.
        """
        o = files.ThumbnailArg(path,
                               format,
                               size)
        r = self.request(self.HOST_CONTENT,
                         'files/get_thumbnail',
                         self.ROUTE_STYLE_DOWNLOAD,
                         bv.Struct(files.ThumbnailArg),
                         bv.Struct(files.FileMetadata),
                         bv.Union(files.ThumbnailError),
                         o,
                         None)
        return r

    def files_get_thumbnail_to_file(self,
                                    download_path,
                                    path,
                                    format=files.ThumbnailFormat.jpeg,
                                    size=files.ThumbnailSize.s):
        """
        Get a thumbnail for an image.

        :param str download_path: Path on local machine to save file.
        :param str path: The path to the image file you want to thumbnail.
        :param format: The format for the thumbnail image, jpeg (default) or
            png. For  images that are photos, jpeg should be preferred, while
            png is  better for screenshots and digital arts.
        :type format: :class:`dropbox.files.ThumbnailFormat`
        :param size: The size for the thumbnail image (default s).
        :type size: :class:`dropbox.files.ThumbnailSize`
        :rtype: (:class:`dropbox.files.FileMetadata`,
                 :class:`requests.models.Response`)
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.files.ThumbnailError`
        """
        o = files.ThumbnailArg(path,
                               format,
                               size)
        r = self.request(self.HOST_CONTENT,
                         'files/get_thumbnail',
                         self.ROUTE_STYLE_DOWNLOAD,
                         bv.Struct(files.ThumbnailArg),
                         bv.Struct(files.FileMetadata),
                         bv.Union(files.ThumbnailError),
                         o,
                         None)
        self._save_body_to_file(download_path, r[1])
        return r[0]

    def files_get_preview(self,
                          path,
                          rev=None):
        """
        Get a preview for a file. Currently previews are only generated for the
        files with  the following extensions: .doc, .docx, .docm, .ppt, .pps,
        .ppsx, .ppsm, .pptx, .pptm,  .xls, .xlsx, .xlsm, .rtf

        :param str path: The path of the file to preview.
        :param Nullable rev: Optional revision, taken from the corresponding
            :class:`Metadata` field.
        :rtype: (:class:`dropbox.files.FileMetadata`,
                 :class:`requests.models.Response`)
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.files.PreviewError`

        You must call close on the Response object when you are done with it,
        otherwise you will max out your available connections.
        """
        o = files.PreviewArg(path,
                             rev)
        r = self.request(self.HOST_CONTENT,
                         'files/get_preview',
                         self.ROUTE_STYLE_DOWNLOAD,
                         bv.Struct(files.PreviewArg),
                         bv.Struct(files.FileMetadata),
                         bv.Union(files.PreviewError),
                         o,
                         None)
        return r

    def files_get_preview_to_file(self,
                                  download_path,
                                  path,
                                  rev=None):
        """
        Get a preview for a file. Currently previews are only generated for the
        files with  the following extensions: .doc, .docx, .docm, .ppt, .pps,
        .ppsx, .ppsm, .pptx, .pptm,  .xls, .xlsx, .xlsm, .rtf

        :param str download_path: Path on local machine to save file.
        :param str path: The path of the file to preview.
        :param Nullable rev: Optional revision, taken from the corresponding
            :class:`Metadata` field.
        :rtype: (:class:`dropbox.files.FileMetadata`,
                 :class:`requests.models.Response`)
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.files.PreviewError`
        """
        o = files.PreviewArg(path,
                             rev)
        r = self.request(self.HOST_CONTENT,
                         'files/get_preview',
                         self.ROUTE_STYLE_DOWNLOAD,
                         bv.Struct(files.PreviewArg),
                         bv.Struct(files.FileMetadata),
                         bv.Union(files.PreviewError),
                         o,
                         None)
        self._save_body_to_file(download_path, r[1])
        return r[0]

    def files_list_revisions(self,
                             path,
                             limit=10):
        """
        Return revisions of a file

        :param str path: The path to the file you want to see the revisions of.
        :param long limit: The maximum number of revision entries returned.
        :rtype: :class:`dropbox.files.ListRevisionsResult`
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.files.ListRevisionsError`
        """
        o = files.ListRevisionsArg(path,
                                   limit)
        r = self.request(self.HOST_API,
                         'files/list_revisions',
                         self.ROUTE_STYLE_RPC,
                         bv.Struct(files.ListRevisionsArg),
                         bv.Struct(files.ListRevisionsResult),
                         bv.Union(files.ListRevisionsError),
                         o,
                         None)
        return r

    def files_restore(self,
                      path,
                      rev):
        """
        Restore a file to a specific revision

        :param str path: The path to the file you want to restore.
        :param str rev: The revision to restore for the file.
        :rtype: :class:`dropbox.files.FileMetadata`
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.files.RestoreError`
        """
        o = files.RestoreArg(path,
                             rev)
        r = self.request(self.HOST_API,
                         'files/restore',
                         self.ROUTE_STYLE_RPC,
                         bv.Struct(files.RestoreArg),
                         bv.Struct(files.FileMetadata),
                         bv.Union(files.RestoreError),
                         o,
                         None)
        return r

    # ------------------------------------------
    # Routes in sharing namespace

    def sharing_get_shared_links(self,
                                 path=None):
        """
        Returns a list of :class:`LinkMetadata` objects for this user, including
        collection links. If no path is given or the path is empty, returns a
        list of all shared links for the current user, including collection
        links. If a non-empty path is given, returns a list of all shared links
        that allow access to the given path.  Collection links are never
        returned in this case. Note that the url field in the response is never
        the shortened URL. This API is not supported for App Folder and
        filetypes apps.

        :param Nullable path: See :meth:`get_shared_links` description.
        :rtype: :class:`dropbox.sharing.GetSharedLinksResult`
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.sharing.GetSharedLinksError`
        """
        o = sharing.GetSharedLinksArg(path)
        r = self.request(self.HOST_API,
                         'sharing/get_shared_links',
                         self.ROUTE_STYLE_RPC,
                         bv.Struct(sharing.GetSharedLinksArg),
                         bv.Struct(sharing.GetSharedLinksResult),
                         bv.Union(sharing.GetSharedLinksError),
                         o,
                         None)
        return r

    def sharing_create_shared_link(self,
                                   path,
                                   short_url=False,
                                   pending_upload=None):
        """
        Create a shared link. If a shared link already exists for the given
        path, that link is returned. Note that in the returned
        :class:`PathLinkMetadata`, the url field is the shortened URL if the
        short_url argument is set to u'true'. This API is not supported for App
        Folder and filetypes apps.

        :param str path: The path to share.
        :param bool short_url: Whether to return a shortened URL.
        :param Nullable pending_upload: If it's okay to share a path that does
            not yet exist, set this to either 'file' or 'folder' to indicate
            whether to assume it's a file or folder.
        :rtype: :class:`dropbox.sharing.PathLinkMetadata`
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.sharing.CreateSharedLinkError`
        """
        o = sharing.CreateSharedLinkArg(path,
                                        short_url,
                                        pending_upload)
        r = self.request(self.HOST_API,
                         'sharing/create_shared_link',
                         self.ROUTE_STYLE_RPC,
                         bv.Struct(sharing.CreateSharedLinkArg),
                         bv.Struct(sharing.PathLinkMetadata),
                         bv.Union(sharing.CreateSharedLinkError),
                         o,
                         None)
        return r

    def sharing_get_shared_folder(self,
                                  id,
                                  include_membership=True):
        """
        Gets shared folder by its folder ID.

        :param str id: The ID for the shared folder.
        :param bool include_membership: If include user and group membership
            information in the response.
        :rtype: :class:`dropbox.sharing.SharedFolderMetadata`
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.sharing.SharedFolderAccessError`
        """
        o = sharing.GetSharedFolderArgs(id,
                                        include_membership)
        r = self.request(self.HOST_API,
                         'sharing/get_shared_folder',
                         self.ROUTE_STYLE_RPC,
                         bv.Struct(sharing.GetSharedFolderArgs),
                         bv.StructTree(sharing.SharedFolderMetadata),
                         bv.Union(sharing.SharedFolderAccessError),
                         o,
                         None)
        return r

    def sharing_list_shared_folders(self,
                                    include_membership=False):
        """
        Return the list of all shared folders the authenticated user has access
        to.

        :param bool include_membership: If include user and group membership
            information in the response.
        :rtype: :class:`dropbox.sharing.ListSharedFoldersResult`
        """
        o = sharing.ListSharedFoldersArgs(include_membership)
        r = self.request(self.HOST_API,
                         'sharing/list_shared_folders',
                         self.ROUTE_STYLE_RPC,
                         bv.Struct(sharing.ListSharedFoldersArgs),
                         bv.Struct(sharing.ListSharedFoldersResult),
                         bv.Void(),
                         o,
                         None)
        return r

    # ------------------------------------------
    # Routes in users namespace

    def users_get_account(self,
                          account_id):
        """
        Get information about a user's account.

        :param str account_id: A user's account identifier.
        :rtype: :class:`dropbox.users.BasicAccount`
        :raises: :class:`dropbox.exceptions.ApiError`

        If this raises, ApiError.reason is of type:
            :class:`dropbox.users.GetAccountError`
        """
        o = users.GetAccountArg(account_id)
        r = self.request(self.HOST_API,
                         'users/get_account',
                         self.ROUTE_STYLE_RPC,
                         bv.Struct(users.GetAccountArg),
                         bv.Struct(users.BasicAccount),
                         bv.Union(users.GetAccountError),
                         o,
                         None)
        return r

    def users_get_current_account(self):
        """
        Get information about the current user's account.

        :rtype: :class:`dropbox.users.FullAccount`
        """
        o = None
        r = self.request(self.HOST_API,
                         'users/get_current_account',
                         self.ROUTE_STYLE_RPC,
                         bv.Void(),
                         bv.Struct(users.FullAccount),
                         bv.Void(),
                         o,
                         None)
        return r

    def users_get_space_usage(self):
        """
        Get the space usage information for the current user's account.

        :rtype: :class:`dropbox.users.SpaceUsage`
        """
        o = None
        r = self.request(self.HOST_API,
                         'users/get_space_usage',
                         self.ROUTE_STYLE_RPC,
                         bv.Void(),
                         bv.Struct(users.SpaceUsage),
                         bv.Void(),
                         o,
                         None)
        return r

