
define dso_local i32 @main() {

	; <label>: 0e
	%1 = alloca i32
	%2 = alloca i32

	; <label>: 81
	%3 = add i32 4, 2
	%1 = load i32, i32* %3
	%2 = load i32, i32* %1
	ret i32 3
}