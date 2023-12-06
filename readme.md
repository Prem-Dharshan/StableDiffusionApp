### Stable Diffusion App

---

## Steps

#### Step 1: Install VSC & Github Desktop

#### Step 2: https://github.com/nicknochnack/StableDiffusionApp.git
Copy this link and paste in File > Clone respository > URL > paste the link > Choose Local path > Click Clone 

Repo will be cloned in the path chosen and click Open with VSC

#### Step 3: Run the below command 
Bash: 
```
python -m venv venv 
```
CMD:
```
python -m venv <name_of_virtualenv>
```

Run the below command to activate venv
```
source <name_of_virtualenv>/bin/activate
```
In our case,
```
source venv/bin/activate
```

#### Step 4: Install packages
```
pip install -r requirements.txt 
```
```
python.exe -m pip install --upgrade pip
```

#### Step 5: Get Auth Token

Goto https://huggingface.co/docs/hub/security-tokens

Register/ Login and generate a User access Token
in https://huggingface.co/settings/tokens

Copy the token and paste in authtoken.py

auth_token = "YOUR HUGGING FACE TOKEN HERE" 

#### Step 6: Run app.py
```
python app/app.py
```

The program will take some time to be interpreted. DW :)

---

## Summary 

The program provides a simple GUI for users to input text, generate images using a pre-trained model, and display the generated images in the GUI. The model used for image generation appears to be a stable diffusion model loaded from the Hugging Face Model Hub.
