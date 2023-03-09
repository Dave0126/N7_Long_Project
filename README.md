# N7_Long_Project

## Introduction

This project that involves the design of a drone path configuration system that is intended to operate within the U-space framework. The technology tries to address some of the issues with safety that come with integrating drones into airspace,especially the modification of the trajectory of a drone following a reconfiguration of the airspace when imposing constraints on the trajectory initially planned.

## Development environment 

- `Python Ver. 3.10.10`

- `pip Ver. 23.0`

- `PyQt5 Ver. 5.15.7`

  ```shell
  pip3 install pyqt5==5.15.7
  ```

- `PyQtWebEngine Ver. 5.15.6`

  ```shell
  pip3 install pyqtwebengine==5.15.6
  ```




## How to run the demo: 

In the project `root` directory:

```
make demo
```



## Development Specifications

### Code Submission Specification

- All `commit` must be <u>***commented***</u>, and the content must describe briefly what is involved in the commit.

  ```shell
  git commit -m "Comments"
  ```

- A reasonable level of granularity in `commit`, with one commit containing a single function point.



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
  feat/featureName[/developerName]
  ```

- All `feat` branches use `dev` branch as their parent branches

  ```shell
  git fetch origin dev 		# no merge
  # OR
  git pull origin dev 		# merge
  ```

- Pull a `feat` branch from develop on a <u>***feature level***</u>

- Each `feat` branch should be as <u>***fine-grained***</u> as possible to facilitate fast iteration and avoid conflicts

- When one of the `feat` branches is complete, it is <u>***merged back***</u> into the `dev` branch

  ```shell
  git checkout dev 		# switch to dev branch
  git merge _YOUR_FEATURE_BRANCH 		# merge your feature branch
  git push origin dev 		# update remote dev branch on GitHub
  ```

- `feat` branches only interact with the `dev` branch, <u>***NOT directly***</u> with the `master` branch





## Notice

- `2023-02-15`

  When the frontend program calls `addPoint()` and `addAreas()` to create restricted areas with a graphical interface, it will generate temporary JSON files, which are saved in the `data/temp` folder. The above two methods will repeatedly call the `folium.plugins.Draw()` function, so for the second called function, two JSON files with the same content will be written repeatedly.





## Demos

1. `2023-02-15` Frontend-MainWindow by Guohao

![screenshot1](demos/screenshot1.gif)


2. `2023-02-23` Rewrite `MainWindow` and all JS methods for `map` and integrate with `Drone Simulation`

![screenshot1](demos/screenshot2.gif)

