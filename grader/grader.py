#!/usr/bin/env python3
"""
Simple grader for UART RX bug challenge
Runs testbench and reports PASS/FAIL with test count
"""

import subprocess
import sys
import os

def run_testbench():
    """Run the UART RX testbench"""
    print("="*60)
    print("UART RX Bug Challenge - Grader")
    print("="*60)
    
    # Change to tb directory
    tb_dir = os.path.join(os.path.dirname(__file__), 'tb')
    if not os.path.exists(tb_dir):
        tb_dir = 'tb'
    
    print(f"\nRunning testbench in: {os.path.abspath(tb_dir)}")
    print("-"*60)
    
    try:
        # Run the test
        result = subprocess.run(
            ['python3', 'test_uart_rx.py'],
            cwd=tb_dir,
            capture_output=True,
            text=True,
            timeout=60
        )
        
        # Print output
        print(result.stdout)
        
        if result.stderr:
            print("STDERR:", file=sys.stderr)
            print(result.stderr, file=sys.stderr)
        
        # Check for success
        if result.returncode == 0:
            print("-"*60)
            print("Grade: PASS ✓")
            print("All tests passed!")
            print("="*60)
            return 0
        else:
            # Count which test failed
            test_count = count_passed_tests(result.stdout + result.stderr)
            print("-"*60)
            print(f"Grade: FAIL ✗")
            print(f"Tests passed: {test_count}/4")
            print(f"Pass rate: {(test_count/4)*100:.1f}%")
            print("="*60)
            return 1
            
    except subprocess.TimeoutExpired:
        print("-"*60)
        print("Grade: FAIL ✗")
        print("Error: Testbench timed out (>60s)")
        print("="*60)
        return 1
    except FileNotFoundError:
        print("-"*60)
        print("Grade: ERROR")
        print("Error: Could not find test_uart_rx.py")
        print("="*60)
        return 1
    except Exception as e:
        print("-"*60)
        print("Grade: ERROR")
        print(f"Error: {str(e)}")
        print("="*60)
        return 1

def count_passed_tests(output):
    """Count how many tests passed before failure"""
    test_markers = [
        'test 1: p test',
        'test 2: walk',
        'test 3: walk 2', 
        'test 4: r test'
    ]
    
    passed = 0
    for marker in test_markers:
        if marker in output:
            # Check if this test section has an error
            test_start = output.find(marker)
            # Find next test or end of output
            next_test_pos = len(output)
            for other_marker in test_markers[test_markers.index(marker)+1:]:
                pos = output.find(other_marker, test_start)
                if pos != -1:
                    next_test_pos = pos
                    break
            
            test_section = output[test_start:next_test_pos]
            
            # Check for errors in this section
            if 'AssertionError' in test_section or 'Traceback' in test_section:
                break  # This test failed, stop counting
            else:
                passed += 1
        else:
            break  # Test didn't even start
    
    return passed

if __name__ == '__main__':
    exit_code = run_testbench()
    sys.exit(exit_code)
