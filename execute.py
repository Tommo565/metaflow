import subprocess
import sys
from metaflow import FlowSpec, step


class TestPipeline(FlowSpec):
    
    @step
    def start(self):
        print("Starting Execution...")
        self.next(self.run_test1)
        
    @step
    def run_test1(self):
        subprocess.run([
            sys.executable, "execution_scripts/test1.py", "run"]
        )
        self.next(self.run_test2)
        
    @step
    def run_test2(self):
        subprocess.run([
            sys.executable, "execution_scripts/test2.py", "run"]
        )
        self.next(self.run_test3)
        
    @step
    def run_test3(self):
        subprocess.run([
            sys.executable, "execution_scripts/test3.py", "run"]
        )
        self.next(self.end)
        
    @step
    def end(self):
        print("Execution Complete! Have a nice day =)")
    


if __name__ == "__main__":
    TestPipeline()
        