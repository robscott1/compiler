%struct.A = type { i32 }
define dso_local i32 @main() {

	; <label>: d0
	%1 = alloca %struct.A*
	%2 = alloca i32

	; <label>: 62
	%3 = call i32 f ()
	%4 = icmp lt i1 0, %3
	br i1 %4 label e8 label ba

	; <label>: e8
	ret i32 4

	; <label>: ba
	%5 = getelementptr %struct.A*, %struct.A** %1 i1 0, i32 0
	ret i32 %5
}
define dso_local i32 @f() {

	; <label>: 3a
	%1 = alloca i32

	; <label>: da
	%1 = load i32, i32* 4
	ret i32 %1
}