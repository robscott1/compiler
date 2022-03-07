%struct.A = type { i32 i32 }define dso_local <TYPE> @main() {

	; <label>: 0a
	%1 = alloca i32

	; <label>: c4
	%2 = (i8* ...) @__isoc99__scanf(i8* getelementptr([4 x i8], [4 x i8]* @.str.1, i32 0, i32 0) i32 %0)
	%1 = load i32, i32* %0
	ret i32 3
}