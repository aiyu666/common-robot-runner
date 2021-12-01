# Sequence chart

```sequence
CLI->Dispatcher: $ runner <testing_framework>
Note right of CLI: input variable to decide \nwhich runner to use

Dispatcher->Runner: Call target runner instance
Note right of Dispatcher: Dispather will \ninitial instance in __init__

Runner->Runner: Run target runner
Runner->Service: Call service module
Service-->Runner: Response service result

Note right of Service: According to optional variable\n to decide to trigger which service

Runner->Runner: Analytics test case result\n and report to sheet \nor management tools
```
