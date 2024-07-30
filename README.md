# SSH Key Generator

## Project Description 

This project aims to generate SSH keys securely and automatically and this code was created as part of my cybersecurity training to learn and understand how it works.

## Screenshot 📸

![Projet](https://github.com/user-attachments/assets/b4acc8bf-4296-47cc-b5b6-0c15270fa00a)

## Use

1. Clone the GitHub repository to your local machine <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" height="15" alt="git logo" />:

    ```
    git clone https://github.com/Alexous-O/SSH-Key-Generator.git
    ```
    
2. Open the project then start them :

## Explanations

1. Importing the paramiko library :
	- import paramiko

2. Fonction generate_ssh_key_pair :
	- This function generates an SSH key pair (private key and public key) and writes them to specified files.

3. RSA private key generation:
	- key = paramiko.RSAKey.generate(2048) generates a 2048-bit RSA private key.

4. Writing the private key to a file:
	- with open(private_key_file, "w") as private_key_file_obj: opens the file for the private key in write mode.
	
	- key.write_private_key(private_key_file_obj) writes the private key to the file.

5. Writing the public key to a file:
	- with open(public_key_file, "w") as public_key_file_obj: opens the file for the public key in write mode.

	- public_key_file_obj.write(f"{key.get_name()} {key.get_base64()}") writes the public key to the file.

6. Call the function to generate the key pair:
	- generate_ssh_key_pair(private_key_file, public_key_file) generates the key pair and saves them in the id_private_key and id_public_key files.

## Author 👨‍💻
The project was created by myself.
