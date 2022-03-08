
define dso_local i32 @main() {

	; <label>: 2c
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: 2c
	%t3 = add i32 4, 2
	store %t3 i32, i32* %t1
	%t4 = load i32, i32* %t1
	store %t4 i32*, i32* %t2
	ret i32 3
}