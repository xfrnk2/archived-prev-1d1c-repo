

from __future__ import print_function
from googleapiclient import errors
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file as oauth_file, client, tools

def main():
    """Runs the sample.
    """
    SCRIPT_ID = 'AKfycbzONlW7e46d1QJJtsZmbpDrcWAI2q1ZpC6csz0WzJvdMMHgLSCL29D4sDMzajKZ3AUHjg'

    # Set up the Apps Script API
    SCOPES = [
        'https://www.googleapis.com/auth/script.scriptapp',
        'https://www.googleapis.com/auth/drive.readonly',
        'https: // mail.google.com',
        'https: // www.googleapis.com / auth / userinfo.email',
    ]
    store = oauth_file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret_332770532992-2t4k4ih20nort498dctigus2upr9u64t.apps.googleusercontent.com.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('script', 'v1', credentials=creds)

    # Create an execution request object.
    request = {"function": "getCalendar_sendMail"}

    try:
        # Make the API request.
        response = service.scripts().run(body=request,
                scriptId=SCRIPT_ID).execute()

        if 'error' in response:

            # The API executed, but the script returned an error.

            # Extract the first (and only) set of error details. The values of
            # this object are the script's 'errorMessage' and 'errorType', and
            # an list of stack trace elements.
            error = response['error']['details'][0]
            print("Script error message: {0}".format(error['errorMessage']))

            if 'scriptStackTraceElements' in error:
                # There may not be a stacktrace if the script didn't start
                # executing.
                print("Script error stacktrace:")
                for trace in error['scriptStackTraceElements']:
                    print("\t{0}: {1}".format(trace['function'],
                        trace['lineNumber']))
        else:
            # The structure of the result depends upon what the Apps Script
            # function returns. Here, the function returns an Apps Script Object
            # with String keys and values, and so the result is treated as a
            # Python dictionary (folderSet).
            folderSet = response['response'].get('result', {})
            if not folderSet:
                print('No folders returned!')
            else:
                print('Folders under your root folder:')
                for (folderId, folder) in folderSet.items():
                    print("\t{0} ({1})".format(folder, folderId))

    except errors.HttpError as e:
        # The API encountered a problem before the script started executing.
        print(e.content)


if __name__ == '__main__':
    main()