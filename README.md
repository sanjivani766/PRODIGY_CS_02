# 🔐 Pixel Manipulation For Image Encryption 

## Overview

The **Pixel Manipulation Image Encryption Tool** is a Python-based application designed to demonstrate fundamental **image security and cryptographic principles**.
The system encrypts digital images by applying **pixel value transformation and pixel position permutation**, ensuring that the original image becomes unreadable without the correct secret key.

The application also provides a **graphical user interface (GUI)** built with Tkinter, allowing users to easily select images, encrypt them, and restore them through decryption.


## 🎯 Objectives

* Implement a simple yet effective **image encryption mechanism**
* Demonstrate **symmetric key encryption principles**
* Apply **pixel-level transformations for data protection**
* Build a **user-friendly graphical interface**
* Understand how encryption concepts can be applied to multimedia data


## ✨ Key Features

* Image selection through a graphical interface
* Encryption using a **secret numeric key**
* Pixel value manipulation using modular arithmetic
* Pixel shuffling (permutation) to obscure image structure
* Decryption functionality to restore the original image
* Automatic generation of encrypted and decrypted image files
* Error handling for invalid inputs


## 🛠 Technologies Used

* **Python** – Core programming language
* **Tkinter** – GUI development
* **Pillow (PIL)** – Image processing
* **Random Module** – Pixel permutation logic


## ▶ Running the Application

Execute the following command:

```bash
python img_encryption_tool.py
```

This will launch the graphical interface where users can select an image and perform encryption or decryption.


## 🔐 Encryption Methodology

The encryption algorithm combines two fundamental cryptographic techniques:

### 1. Pixel Value Transformation

Each pixel in the image contains three color components:

```
(Red, Green, Blue)
```

These values are modified using a secret key and modular arithmetic:

```
Encrypted Value = (Original Value + Key) mod 256
```

This ensures that the resulting pixel values remain within the valid RGB range.

---

### 2. Pixel Permutation (Shuffling)

To further enhance security, the encrypted pixels are **randomly shuffled** using the secret key as a seed value. This disrupts the spatial structure of the image, making it visually unrecognizable.

---

### 3. Decryption Process

The decryption process reverses both steps:

1. Restore the original pixel order (reverse permutation)
2. Restore original pixel values using the same secret key

```
Original Value = (Encrypted Value - Key) mod 256
```

Only users with the **correct encryption key** can recover the original image.


## 📂 Project Structure

```
pixel-image-encryption
│
├── img_encryption_tool.py
├── input.jpg
├── encrypted_image.png
├── decrypted_image.png
└── README.md
```


## 🔎 Example Workflow

1. Launch the application
2. Select an image from your system
3. Enter a numeric secret key
4. Click **Encrypt Image** to generate an encrypted version
5. Select the encrypted image
6. Enter the same key and click **Decrypt Image**
7. The original image will be restored


## 🧠 Cybersecurity Concepts Demonstrated

* Image-based data protection
* Symmetric key cryptography
* Pixel manipulation encryption
* Permutation-based obfuscation
* Modular arithmetic in encryption systems


## 🚀 Future Enhancements

Potential improvements for this project include:

* Implementation of stronger cryptographic algorithms
* Password-based key generation
* Image preview within the GUI
* Batch image encryption
* Integration with advanced encryption standards
* Secure key management mechanisms


## 📜 Note

This project is intended for **educational and research purposes** as part of a cybersecurity learning initiative.
