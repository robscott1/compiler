
define dso_local i32 @main() {

	; <label>: 0e
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: 81
	%t3 = add i32 4, 2
	%t1 = load i32, i32* %t3
	%t2 = load i32, i32* %t1
	ret i32 3
}