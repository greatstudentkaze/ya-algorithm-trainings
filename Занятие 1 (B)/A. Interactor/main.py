code = int(input())
interactor_verdict = int(input())
checker_verdict = int(input())

if interactor_verdict == 0:
    print(3 if code != 0 else checker_verdict)
elif interactor_verdict == 1:
    print(checker_verdict)
elif interactor_verdict == 4:
    print(3 if code != 0 else 4)
elif interactor_verdict == 6:
    print(0)
elif interactor_verdict == 7:
    print(1)
else:
    print(interactor_verdict)
