# common-robot-runner

## Setup your development environment
### Install  pipenv
* Brew
    ```
    brew install pipenv
    ```
* pip
    ```
    pip install pipenv
    ```

### Run the vurtual environment
```
pipenv shell
```

### How to install package in your vurtual environment?
```
pipenv install <package_name>
or
pipenv install <package_name> --dev
```

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
