# MLOps Home Assignment - GTD infrastracture Team 

## Exercise Overview
In this exercise, you will design and implement a video processing pipeline. The system should detect pedestrians in a video, extract their pose estimation, and generate a new video with visual overlays.

## Your Task
You are responsible for the **entire stack**, including:
1.  **Infrastructure:** Setting up the Docker environment and Orchestrator (Airflow).
2.  **Pipeline Logic:** Implementing the object detection and pose estimation steps.
3.  **Data Handling:** Managing the flow of video data through the pipeline.

## Requirements
* **Language:** Python.
* **Orchestration:** Apache Airflow.
* **Delivery:** A standard \`docker-compose.yml\` that spins up the whole system.
* **Input:** A video file placed in the \`input/\` folder.
* **Output:** A processed video saved to the \`output/\` folder.

## Recommended Tools
You are free to use any suitable models or libraries, but the following are standard recommendations:
* **Detection:** [YOLOv8](https://github.com/ultralytics/ultralytics)
* **Pose Estimation:** [ViTPose](https://github.com/ViTAE-Transformer/ViTPose)

## Getting Started

### 1. Initialize Dataset
We will be using the **MOT Video Data** from Kaggle.
Run the initialization script to check for the data or attempt an automated download:

\`\`\`bash
./scripts/init_dataset.sh
\`\`\`

*If the script cannot download automatically, it will provide a link for you to manually drop the file into the \`input/\` folder.*

### 2. Example Notebook
The repository includes an `example.ipynb` notebook that demonstrates the core functionality of the video processing pipeline:

* **Video Processing:** Shows how to use `VideoProcessor` to load and extract frames from video files
* **Pedestrian Detection:** Demonstrates `PedestrianDetectionModel` to detect pedestrians in video frames with bounding boxes
* **Pose Estimation:** Illustrates `PoseEstimationModel` to estimate human pose keypoints for detected pedestrians

The notebook provides a step-by-step walkthrough of:
1. Loading a video frame
2. Detecting pedestrians and visualizing bounding boxes
3. Estimating pose keypoints for each detected person and overlaying them on the image

This example serves as a reference implementation and can help you understand how to integrate the detection and pose estimation models into your pipeline.

## Submission Instructions
**⚠️ IMPORTANT: DO NOT FORK THIS REPOSITORY**
Forks are public by default, which means other candidates can see your solution.

1.  Click the green **"Use this template"** button at the top right of this page and select **"Create a new repository"**.
2.  Name your repository (e.g., \`video-pipeline-solution\`).
3.  **Crucial:** Set the visibility to **Private**.
4.  Implement your solution in your new private repository.
5.  When you are ready to submit, add **\`yitzhaklevi\`** as a collaborator (Settings -> Collaborators -> Add people).
6.  Send the link to your repository to the hiring team.

## Deliverables
* Source code for your DAGs and scripts.
* \`docker-compose.yml\` to run the environment.
* \`README.md\` explaining how to run your solution.
