# Obtaining sources



Download source tar.gz from github mdata-client release page into SOURCES directory using cURL:
curl -o mdata-client-0.0.1.tar.gz -L https://codeload.github.com/joyent/mdata-client/tar.gz/20151001

The version number in `mdata-client-{version}.tar.gz` must be same as the version in SPEC file.
Consult official repository [https://github.com/joyent/mdata-client](https://github.com/joyent/mdata-client) to obtain version number of the release.

Since mdata-client release appends version derived from date to it's directory before createing tar.gz, make sure you put this value in SPEC file. The variable that you need to edit is `tar_version` at the top of the SPEC file.
