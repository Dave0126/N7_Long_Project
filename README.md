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

> [GIT tutorial](https://www.w3schools.com/git/)

We have 2 types of branches, <u>***Master***</u> and <u>***Develop***</u>.

- <u>***Master***</u> branch is used to organize activities related to software development and deployment.
- <u>***Develop***</u> branch organizes the various activities that are done to solve a specific problem (<u>***features***</u>).

The master branch is the core branch for all development activities. The output of all development activities is ultimately reflected in the code of the master branch.



#### `master` branch

- The `master` branch holds the official release history and the release tag identifies the different releases
- A project can have <u>***ONLY ONE***</u> `master` branch
- The `master` branch is only updated when new code is <u>***released***</u> for deployment
- `master` branch is a <u>***protected***</u> branch and <u>***CANNOT***</u> be directly pushed to a remote master branch
- In our project, the `master` branch code <u>***CAN ONLY***</u> be merged with the `dev` branch.



#### `dev` branch (develop)

- The `dev` branch is a development branch and generally contains all new features being developed
- The `dev` branch cannot interact directly with the `master` branch
- The `dev` branch spawns `feature` branches
- The `dev` branch is a protected branch and cannot be directly pushed to the remote repository develop branch
- A project can have <u>***ONLY ONE***</u> `dev` branch



#### `feat` Branch (feature)

- Naming convention:

  ```
  feat/featureName		OR	feature_featureName/developerName
  ```

- All `feature` branches use `develop` branch as their parent branches

- Pull a `feature` branch from develop on a <u>***feature level***</u>

- Each `feature` branch should be as <u>***fine-grained***</u> as possible to facilitate fast iteration and avoid conflicts

- When one of the `feature` branches is complete, it is <u>***merged back***</u> into the `develop` branch

- `feature` branches only interact with the `develop` branch, <u>***NOT directly***</u> with the `master` branch

