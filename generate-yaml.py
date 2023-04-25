for i in range(2):
    print("    - name: " + str(i * 10 + 1) + " - Run Python script")
    print("      run: |")
    print("        python piecewise-prepare-report.py --start " + str(i * 10 + 1))
    print()