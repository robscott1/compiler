%struct.A = type { i32 i32 }define dso_local <TYPE> @main() {

	; <label>: 1e
	%1 = alloca %struct.A*
	%2 = alloca i32

	; <label>: 59
	%3 = (i8* ...) @__isoc99__scanf(i8* getelementptr([4 x i8], [4 x i8]* @.str.1, i32 0, i32 0) i32 %0)
	%2 = load i32, i32* %0
	ret i32 3
}