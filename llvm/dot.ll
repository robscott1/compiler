%struct.A = type { i32 }define dso_local <TYPE> @main() {

	; <label>: d0
	%1 = alloca %struct.A*
	%2 = alloca i32

	; <label>: e4
	%3 = call i32 f ()
	%4 = icmp lt i1 0, %3
	br i1 %4 label 58 label a8

	; <label>: 58
	ret i32 4

	; <label>: a8
	%5 = getelementptr %struct.A*, %struct.A** %1 i1 0, i32 0
	ret i32 %5
}
define dso_local <TYPE> @f() {

	; <label>: b2
	%1 = alloca i32

	; <label>: ed
	%1 = load i32, i32* 4
	ret i32 %1
}