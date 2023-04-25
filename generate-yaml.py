for i in range(1000, 1500):
    print("    - name: " + '"' + str(i * 10 + 1) + '"')
    print("      run: |")
    print("        python piecewise-prepare-report.py --start " + '"' + str(i * 10 + 1) + '"')
    print()