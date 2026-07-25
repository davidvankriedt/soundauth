# Sound Authentication Mechanism

An exploration of using sound as an alternative to text-based passwords, facial recognition, or touch id.

## Requirements
Python + pip (>= Python 3.8)

## Installation

#### Clone this repository: 

```

git clone https://github.com/davidvankriedt/soundauth.git
```

#### Create a virtual environment:

```
python3 -m venv env
source env/bin/activate
```

#### Install dependencies:

```
pip install -r requirements.txt
```

## Usage

```
python3 soundauth.py
```

## Project Structure

soundauth.py                -- main script: "locks" terminal until you input the correct melody through a microphone.
archive/morsecode-chat.py   -- past experiment: a chat that uses morse code through sound to communicate with another party.

