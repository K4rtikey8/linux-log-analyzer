# Linux Log Analyzer

A Python-based Linux log analysis tool that reads log files, counts log levels, generates reports, and allows filtering of specific log entries using command-line arguments.

## Features

### Version 1

* Read Linux log files
* Count INFO messages
* Count WARNING messages
* Count ERROR messages

### Version 2

* Detect the most common log level

### Version 3

* Generate analysis reports in a text file

### Version 4

* Create timestamped reports
* Store reports in a dedicated reports folder

### Version 5

* Filter logs using command-line arguments
* Display only selected log levels

## Technologies Used

* Python 3
* Linux
* Git
* GitHub

## Project Structure

linux-log-analyzer/

├── log_analyzer.py

├── sample.log

├── reports/

├── README.md

└── .gitignore

## Installation

Clone the repository:

git clone https://github.com/K4rtikey8/linux-log-analyzer.git

Move into the project directory:

cd linux-log-analyzer

Run the program:

python3 log_analyzer.py

## Usage Examples

Run normal analysis:

python3 log_analyzer.py

Filter ERROR logs:

python3 log_analyzer.py ERROR

Filter WARNING logs:

python3 log_analyzer.py WARNING

Filter INFO logs:

python3 log_analyzer.py INFO

## Sample Output

===== LOG ANALYSIS REPORT =====

INFO Count: 3

WARNING Count: 2

ERROR Count: 5

Most Common Log Level: ERROR

## What I Learned

* Reading files in Python
* Writing reports to files
* Working with timestamps
* Command-line arguments using sys.argv
* Linux file management
* Git and GitHub workflow
* Basic log analysis concepts

## Future Improvements

* CSV report generation
* Graphical dashboard
* Real Linux system log support
* AWS deployment on EC2
* Email alerts for critical errors

## Author

Kartikey Tiwari

Computer Science Student

Cloud & AI Enthusiast

