# Lab 1 – CI with GitHub Actions

MLOps (IE-7374), Northeastern University

Based on Github_Labs/Lab1 from https://github.com/raminmohammadi/MLOps

## What I Learned From This Lab

### 1. What CI Actually Means
Before this, I knew CI as a term. Now I understand it practically:

* I push code to GitHub
* GitHub starts a fresh computer
* It installs Python and my requirements
* It runs all my tests
* It shows a green check if everything passes, red if something breaks

So the tests run on GitHub's computer, not mine. If they pass there, the code works for everyone, not only on my laptop.

### 2. Tests Check Answers, Not Code
A test only checks that the output is correct for the examples I give it.

For example, if someone wrongly calculates F1 as the average of precision and recall, it still gives the right answer whenever precision and recall are equal. So a weak test would not catch that mistake.

That is why I tested many different cases.

## Customizations I Made

### 1. Replaced Calculator With ML Metrics
The original lab had a calculator (add, subtract, multiply).

I replaced it with an ML metrics module in `src/metrics.py`:

* accuracy – how many predictions were correct
* precision – when the model predicted 1, how often it was right
* recall – of all real 1s, how many the model caught
* f1_score – one score that balances precision and recall

Reason:
In ML, metrics decide which model is best. If metrics are wrong, the wrong model gets picked. So this is code that really needs testing.

### 2. Added Input Checks
The functions now raise an error if:

* the lists are empty
* the lists have different lengths

Reason: a clear error is better than silently giving a wrong score.

### 3. Stronger Tests
* Pytest: 17 tests (original had 4)
* Unittest: 6 tests (original had 4)

They include multiple input cases, edge cases (like when there is nothing to divide by), and error checks.

### 4. Updated CI Workflows
* Runs on pull requests too, not only on push
* Tests on Python 3.12, 3.13 and 3.14 (original used only 3.8, which is no longer supported)
* Updated GitHub Actions to current versions, because the original `upload-artifact@v2` no longer works
* Saves a separate test report for each Python version

## How To Run (For TA)

### Step 1 – Run Locally

```
python3 -m venv lab_01
source lab_01/bin/activate
pip install -r requirements.txt
pytest test/test_pytest.py -v
python3 -m unittest test.test_unittest -v
```

You should see `17 passed` for pytest and `Ran 6 tests ... OK` for unittest.

### Step 2 – Check GitHub Actions
1. Open the Actions tab
2. Both "Testing with Pytest" and "Python Unittests" should have a green check
3. Click any run to see three jobs, one for each Python version
4. Scroll down to Artifacts to see the test reports

## Final Reflection
The main thing I learned is that CI is a safety check that runs on every change. Mistakes get caught right away instead of after they cause problems.