# Prosody API Tool for Speech Emotion Recognition
This repository contains tools for **Prosody Analysis and Emotion Recognition**, focusing on real-time and aggregated emotion analysis using prosodic features from audio data. The project supports mental health research and application development.

## Project Overview

The Prosody API Tool is a system designed to analyze and predict emotional states from voice inputs. It consists of two main components: the Prosody Host and the Prosody Server. The Host sends voice data to the Server, which processes the data and returns predictions along with visual representations of the emotional analysis.

## Components

### Prosody Host

The Prosody Host is responsible for sending voice data to the Prosody Server and receiving the prediction results. It uses MQTT for communication with the server.

#### Functions

1. **Host Configuration**
   - Sets up the MQTT client with the broker address, port, username, and password.
   - Defines topics for sending voice data and receiving images and string responses.

2. **Callback Function**
   - Handles messages received from the server.
   - Saves received images (histogram and map) and string data (probabilities) to local files.

3. **Client Setup**
   - Initializes the MQTT client with the specified configuration.
   - Connects to the broker and subscribes to the relevant topics.

4. **Sending Voice Data**
   - Reads the voice file from a specified path and sends it to the server.
   - Waits for responses from the server and saves the received data.

5. **Display Images**
   - Displays the received histogram and map images using IPython.

#### Code Structure

- **Configuration**: Set up the MQTT client and topics.
- **Callback**: Define the `on_message` function to handle received messages.
- **Client Initialization**: Connect to the broker and subscribe to topics.
- **Sending Voice**: Read and send the voice file.
- **Display**: Show the received images.

### Prosody Server

The Prosody Server receives voice data from the Host, processes it to predict emotional states, and sends back the results along with visual representations.

#### Functions

1. **Server Configuration**
   - Sets up the MQTT client with the broker address, port, username, and password.
   - Defines topics for receiving voice data and sending images and string responses.

2. **Emotion Plotter**
   - Initializes plotting figures for histogram and The circumplex model (**The Russell map**).
   - Updates the plots with predicted probabilities and saves the images.

3. **Process WAV File**
   - Processes the received voice file to predict emotions using the Emotion2Vec model.
   - Returns the predicted emotion and probabilities.

4. **Callback Function**
   - Handles received voice data.
   - Saves the voice file, processes it, and publishes the results back to the host.

5. **Client Setup**
   - Initializes the MQTT client with the specified configuration.
   - Connects to the broker and subscribes to the voice topic.

#### Code Structure

- **Configuration**: Set up the MQTT client and topics.
- **Emotion Plotter**: Define the `EmotionPlotter` class for plotting and updating emotional analysis.
- **Process WAV File**: Define the `process_wav_file` function to process voice data.
- **Callback**: Define the `on_message` function to handle received voice data.
- **Client Initialization**: Connect to the broker and subscribe to the voice topic.

## How to Use

### Prosody Host

1. **Configuration**: Update the broker address, port, username, and password in the Host configuration section.
2. **Voice File**: Place the voice file in the specified path (`./voice_send/voice.wav`).
3. **Run the Host**: Execute the Host script to send the voice file and receive the predictions.

### Prosody Server

1. **Configuration**: Update the broker address, port, username, and password in the Server configuration section.
2. **Run the Server**: Execute the Server script to start listening for voice data from the Host.
3. **Receive and Process**: The Server will receive voice data, process it, and send back the predictions and visual representations.

## Photos and Screenshots

- **Histogram and Map Images**: The received images (**histogram** and The circumplex model (**The Russell map**)) should be saved in the `./prosody_received` directory for the Host and the `./Images` directory for the Server. These images can be displayed using the provided display code in the Host script.

![image](https://github.com/user-attachments/assets/2c04577b-7716-451f-bfaa-a33477df1bf7)

![image](https://github.com/user-attachments/assets/7ac34e04-dcc3-4cdc-b4c8-3722313bed4d)

## Example

1. **Host**: Place the voice file in the `./voice_send` directory and run the Host script.
2. **Server**: Run the Server script to start listening for voice data.
3. **Results**: The Server will process the voice data and send back the predictions and images to the Host, which will display the results.
![image](https://github.com/user-attachments/assets/96d1944c-0f23-4e6f-801b-d6de6dcb37e9)



## Dependencies

- `paho-mqtt`: For MQTT communication.
- `emotion2vecplus`: For emotion prediction.
- `matplotlib`: For plotting histograms and maps.
- `numpy` and `pandas`: For data handling.
---
## Installation
To use this tool, you need to install the required dependencies. Run the following command to install them:

```bash
pip install -r requirements.txt
```

Alternatively, you can install the dependencies manually:

```bash
pip install paho-mqtt emotion2vecplus matplotlib numpy pandas
```
---
## Acknowledgments

This project, part of the Prosody in Mental Health initiative, is developed at **Reutlingen University**.

- **Author:** Mohamad Eyad Alkostantini   
- **Supervisors:** Bakir Hadzic, Parvez Mohammed, (ViSiR, Actimi GmbH, Neuronation (Synaptikon GmbH) and PFH Göttingen)
- **Professor:** Prof. Matthias Rätsch 

We gratefully acknowledge their guidance and support throughout the project.

---

## Contact
For questions or support, please reach out to [Mohamad_Eyad.Alkostantini@Student.Reutlingen-University.DE].

