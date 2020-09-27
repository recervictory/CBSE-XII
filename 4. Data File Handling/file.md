## 4.1 : Introduction
- Computer Program needs to process different types for files.
- These files stored information or data in the permanent location in the Computer and serve different purpose in computer application
    - For Word Processer, we use Document files(*.doc/,*.docx).
    - Database program has its own types of file system (*.db).
    - Complier program use source files to generate executable file.
- Programs that are used in day-to-day business operations rely extensively on files. 

    A file in itself is a bunch of bytes stored on some storage devie like hard-disk, pen-drive. It  a document or the data stored on a permanent storage device which can be read,written or rewritten according to requirement. In other words, data is packaged up on the storagedevice as data structures called Files. 

## 4.2 : Data Files
A data files are the files that store data pretraining to a specific application, for later use. The data files can be stored in two ways :
- Text Files
- Binary Files

1. **Text Files**: A text files stores information in *ASCII or UniCode* characters. In the text files, each lines is terminated,(delimited) with a special characters known known as **EOF(End of Line)** character. In the text files, some internal translations take places when this EOL character is read or written. In Python, by default, this EOL character is newline character ('\n') or carriage-return, newline combination('\r\n').
2. **Binary Files**: A binary files is just that contains information in same format in which the information is held in memory. i.e., the files content that return to you is raw format (with no translations or specific encoding). In binary files, there is no delimited for lines. Also no translations occurs in binary files. As a result, binary files are faster and easier for a program to read and write in compare with a text files. As long as the people or need to be ported to different type of system, binary files are the best way to store program.


## 4.3 Data File Operations
In python file data file operations a strict rule needed to be follow. **After performing desirable operation, it needs to be close so that resources that are tied with the file are freed**.
Thus, python file handling takes place in the following order:
1. Opening a file.
2. Performing operation (read, write, etc.) or processing data.
3. Closing the File.

## 4.4 Opening and Closing Files
To handle data files in Python, we need to have a `file variable or file object or file handle`. Object can be created by using `open()` function and `file()` function.  To work with file we need to open it. This is done by using the build in `open()` function.
***
- **Opening a File -- open():** When we want to read or write from storage devices, we must first open the file. When we open a file, the file must stored on the same folder  that we are start the python. `open()` function takes the **name** of the file (i.e data.txt) as first argument. The second argument indicates the **mode of accessing** the file. This is an optional parameter the default mode is **read mode** or `"r"`.
    - **Modes for Opening a File :**
      - Read (`"r"`): to read file,
      - Write(`"w"`): to write to the file,
      - append(`"a"`): to write a file in append mode (write at the end of file)

- **Syntax:**
    > file_object = open(file_name,access_mode)
- **Example:**
    > file_handler = open(data.txt,"r")
***

