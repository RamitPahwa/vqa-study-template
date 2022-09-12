## Template for conducting psychopy-base Video Quality studies

This code has a template for conducting an Absolute Category Rating Video Quality Study with psychopy and Potplayer.

The study begins with a prompt asking for the subject ID and session ID. If the session ID is >1 and no previous session scorefile was found, the program exits with a warning that the subject has to finish their first session first.

The train() function is called to present a training session. Videos are shown and ratings collected but not saved. The study invigilator is expected to guide the participant through this session.

The study() function is used to run the actual study. Videos are shown one after the other. Their paths are read from a csv file.

CSV files and video folders are hardcoded for simplicity. Please change them for your application.