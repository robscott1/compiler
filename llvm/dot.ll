%struct.A = type { i32 }
define dso_local i32 @main() {

	; <label>: eb
	%t1 = alloca %struct.A*
	%t2 = alloca i32

	; <label>: 40
	%t3 = call i32 @f()
	%t4 = icmp slt i1 0, %t3
	br i1 %t4, label fa, label 83

	; <label>: fa
	ret i32 4

	; <label>: 83
	%t5 = load %struct.A*, %struct.A** %t1
	%t6 = getelementptr %struct.A, %struct.A* %t5 i1 0, i32 0
	ret i32 %t6
}
define dso_local i32 @f() {

	; <label>: f4
	%t1 = alloca i32

	; <label>: 95
	store i32 4, i32* %t1
	%t2 = load i32, i32* %t1
	ret i32 %t2
}