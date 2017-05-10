from django.test import TestCase

# Create your tests here.
def run_tests(test_labels, verbosity=1, interactive=True, extra_tests=[]):
    result = TeamcityTestRunner().run(suite)
