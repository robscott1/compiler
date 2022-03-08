%tstruct.A = type { i32 }
define dso_local i32 @main() {

	; <label>: d0
	%t1 = alloca %tstruct.A*
	%t2 = alloca i32

	; <label>: 62
	%t3 = call i32 f ()
	%t4 = icmp lt i1 0, %t3
	br i1 %t4 label e8 label ba

	; <label>: e8
	ret i32 4

	; <label>: ba
	%t5 = getelementptr %tstruct.A*, %tstruct.A** %t1 i1 0, i32 0
	ret i32 %t5
}
define dso_local i32 @f() {

	; <label>: 3a
	%t1 = alloca i32

	; <label>: da
	%t1 = load i32, i32* 4
	ret i32 %t1
}