# N7_Long_Project

- `Python Ver. 3.10.10`
- `pip Ver. 23.0`
- `PyQt5 Ver. 5.15.7`
- `PyQtWebEngine Ver. 5.15.6`
- `folium Ver. 0.14.0`


To run the demo: 
```
python3 src/frontend/main.py
```



## Development Specifications

### GIT Branch Conventions

We have three types of branches, <u>***Master***</u> and <u>***Develop***</u>.

- `master` branch is used to organize activities related to software development and deployment.
- `develop` branch organizes the various activities that are done to solve a specific problem.

The master branch is the core branch for all development activities. The output of all development activities is ultimately reflected in the code of the master branch.



#### `develop` Branch

- The `develop` branch is a development branch and generally contains all new features being developed
- The `develop` branch cannot interact directly with the `master` branch
- The `develop` branch spawns `feature` branches
- The `develop` branch is a protected branch and cannot be directly pushed to the remote repository develop branch
- A project can have <u>***ONLY ONE***</u> develop branch

##### `feature` Branch

- Naming convention:

  ```
  feature_featureName		OR	feature_featureName/developerName
  ```

- All `feature` branches use `develop` branch as their parent branches

- Pull a `feature` branch from develop on a <u>***feature level***</u>

- Each `feature` branch should be as <u>***fine-grained***</u> as possible to facilitate fast iteration and avoid conflicts

- When one of the `feature` branches is complete, it is <u>***merged back***</u> into the `develop` branch

- `feature` branches only interact with the `develop` branch, <u>***NOT directly***</u> with the `master` branch

