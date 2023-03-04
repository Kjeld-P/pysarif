import sys
import src.pysarif

SARIF_FILEPATH = "2_cpp_autosar_non-identical-identifier-used-for-the-parameter-in-re-declaration-of-a-function.sarif"

def main() -> int:
    sarif = src.pysarif.load_from_file(SARIF_FILEPATH)
    print(sarif.runs[0].tool.driver.associated_component)
    src.pysarif.save_to_file(sarif, "test.sarif")

if __name__ == '__main__':
    sys.exit(main())