# mdata-client-rpm

This repository contains directory structure required by rpmbuild tool to build RPM file from source tar.gz file.  

This repository DOES NOT contain mdata-client source code.  
To obtain the source code you will need to either clone repository or download release from [official mdata-client Joyent repo](https://github.com/joyent/mdata-client)

## Creating RPM

1. Clone this repository to machine on which you'll be creating RPM  
2. Go to SOURCES/ directory and download mdata-client release (or clone and tar the repo)  
  ```
  curl -o mdata-client-0.0.1.tar.gz -L https://codeload.github.com/joyent/mdata-client/tar.gz/20151001
  ```
3. `cd` into `SPEC/` directory and run `rpmbuild`  
```
rpmbuild --define "_topdir /path/to/mdata-client-rpm/" -ba mdata-client-0.0.1-1.el7.spec
```  
Where `/path/to/mdata-client-rpm/` is full path to cloned **mdata-client-rpm** repository
