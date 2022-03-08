%struct.A = type { i32, i32 }
define dso_local i32 @main() {

	; <label>: LABEL@5d
	%t1 = alloca i32

	; <label>: LABEL@50
	%t2 = (i8* ...) @__isoc99__scanf(i8* getelementptr([4 x i8], [4 x i8]* @.str.1, i32 0, i32 0) i32 %t0)
	store i32 %t0, i32* %t1
	ret i32 3
}