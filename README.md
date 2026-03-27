# 🐍 Python Projects

A curated collection of personal Python side projects, ranging from security & cryptography to computer vision, competitive programming, and fun mini-applications.

## 📂 Repository Structure

### Submodule Projects (Linked Repos)

| Folder | Description | Link |
| :--- | :--- | :--- |
| `Computer_Vision_Practice` | OpenCV toolkit covering face detection, recognition, motion detection, and edge detection. | [Repo](https://github.com/Ray0737/Computer_Vision_Practice) |
| `Incryption_Practice` | Cryptography & CTF practice — RSA, AES-256 GCM, Argon2id hashing, and encoding challenges. | [Repo](https://github.com/Ray0737/Incryption_Practice) |
| `POSN_Practice` | 20 Python competitive programming solutions for POSN (Promotion of Academic Olympiad and Development of Science Education). | [Repo](https://github.com/Ray0737/POSN_Practice) |

### Standalone Projects (Files Only)

| Folder | Description |
| :--- | :--- |
| `POS_System` | Full-featured Tkinter Point-of-Sale GUI with cart, 7% VAT, transaction history, JSON persistence, and CSV export. |
| `New_Year_Timer` | New Year's Eve countdown timer in both GUI (Tkinter) and terminal versions, set for GMT+7 Bangkok time. |
| `Christmas_tree` | Animated ASCII Christmas tree with randomized ANSI color ornaments in the terminal. |
| `Card_Game` | Terminal-based multiplayer card game for up to 6 players with deck shuffling and turn-based play. |

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **GUI:** Tkinter
- **Computer Vision:** OpenCV (`opencv-contrib-python`)
- **Cryptography:** `cryptography`, `argon2-cffi`
- **Data:** JSON, CSV
- **Standard Library:** `random`, `datetime`, `os`, `sys`, `time`

## 🚀 Getting Started

```bash
# Clone with submodules
git clone --recurse-submodules https://github.com/Ray0737/Python_Projects.git

# Or if already cloned, initialize submodules
git submodule update --init --recursive
```

## ⚠️ Deployment Notes

- **POS_System** contains test credentials (`Test_user` / `0123`). Remove before any public deployment.
- **New_Year_Timer** must be launched before 23:00 on December 31st for the countdown to function correctly.
- **Computer_Vision_Practice** requires a webcam for live detection scripts. Verify all image paths (`pic\...`) when deploying.
- **Incryption_Practice**: Loss of `private_key.pem` or the Master Password means permanent data loss — by design.
