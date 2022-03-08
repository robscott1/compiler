%tstruct.A = type { i32 }
define dso_local i32 @main() {

	; <label>: 6c
	%t1 = alloca %tstruct.A*
	%t2 = alloca i32

	; <label>: 69
	%t2 = load i32, i32* 4
	%t3 = call %tstruct.A* foo ()
	%t4 = getelementptr %tstruct.A*, %tstruct.A** %t3 i1 0, i32 0
	ret i32 %t4
}
define dso_local %tstruct.A @foo() {

	; <label>: be
	%t1 = alloca %tstruct.A*

	; <label>: 1f
	ret %tstruct.A* %t1
}