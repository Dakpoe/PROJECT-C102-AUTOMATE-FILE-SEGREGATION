import os
import shutil


from_dir = "Downloads"
to_dir = "C:/Users/fritz/OneDrive/Desktop/VIsual Studio Code/Document_Files"


list_of_files = os.listdir(from_dir)


for file_name in list_of_files:
    
    source_path = os.path.join(from_dir, file_name)
    destination_path = os.path.join(to_dir, "Document_Files", file_name)
    
    
    if '.' not in file_name:
        continue
    
   
    extension = os.path.splitext(file_name)[1]
    allowed_extensions = ['.txt', '.doc', '.docx', '.pdf']
    if extension.lower() in allowed_extensions:
        
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        
        shutil.move(source_path, destination_path)
        print(f"Moved {file_name} to {destination_path}")
