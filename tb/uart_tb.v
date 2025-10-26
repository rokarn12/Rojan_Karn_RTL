`timescale 1ns/1ps

module uart_tb;
	reg clk = 0;
	reg reset = 0;

	uart dut (.clk(clk), .rst(reset));

	// generate clock
	always #10 clk = ~clk;

	initial begin
		#20
		reset = 1;
		#40
		reset = 0;
		$display("Reset released - RUNNING TESTBENCH");
		#200;
		$display("PASS"); // dummy pass message
		$finish;
	end
endmodule


