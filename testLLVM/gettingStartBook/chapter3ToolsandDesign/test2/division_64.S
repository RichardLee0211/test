	.section	__TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 13
	.globl	_main
	.p2align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## BB#0:
	pushq	%rbp
Lcfi0:
	.cfi_def_cfa_offset 16
Lcfi1:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
Lcfi2:
	.cfi_def_cfa_register %rbp
	subq	$32, %rsp
	leaq	L_.str(%rip), %rdi
	leaq	-16(%rbp), %rsi
	leaq	-24(%rbp), %rdx
	movl	$0, -4(%rbp)
	movq	$0, -16(%rbp)
	movq	$0, -24(%rbp)
	movb	$0, %al
	callq	_scanf
	leaq	L_.str.1(%rip), %rdi
	movq	-16(%rbp), %rdx
	movl	%eax, -28(%rbp)         ## 4-byte Spill
	movq	%rdx, %rax
	xorl	%ecx, %ecx
	movl	%ecx, %edx
	divq	-24(%rbp)
	movq	%rax, %rsi
	movb	$0, %al
	callq	_printf
	xorl	%ecx, %ecx
	movl	%eax, -32(%rbp)         ## 4-byte Spill
	movl	%ecx, %eax
	addq	$32, %rsp
	popq	%rbp
	retq
	.cfi_endproc

	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"%lld %lld"

L_.str.1:                               ## @.str.1
	.asciz	"64-bit division is %lld\n"


.subsections_via_symbols
