%struct.A = type { i32 }define dso_local <TYPE> @main() {

	; <label>: 25
	%1 = alloca %struct.A*
	%2 = alloca i32

	; <label>: b1
	%2 = load i32, i32* 4
	%3 = call %struct.A* foo ()
	%4 = getelementptr %struct.A*, %struct.A** %3 i1 0, i32 0
	ret i32 %4
}
define dso_local <TYPE> @foo() {

	; <label>: 4a
	%1 = alloca %struct.A*

	; <label>: a2
	ret %struct.A* %1
}