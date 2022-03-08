%struct.A = type { i32 }
define dso_local i32 @main() {

	; <label>: 6c
	%1 = alloca %struct.A*
	%2 = alloca i32

	; <label>: 69
	%2 = load i32, i32* 4
	%3 = call %struct.A* foo ()
	%4 = getelementptr %struct.A*, %struct.A** %3 i1 0, i32 0
	ret i32 %4
}
define dso_local %struct.A @foo() {

	; <label>: be
	%1 = alloca %struct.A*

	; <label>: 1f
	ret %struct.A* %1
}