Classroom Carbon Footprint Reduction Using AI & ML
This project aims to minimize energy consumption in classrooms by automatically controlling lights and fans based on student occupancy and location. Leveraging AI and machine learning (ML) techniques with YOLOv8 for object detection, this system ensures that lights and fans are only active when students are present below them, reducing unnecessary energy use and promoting sustainable practices.

Project Overview
The Classroom Carbon Footprint Reduction system uses CCTV footage from the classroom to detect student locations in real-time. Using OpenCV for image processing and YOLOv8 for efficient object detection, the system identifies whether students are present beneath specific lights or fans. If a fan or light is not directly above any student, it automatically turns off, thus conserving electricity and reducing the classroom’s carbon footprint.

Features
AI-Powered Detection: Uses YOLOv8 to detect students and analyze their positions in relation to classroom lights and fans.
Automated Control: Controls fans and lights based on real-time occupancy, saving energy by avoiding unnecessary usage.
Real-Time Updates: Continuously monitors and adjusts as students enter, leave, or move within the classroom.
Energy Efficiency: Contributes to carbon footprint reduction through intelligent resource management.
How It Works
Student Detection: Using a CCTV camera, YOLOv8 detects students' presence and positions in the classroom.
Location Mapping: Maps detected students’ locations to specific zones below lights or fans.
Automated Switching: Turns lights and fans on only in occupied zones and off in unoccupied ones, controlled via a connected hardware relay.
Technology Stack
AI/ML Model: YOLOv8 model for object detection
Libraries: OpenCV for image processing and object tracking
Hardware: IoT devices and relays for light and fan control
Programming Language: Python for system integration
Framework: Deep learning framework for YOLOv8 model deployment
System Requirements
Hardware: CCTV camera, IoT relay switches for controlling fans and lights
Software: Python, OpenCV, and YOLOv8 dependencies
Computational Requirements: GPU for efficient processing (recommended for YOLOv8)
