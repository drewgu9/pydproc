# pydproc

pydproc is python3 package that provides a simple to use command line interface for periodic data retrieval from APIs. Using inputs from a yml file, pydproc builds a new Docker image specific to that process. The user can then run, stop, and restart these processes for pydproc to start collecting data. When the user wants this data, they can easily retrieve it along with the run logs. This can help generate new datasets for machine learning projects as it simplifies and automates the process of data collection from APIs.

## Installation

Pydproc can be installed using pip3:

    pip3 install pydproc
    
 If you install using pip, it might not work due to conflicting versions of Python (needs Python3)
 
 If you run into a "module not found" error, you can use pip3 to install any dependencies.
 However, the package should automatically install most dependencies. 

## Getting Started

Examples of YML files can be found in examples/weather.yml

The following command builds the docker container for a specified YML file with an API code:

    pydproc build --ymlfile $FILE_PATH

To run the container to mine data do
    
    pydproc start $FILE_NAME
    
To make your YML file from user input do 

    pydproc build
 
 Commands such as start, stop, restart, and remove follow the format of 
 
    pydproc $COMMAND $PROC_NAME
 
 API data is stored in a saved_data folder. To copy data from a certain file to a destination on your local machine,
 
    pydproc get-data $RUN_NAME $DESTINATION_PATH
    
 For more information do
 
    pydproc --help
 
 Example Code: 
 
    pydproc build --ymlfile ./example/weather.yml
    pydproc start weather
    pydproc get-data ./saved_data/weather-0 ./destination
 
 Thanks for using our package!

## Potential Docker Issue
 
 This package requires docker to be installed and running. If one runs into a "docker mount denied" error, simply to go 
 Docker -> Preferences -> File Sharing and allow Docker to mount the pydproc/saved_data folder. All our API data is stored in 
 the saved_data folder, so Docker needs permission to mount this file.
 
## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Vladimir Ovechkin** - *Project setup, Initial work, Managing TODOs, Packaging* - University of Washington
* **Robert Burris** - *YAML processing, Data field validation, API data parsing* - University of Washington
* **Andrew Wu** - *Command Line Interface, Docker Container Configuration, User Manual* - University of Washington

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
