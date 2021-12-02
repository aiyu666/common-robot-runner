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

### Install pre-commit
```
brew install pre-commit
or
pip install pre-commit

pre-commit install
```

If the check lint when you commit
#### Fail result
![](https://i.imgur.com/qUXkF7G.png)

#### Success result
![](https://i.imgur.com/sMI5pWI.png)

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
    * Click Power-Ups ->  "Github" -> "Attach Pull Request..."

        ![](https://i.imgur.com/Wuf10eL.png)
    * Select your Pull Request

        ![](https://i.imgur.com/aZwCyfy.png)

    * Trello will show your Pull Request

        ![](https://i.imgur.com/fzCKZlE.png)
    * Github Pull Request will comment the trello ticket link

        ![](https://i.imgur.com/Scsyne2.png)

7. Request code review
8. Squash merge
