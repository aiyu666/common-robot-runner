# common-robot-runner

## Set dev env

### Install package
```
pip install -r requirements.txt
or 
pip3 install -r requirements.txt
```

### Set PYTHONPATH
```
export PYTHONPATH="$(pwd)"
```

## How to test?
```
pytest
```

## Work flow
1. checkout branch DQA-<ticket_number>
2. coding
3. fetch + rebase or pull master
4. push
5. create PR
6. link PR with ticket
    ![](https://i.imgur.com/BBdPlIJ.png =300x400)
    ![](https://i.imgur.com/iUk0IDG.png =300x400)
    ![](https://i.imgur.com/r3s7klb.png =300x400)
    ![](https://i.imgur.com/FtTa2Gf.png =300x400)

7. request code review
8. squash merge
