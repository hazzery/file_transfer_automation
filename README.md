# file_transfer_automation

file_transfer_automation is a simple file transfer automation tool.
It is used to transfer files from an FTP server once a day.

## Configuration

All configuration of file_transfer_automation is specified in `config.toml`.
The config file contains the following options:


 - `schedule_time` - The time of day for the email to be scheduled.

#### FTP
 - `hostname` - The hostname of the FTP server.
 - `port_number` - The port number the FTP server is running on.
 - `username` - Your username to authenticate your FTP session.
 - `password` - Your password to authenticate your FTP session.
 - `working_directory` - The directory within the FTP server you would like to download files from

## How to run

To run file_transfer_automation execute the following command.
```bash
python3 -m file_transfer_automation
```
This will run in your terminal perpetually, downloading the contents of the specified directory daily,
until stopped manually.
