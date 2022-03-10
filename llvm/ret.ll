
define dso_local i32 @foo(i32) {

L66:
	%t1 = alloca i32
	br label %L15

L15:
	%t2 = load i32, i32* %t1
	ret i32 %t2
}
define dso_local i32 @main(i32) {

L38:
	%t1 = alloca i32
	%t2 = alloca i32
	br label %L31

L31:
	store i32 1, i32* %t1
	%t3 = load i32, i32* %t1
	%t4 = icmp sgt i32 %t3, 0
	br i1 %t4, label %L71, label %L87

L71:
	ret i32 1

L87:
	ret i32 1
}