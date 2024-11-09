# Fakeproof-for-GFG-Hakathon

# Deepfake Video Generator 
The main objective of this project is to develop a robust deepfake video generation system capable of producing highly realistic synthetic media. This will involve:

Data Acquisition: Collecting a diverse dataset of high-quality videos and images.

Model Development: Training a sophisticated deep learning model, such as Inswapper, on the collected dataset.

Deepfake Generation: Utilizing the trained model to seamlessly integrate a source person's face onto a target video.

Post-Processing: Refining the generated deepfake videos through techniques like frame colour correction and frame enhancer.

Ethical Considerations: Adhering to ethical guidelines and responsible use of deepfake technology.


# Detailed Component Diagram

**1. User Interface (UI)**

**Input Module:** Enables users to upload source images/videos and select target faces.

**Output Module:** Displays the generated deepfake and allows downloading or sharing.

**2. Backend Services**

**API Layer:** Manages communication between the UI and backend processing modules.

**3. Data Processing Module**

**Face Detection and Alignment:** Extracts and aligns faces from input data for consistent processing.

**Data Preprocessing:** Normalizes and prepares data for model input.

**4. Deep Learning Model**

**Face Encoder:** Encodes facial features of source and target faces.

**Face Generator:** Creates the deepfake by mapping target features onto the source face.

**5. Post-processing Module**

**Refinement Tools:** Enhances output quality through smoothing and colour adjustments.

**Output Generation:** Combines frames into the final video or image format.

# Technical Documentation

Be aware installations needs technical skills and is not recommended for beginners

# 1. Prepare Your Platform

**GIT**

winget install -e --id Git.Git

**Conda**

winget install -e --id Anaconda.Miniconda3 --override "/AddToPath=1"

**FFmpeg**

winget install -e --id Gyan.FFmpeg

**Codec**

winget install -e --id CodecGuide.K-LiteCodecPack.Basic

# 2. Prepare Your Environment 

**Initialize conda for your terminal:**

*conda init –all*

**Create the environment:**

*conda create --name facefusion python=3.12*

**Activate the environment:**

*conda activate facefusion*

# 3.Install Your Accelerator

CUDA

Compatible with NVIDIA graphic cards:

*conda install conda-forge::cuda-runtime=12.4.1 conda-forge::cudnn=9.2.1.18*

TensorRT 5. Install The Application

Copy

Install pytorch to run on GPU from https://pytorch.org/get-started/locally/ according to the hardware and CUDA compatibility. Run command *pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118* 

(if you have CUDA 11.8 on your windows)

*python install.py --onnxruntime {default, ...}*

Suitable for high performance NVIDIA graphic cards:

*pip install tensorrt==10.5.0 --extra-index-url https://pypi.nvidia.com*



# 4. Download Your Copy

Clone the repository:

*git clone <our repo link>*

Ensure to enter the directory:

using command *cd facefusion* and install the requirements file by running command *pip install -r requirements.txt*

# 5. Install The Application

*python install.py --onnxruntime {default, ...}*

# 6. Reload Your Environment

*conda deactivate*

*conda activate facefusion*

# 7. Done

Finally, run the program:

*python facefusion.py run --open-browser*

(some models will be downloaded before finally running the program for the first time)

# 8. Access the Web Interface: 

Open a browser and navigate to  http://127.0.0.1:7860

To exit go to running current terminal and press ***Ctrl + c***# Fakeproof-for-GFG-Hakathon
