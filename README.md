[<img src="https://img.shields.io/docker/v/therealjohannes/server_backup?label=Dockerhub">](<https://hub.docker.com/repository/docker/therealjohannes/server_backup>)
# MiniAutoBackup
A mini backup server that syncs local folders to the cloud using rclone. This can be used to automatically keep a second backup of a local server on a commercial cloud service like onedrive or google drive (ideally using rclones [crypt](https://rclone.org/crypt/) functionality).

The backup service can be easily set up by configuring the docker-compose file. Here you have to specify, which local folders you want to be backed up. Also you need to mount the rclone config file with an already set up remote.
Once that is done, adjust the environment variable *REMOTE_EXPORT_PATH* to point to a path on the configured rclone remote and choose when you want the backup to run with *UPLOAD_SCHEDULE*.
