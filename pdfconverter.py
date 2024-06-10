import docx2pdf
import pdf2docx


#function to get the extension of the tile
def get_extension(filename):
    dot_index = filename.rfind(".")
    if dot_index != -1:
        return filename[dot_index:]
    else:
        return ""


#inputs
input_path = input("Enter doc name as path: ")
output_filename = input("Enter output filename with extension: ")

#output path
output_path = input_path[:input_path.rfind('\\')]
output_path = output_path + "\\"+ output_filename

input_extension = get_extension(input_path)
output_extension = get_extension(output_path)
if input_extension == "" or output_extension == "":
    print("Invalid Input")
    exit(0)
if input_extension == ".pdf" and output_extension == ".docx":
    pdf2docx.Converter(input_path).convert(output_path,start=0,end=None)
    print("File saved to: " + output_path)
if input_extension == ".docx" and output_extension == ".pdf":
    docx2pdf.convert(input_path, output_path)
    print("File saved to: " + output_path)
