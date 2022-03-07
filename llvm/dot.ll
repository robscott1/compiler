%struct.A = type { i32 }define dso_local <TYPE> @main() {

	; <label>: 25
	%1 = alloca %struct.A*
	%2 = alloca i32

	; <label>: 12
	%3 = call i32 f ()
	%4 = icmp lt i1 0, %3
	br i1 %4 label 74 label 45

	; <label>: 74
	ret i32 4

	; <label>: 45
	%5 = getelementptr %struct.A*, %struct.A** %1 i1 0, i32 0
	ret i32 %5
}
define dso_local <TYPE> @f() {

	; <label>: da
	%1 = alloca i32

	; <label>: 86
	%1 = load i32, i32* 4
	ret i32 %1
}