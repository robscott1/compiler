%tstruct.A = type { i32 i32 }
define dso_local i32 @main() {

	; <label>: 7b
	%t1 = alloca i32

	; <label>: d9
	%t2 = (i8* ...) @__isoc99__scanf(i8* getelementptr([4 x i8], [4 x i8]* @.str.1, i32 0, i32 0) i32 %t0)
	%t1 = load i32, i32* %t0
	ret i32 3
}