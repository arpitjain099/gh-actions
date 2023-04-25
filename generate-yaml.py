for i in range(1):
    print("    - name: " + str(i * 100 + 1) + " - Run Python script")
    print("      run: |")
    print("        python piecewise-prepare-report.py --start " + str(i * 100 + 1))
    print()