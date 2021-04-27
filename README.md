# Image Repo
Simple tool for backing up images as their hashed bytes into a csv file. Lots of potential for future development such as tagging!

## How it works
I focused on creating a command-line interface to simplify effort on the UI and focus my efforts on the logic. For the CLI, I used the Click library.

The backend is mainly powered by Pandas, which allows for effortless data manipulation. The csv files in the `repo` folder act like pseudo-databases and the user is free to add and download images as they like.

## How to use

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Create Image Repo
```bash
python image_repo/main.py create-repo my_repo_name
```

### Add Image to Image Repo
```bash
python image_repo/main.py add-image path/to/image.jpg my_repo_name
```

### Print Out Images
```bash
python image_repo/main.py list-images my_repo_name
```

### Dump Images
```bash
python image_repo/main.py dump-images my_repo_name
```
