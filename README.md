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
1. Checkout branch DQA-<ticket_number>
2. Coding
3. Fetch + rebase or pull master
4. Push
5. Create PR
6. Link PR with ticket
    * 點擊強化功能的 "Github" -> 選取附加提取要求(PR)

        ![](https://i.imgur.com/Wuf10eL.png)
    * 選取 PR

        ![](https://i.imgur.com/aZwCyfy.png)

    * Trello 會顯示 PR

        ![](https://i.imgur.com/fzCKZlE.png)
    * PR 會顯示 Trello ticket link

        ![](https://i.imgur.com/Scsyne2.png)

7. Request code review
8. Squash merge
