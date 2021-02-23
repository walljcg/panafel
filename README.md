# panafel

* The analysis worksheet relies on the Esri ArcMap Desktop environment v10.7.1) with a valid spatial analyst license. It requires the x64 python environment is installed (i.e. install the 'Background Geoprocessing' tools).

* Please update your system PATH environment variables to include the following two entries:

    ```console
    C:\Python27\ArcGISx6410.7
    C:\Python27\ArcGISx6410.7\Scripts
    ```

* install the requirements:

    ```console
    pip install -r requirements.txt
    ```

* start the notebook server

    ```console
    jupyter notebook
    ```

* please note that the 'AnimalTracking' movement database used in the analysis worksheet has not been included for secuirty reasons. Please contact the author directly for access. 

* several of the analytical steps require the R statistical program. Cells requiring R have been highligted with the %%R cell magic identifier