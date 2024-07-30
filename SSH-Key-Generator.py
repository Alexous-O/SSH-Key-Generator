# pip install paramiko

import paramiko
from art import *
from termcolor import colored

print(colored("""
_______    .-------.     .-./`)  .-./`)  .-./`)      ,-----.         _______    .---.  .---.      .-''-.       .-''-.   
\  ____  \  |  _ _   \    \ .-.') \ .-.') \ .-.')   .'  .-,  '.      /   __  \   |   |  |_ _|    .'_ _   \    .'_ _   \  
| |    \ |  | ( ' )  |    / `-' \ / `-' \ / `-' \  / ,-.|  \ _ \    | ,_/  \__)  |   |  ( ' )   / ( ` )   '  / ( ` )   ' 
| |____/ /  |(_ o _) /     `-'`"`  `-'`"`  `-'`"` ;  \  '_ /  | : ,-./  )        |   '-(_{;}_) . (_ o _)  | . (_ o _)  | 
|   _ _ '.  | (_,_).' __   .---.   .---.   .---.  |  _`,/ \ _/  | \  '_ '`)      |      (_,_)  |  (_,_)___| |  (_,_)___| 
|  ( ' )  \ |  |\ \  |  |  |   |   |   |   |   |  : (  '\_/ \   ;  > (_)  )  __  | _ _--.   |  '  \   .---. '  \   .---. 
| (_{;}_) | |  | \ `'   /  |   |   |   |   |   |   \ `"/  \  ) /  (  .  .-'_/  ) |( ' ) |   |   \  `-'    /  \  `-'    / 
|  (_,_)  / |  |  \    /   |   |   |   |   |   |    '. \_/``".'    `-'`-'     /  (_{;}_)|   |    \       /    \       /  
/_______.'  ''-'   `'-'    '---'   '---'   '---'      '-----'        `._____.'   '(_,_) '---'     `'-..-'      `'-..-'   
                                                                                                                         """, 'green'))
print(colored('Created-by-Briiiochee\n\n', 'green'))

def generate_ssh_key_pair(private_key_file, public_key_file):
    
    key = paramiko.RSAKey.generate(2048)                                            # Generate a new RSA private key
    
    with open(private_key_file, "w") as private_key_file_obj:                       # Write the private key to a file
        key.write_private_key(private_key_file_obj)
    
    with open(public_key_file, "w") as public_key_file_obj:                         # Write the public key to a file
        public_key_file_obj.write(f"{key.get_name()} {key.get_base64()}")

    print(f"Private key stored in {private_key_file}")
    print(f"Public key stored in {public_key_file}")

private_key_file = "id_private_key.txt"                                             # Set file names for keys
public_key_file = "id_public_key.pub"

generate_ssh_key_pair(private_key_file, public_key_file)                            # Generate the key pair