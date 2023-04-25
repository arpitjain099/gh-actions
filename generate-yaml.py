for i in range(1500, 2300):
    print("    - name: " + '"' + str(i * 10 + 1) + '"')
    print("      run: |")
    print("        python piecewise-prepare-report.py --start " + '"' + str(i * 10 + 1) + '"')
    print()