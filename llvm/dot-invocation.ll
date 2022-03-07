%struct.A = type { i32 }define dso_local <TYPE> @main() {

	; <label>: e0
	%1 = alloca %struct.A*
	%2 = alloca i32

	; <label>: ac
	%2 = load i32, i32* 4
	%3 = call %struct.A* foo ()
	%4 = getelementptr %struct.A*, %struct.A** %3 i1 0, i32 0
	ret i32 %4
}
define dso_local <TYPE> @foo() {

	; <label>: ba
	%1 = alloca %struct.A*

	; <label>: e5
	ret %struct.A* %1
}