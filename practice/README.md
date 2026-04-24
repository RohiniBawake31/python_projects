# Impose two images
'''This is a guide for impose two images '''

# How to run?
### clone this repo:
```  git clone https://github.com/Rohinibawake/Impose_images```

### Navigate to the project folder:
```cd Impose_images/ ```

### Build docker image : 
``` docker build -t image .```

### Run docker container:
``` docker run -it --rm  -v /mnt/c/users/asus/Downloads/:/impose/data image ```