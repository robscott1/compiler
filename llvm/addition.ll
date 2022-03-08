
define dso_local i32 @main() {

	; <label>: 68
	%t1 = alloca i32
	%t2 = alloca i32

	; <label>: d5
	%t3 = add i32 4, 2
	store i32 %t3, i32* %t1
	%t4 = load i32, i32* %t1
	store i32 %t4, i32* %t2
	ret i32 3
}