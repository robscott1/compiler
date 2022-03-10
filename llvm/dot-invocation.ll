%struct.A = type { i32 }
define dso_local i32 @main() {

L35:
	%t1 = alloca %struct.A*
	%t2 = alloca i32
	br label %L83

L83:
	store i32 4, i32* %t2
	%t3 = call %struct.A* @foo()
	%t4 = getelementptr %struct.A, %struct.A* %t3, i1 0, i32 0
	ret i32 %t4
}
define dso_local %struct.A @foo() {

L68:
	%t1 = alloca %struct.A*
	br label %L34

L34:
	%t2 = load %struct.A*, %struct.A** %t1
	ret %struct.A* %t2
}