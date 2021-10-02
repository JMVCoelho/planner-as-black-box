
# USING A PLANNER AS A BLACKBOX  

**Contents:**  
A pddl domain for the Hanoi Towers problem.  
Hard-coded instances of the problem (3, 4, 5, 6, 7, 8).    
A python script (`$python3 proj1.py`) which runs a planner as a blackbox to solve the instance of the problem specified in the file `in`.  
    

## Installing Singularity  

    ```$ sudo apt-get update && sudo apt-get install -y build-essential \
        uuid-dev \
        libgpgme-dev \
        squashfs-tools \
        libseccomp-dev \
        wget \
        pkg-config \
        git \
        cryptsetup-bin ```


    ``` $ sudo apt install golang  ```
    
    ``` $ git clone https://github.com/sylabs/singularity.git && \
        cd singularity && \
        git checkout v3.5.2 ```
    
    ``` $ ./mconfig && \
        make -C ./builddir && \
        sudo make -C ./builddir install ```

## Building the planner image   
team23 was the winning team, with their planner Delfi1.  

    ``` $ wget https://bitbucket.org/ipc2018-classical/team23/raw/ipc-2018-seq-opt/Singularity
    $ sudo singularity build planner.img Singularity  ```

## Run  
In `proj.py` change the variable `PLANNER_IMG` so that it points to where your planner image is.  

Then run `python3 proj.py`.  
The solution will be printed on stdout.  